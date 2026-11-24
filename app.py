import os
import db
from flask import Flask, render_template, abort, request, redirect, url_for

app = Flask(__name__)

app.config["DATABASE"] = os.path.join(app.instance_path, "salon.sqlite")
os.makedirs(app.instance_path, exist_ok=True)
db.init_app(app)

calendar_events = [
    {"id": 1, "staff": "Sophia", "service": "Haircut", "date": "2026-11-24", "time": "09:00 AM"},
    {"id": 2, "staff": "Emma", "service": "Manicure", "date": "2026-11-24", "time": "11:00 AM"},
    {"id": 3, "staff": "Olivia", "service": "Facial", "date": "2026-11-24", "time": "02:00 PM"}
]

appointment_data = [
    {"id": 1, "service": "Haircut", "date": "2026-11-20", "time": "10:00 AM", "status": "Confirmed"},
    {"id": 2, "service": "Manicure", "date": "2026-11-21", "time": "01:00 PM", "status": "Completed"},
    {"id": 3, "service": "Facial", "date": "2026-11-22", "time": "03:00 PM", "status": "Confirmed"}
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/services", endpoint="services")
def services_page():
    database = db.get_db()
    services = database.execute(
        """
        SELECT id, name, category, duration_minutes AS duration,
               price_cents, description
        FROM services
        WHERE active = 1
        ORDER BY name
        """
    ).fetchall()
    return render_template("services.html", services=services)


@app.route("/services/<int:service_id>")
def service_detail(service_id):
    database = db.get_db()
    service = database.execute(
        """
        SELECT id, name, category, duration_minutes AS duration,
               price_cents, description
        FROM services
        WHERE id = ? AND active = 1
        """,
        (service_id,)
    ).fetchone()

    if service is None:
        abort(404)

    return render_template("service-detail.html", service=service)


@app.route("/book")
def book():
    database = db.get_db()
    services = database.execute(
        """
        SELECT id, name, duration_minutes AS duration, price_cents
        FROM services
        WHERE active = 1
        ORDER BY name
        """
    ).fetchall()
    return render_template("book.html", services=services)


@app.route("/admin/services/new", methods=("GET", "POST"))
def new_service():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()
        description = request.form.get("description", "").strip()
        duration = request.form.get("duration", "").strip()
        price = request.form.get("price", "").strip()
        error = None

        if not name:
            error = "Service name is required."
        elif not category or not description:
            error = "Category and description are required."
        else:
            try:
                duration_minutes = int(duration)
                price_cents = round(float(price) * 100)
                if duration_minutes <= 0 or price_cents < 0:
                    raise ValueError
            except ValueError:
                error = "Enter a valid duration and price."

        if error is None:
            database = db.get_db()
            database.execute(
                """
                INSERT INTO services
                    (name, category, duration_minutes, price_cents, description)
                VALUES (?, ?, ?, ?, ?)
                """,
                (name, category, duration_minutes, price_cents, description)
            )
            database.commit()
            return redirect(url_for("services"))

        return render_template("new-service.html", error=error)

    return render_template("new-service.html")


@app.route("/calendar")
def calendar():
    return render_template("calendar.html", calendar_events=calendar_events)


@app.route("/appointments", endpoint="appointments")
def appointments_page():
    return render_template("appointments.html", appointments=appointment_data)


if __name__ == "__main__":
    app.run(debug=True)
