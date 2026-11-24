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
    duration_minutes INTEGER NOT NULL,
    price_cents INTEGER NOT NULL,
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
    (name, duration_minutes, price_cents, active)
VALUES
    ('Haircut', 45, 3500, 1),
    ('Hair Coloring', 120, 8500, 1),
    ('Manicure', 45, 3000, 1),
    ('Pedicure', 60, 4000, 1),
    ('Facial', 60, 5500, 1),
    ('Blowout', 45, 4500, 1);

INSERT INTO appointments
    (service_id, client_name, date, time, status, notes)
VALUES
    (1, 'Maria Garcia', '2026-12-01', '10:00', 'Booked', 'First appointment'),
    (2, 'Sophia Smith', '2026-12-02', '13:00', 'Booked', 'Hair color appointment'),
    (3, 'Emma Johnson', '2026-12-03', '15:00', 'Booked', 'Regular client');
