import sqlite3
import os

def create_vehicle_database(vehicle_name, mass, wheelbase, inertia):
    # Create a folder for the vehicle if it doesn't exist
    folder_path = os.path.join('../db/vehicles/', vehicle_name)
    os.makedirs(folder_path, exist_ok=True)

    # Path to the vehicle-specific database
    db_path = os.path.join(folder_path, 'vehicle_specs.db')

    # Connect to the SQLite database (it will create the database if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table for vehicle specs if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vehicle_specs (
        name TEXT PRIMARY KEY,
        mass REAL,
        wheelbase REAL,
        inertia REAL
    )
    ''')

    # Insert vehicle specifications into the database
    cursor.execute('''
    INSERT OR REPLACE INTO vehicle_specs (name, mass, wheelbase, inertia)
    VALUES (?, ?, ?, ?)
    ''', (vehicle_name, mass, wheelbase, inertia))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_vehicle_database()
