DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'client'
);

CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    duration_minutes INTEGER NOT NULL,
    price_cents INTEGER NOT NULL,
    description TEXT NOT NULL,
    active INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    service_id INTEGER NOT NULL,
    client_name TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Booked',
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);

INSERT INTO services
    (name, category, duration_minutes, price_cents, description, active)
VALUES
    ('Haircut', 'Hair', 45, 3500, 'Professional haircut and styling.', 1),
    ('Hair Coloring', 'Hair', 120, 8500, 'Professional hair coloring.', 1),
    ('Manicure', 'Nails', 45, 3000, 'Nail shaping and polish.', 1),
    ('Pedicure', 'Nails', 60, 4000, 'Relaxing foot treatment.', 1),
    ('Facial', 'Skin Care', 60, 5500, 'Refreshing facial treatment.', 1),
    ('Blowout', 'Hair', 45, 4500, 'Professional blowout and styling.', 1);

INSERT INTO appointments
    (service_id, client_name, date, time, status, notes)
VALUES
    (1, 'Maria Garcia', '2026-12-01', '10:00', 'Booked', 'First appointment'),
    (2, 'Sophia Smith', '2026-12-02', '13:00', 'Booked', 'Hair color appointment'),
    (3, 'Emma Johnson', '2026-12-03', '15:00', 'Booked', 'Regular client');
