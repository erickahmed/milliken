


import sqlite3
import os
import argparse

# cog x=0 on the front wheel axis, cog_y=0 on the half track
# TODO: eventually create a wiki
def create(vehicle_name, vehicle_version, mass, wheelbase, cog_x, cog_y, cog_z, steering_ratio):

    folder_path = os.path.join('../db/vehicles/', vehicle_name, vehicle_version)
    os.makedirs(folder_path, exist_ok=True)

    # Path to the vehicle database
    db_path = os.path.join(folder_path, 'parameters.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # DB for vehicle specs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vehicle_specs (
        vehicle_name TEXT,
        vehicle_version TEXT,
        mass REAL,
        wheelbase REAL,
        cog_x REAL,
        cog_y REAL,
        cog_z REAL,
        PRIMARY KEY(vehicle_name, vehicle_version)
    )
    ''')

    # DB for tire specs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tire_specs (
        vehicle_name TEXT,
        vehicle_version TEXT,
        steering_ratio REAL,
        FOREIGN KEY(vehicle_name) REFERENCES vehicle_specs(vehicle_name),
        FOREIGN KEY(vehicle_version) REFERENCES vehicle_specs(vehicle_version)
    )
    ''')

    cursor.execute('''
    INSERT OR REPLACE INTO vehicle_specs (vehicle_name, vehicle_version, mass, wheelbase, cog_x, cog_y, cog_z)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (vehicle_name, vehicle_version, mass, wheelbase, cog_x, cog_y, cog_z))

    cursor.execute('''
    INSERT OR REPLACE INTO tire_specs (vehicle_name, vehicle_version, steering_ratio)
    VALUES (?, ?, ?)
    ''', (vehicle_name, vehicle_version, steering_ratio))

    conn.commit()
    conn.close()
    print(f"Database created successfully at {db_path}")

def load(vehicle_name, vehicle_version, *parameters):
    db_path = os.path.join('../db/vehicles/', vehicle_name, vehicle_version, 'parameters.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Load everything if no parameters are specified
    # TODO: validate this
    if not parameters:
        cursor.execute("PRAGMA table_info(vehicle_specs)")
        parameters = [row[1] for row in cursor.fetchall()]

    query = f"SELECT {', '.join(parameters)} FROM vehicle_specs WHERE vehicle_name = ? AND vehicle_version = ?"

    cursor.execute(query, (vehicle_name, vehicle_version))
    vehicle_parameters = cursor.fetchone()

    conn.close()

    if vehicle_parameters is None:
        print(f"No parameters found for {vehicle_name} version {vehicle_version}")
        return None

    return dict(zip(parameters, vehicle_parameters))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a vehicle database with specifications.")

    # Vehicle parameters
    parser.add_argument('vehicle_name', type=str, help='Vehicle name')
    parser.add_argument('vehicle_version', type=str, help='Vehicle version or setup type')
    parser.add_argument('mass', type=float, help='Mass of the vehicle')
    parser.add_argument('wheelbase', type=float, help='Front half of the wheelbase')
    parser.add_argument('cog_x', type=float, help='Center of gravity coordinate on the x axis')
    parser.add_argument('cog_y', type=float, help='Center of gravity coordinate on the y axis')
    parser.add_argument('cog_z', type=float, help='Center of gravity coordinate on the z axis')

    # Steering parameters
    parser.add_argument('steering_ratio', type=float, default=0, help='Static steering ratio')

    args = parser.parse_args()

    create(
        vehicle_name=args.vehicle_name,
        vehicle_version=args.vehicle_version,
        mass=args.mass,
        wheelbase=args.wheelbase,
        cog_x=args.cog_x,
        cog_y=args.cog_y,
        cog_z=args.cog_z,
        steering_ratio=args.steering_ratio,
    )

    '''mass, wheelbase, cog_x, cog_y, cog_z = load(args.vehicle_name, args.vehicle_version)
    if mass:
        print(f"Vehicle {args.vehicle_name} version {args.vehicle_version} parameters:")
        print(f"Mass: {mass}, Wheelbase: {wheelbase}, COG X {cog_x}, COG Y {cog_y}, COG Z {cog_z}")

    steering_ratio = load(args.vehicle_name, args.vehicle_version) #FIXME
    if steering_ratio:
        print(f"Steering Ratio: {steering_ratio}")'''
