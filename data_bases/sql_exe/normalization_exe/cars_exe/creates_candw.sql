-- SQLite
CREATE TABLE Owners (
    owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
);


CREATE TABLE Insurance_Policies(
    policy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy_name VARCHAR(50) NOT NULL UNIQUE,     
    company VARCHAR(100) NOT NULL                
);

CREATE TABLE Car_models(
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    );


CREATE TABLE Cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vin VARCHAR(17) NOT NULL UNIQUE,
    color VARCHAR(30),
    policy_id INTEGER NOT NULL,
    model_id INTEGER NOT NULL,
    FOREIGN KEY (model_id) REFERENCES Car_models(model_id),
    FOREIGN KEY (policy_id) REFERENCES Insurance_Policies(policy_id)
);


CREATE TABLE Car_Owners (
    car_owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY (car_id) REFERENCES Cars(car_id),
    FOREIGN KEY (owner_id) REFERENCES Owners(owner_id)
);