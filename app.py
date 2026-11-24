
from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample salon services (prices stored in cents)
services = [
    {"id": 1, "name": "Haircut", "category": "Hair", "duration": 45, "price_cents": 3500, "description": "Professional haircut and styling."},
    {"id": 2, "name": "Hair Coloring", "category": "Hair", "duration": 120, "price_cents": 8500, "description": "Beautiful professional hair coloring."},
    {"id": 3, "name": "Manicure", "category": "Nails", "duration": 40, "price_cents": 2500, "description": "Nail shaping and polish."},
    {"id": 4, "name": "Pedicure", "category": "Nails", "duration": 50, "price_cents": 3500, "description": "Relaxing foot and nail treatment."},
    {"id": 5, "name": "Facial", "category": "Skin Care", "duration": 60, "price_cents": 6000, "description": "Refreshing facial treatment."},
    {"id": 6, "name": "Makeup", "category": "Beauty", "duration": 60, "price_cents": 5500, "description": "Professional makeup application."}
]

# Sample staff calendar records
calendar_events = [
    {"id": 1, "staff": "Sophia", "service": "Haircut", "date": "2026-11-24", "time": "09:00 AM"},
    {"id": 2, "staff": "Emma", "service": "Manicure", "date": "2026-11-24", "time": "11:00 AM"},
    {"id": 3, "staff": "Olivia", "service": "Facial", "date": "2026-11-24", "time": "02:00 PM"}
]

# Sample appointment history
appointments = [
    {"id": 1, "service": "Haircut", "date": "2026-11-20", "time": "10:00 AM", "status": "Confirmed"},
    {"id": 2, "service": "Manicure", "date": "2026-11-21", "time": "01:00 PM", "status": "Completed"},
    {"id": 3, "service": "Facial", "date": "2026-11-22", "time": "03:00 PM", "status": "Confirmed"}
]


# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Services list page
@app.route("/services")
def services():
    return render_template("services.html", services=globals()["services"])


# Service detail page
@app.route("/services/<int:service_id>")
def service_detail(service_id):
    service = next(
        (item for item in services if item["id"] == service_id),
        None
    )

    if service is None:
        abort(404)

    return render_template("service-detail.html", service=service)


# Book appointment page
@app.route("/book")
def book():
    return render_template("book.html", services=services)


# Staff calendar page
@app.route("/calendar")
def calendar():
    return render_template("calendar.html", calendar_events=calendar_events)


# Appointment history page
@app.route("/appointments")
def appointments():
    return render_template("appointments.html", appointments=appointments)


if __name__ == "__main__":
    app.run(debug=True)
