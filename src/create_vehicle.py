import sqlite3
import os
import argparse

def create_vehicle_database(vehicle_name, vehicle_version, mass, halfbase_F, halfbase_R,
                           steering_ratio):

    folder_path = os.path.join('../db/vehicles/', vehicle_name, vehicle_version)
    os.makedirs(folder_path, exist_ok=True)

    # Path to the vehicle database
    db_path = os.path.join(folder_path, 'parameters.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # DB for vehicle specs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vehicle_specs (
        name TEXT PRIMARY KEY,
        mass REAL,
        halfbase_F REAL,
        halfbase_R REAL,
    )
    ''')

    # DB for tire specs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tire_specs (
        vehicle_name TEXT,
        steering_ratio REAL,
        FOREIGN KEY(vehicle_name) REFERENCES vehicle_specs(name)
    )
    ''')

    # Insert vehicle specifications into the database
    cursor.execute('''
    INSERT OR REPLACE INTO vehicle_specs (name, mass, wheelbase, inertia)
    VALUES (?, ?, ?, ?)
    ''', (vehicle_name, mass, halfbase_F, halfbase_R))

    # Insert tire specifications into the database
    cursor.execute('''
    INSERT OR REPLACE INTO tire_specs (
        vehicle_name,
        steering_ratio
    )
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        vehicle_name,
        mass,
        halfbase_F,
        halfbase_R,
        vehicle_name,
        steering_ratio
    ))

    conn.commit()
    conn.close()
    print(f"Database created successfully at {db_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a vehicle database with specifications.")

    # Vehicle parameters
    parser.add_argument('vehicle_name', type=str, help='Vehicle name')
    parser.add_argument('vehicle_version', type=str, help='Vehicle version or setup type')
    parser.add_argument('mass', type=float, help='Mass of the vehicle')
    parser.add_argument('wheelbase', type=float, help='Wheelbase of the vehicle')
    parser.add_argument('inertia', type=float, help='Inertia of the vehicle')

    # Steering parameters
    parser.add_argument('steering_ratio', type=float, default=0, help='Static toe angle Front Left')

    args = parser.parse_args()
    create_vehicle_database(
        vehicle_name=args.vehicle_name,
        vehicle_version=args.vehicle_version,
        mass=args.mass,
        halfbase_F=args.halfbase_F,
        halfbase_R=args.halfbase_R,
        steering_ratio=args.steering_ratio,
    )


# FIXME: no hardcoded values
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a vehicle database with specifications.")

    parser.add_argument('vehicle_name', type=str, help='Name of the vehicle')
    parser.add_argument('vehicle_version', type=str, help='Version of the vehicle')
    parser.add_argument('mass', type=float, help='Mass of the vehicle')
    parser.add_argument('halfbase_F', type=float, help='Half wheelbase rear')
    parser.add_argument('halfbase_R', type=float, help='Half wheelbase front')
    parser.add_argument('steering_ratio', type=float, help='Steering to wheel turning ratio')

    args = parser.parse_args()
    create_vehicle_database(
        vehicle_name=args.vehicle_name,
        vehicle_version=args.vehicle_version,
        mass=args.mass,
        halfbase_F=args.halfbase_F,
        halfbase_R=args.halfbase_R,
        steering_ratio=args.steering_ratio,
    )
