-- SQLite
CREATE TABLE Owners (
    owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

CREATE TABLE Cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vin VARCHAR(17) NOT NULL UNIQUE,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    color VARCHAR(30)
);

CREATE TABLE Car_Owners (
    car_owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    insurance_company VARCHAR(100),
    insurance_policy VARCHAR(50),
    FOREIGN KEY (car_id) REFERENCES Cars(car_id),
    FOREIGN KEY (owner_id) REFERENCES Owners(owner_id)
);