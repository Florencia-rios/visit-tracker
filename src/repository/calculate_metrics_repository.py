import sqlite3

from src.dto.response_property import ResponseLocation, ResponseProperty, ResponseAddress


class MetricsRepository:
    def __init__(self, db_file="./src/db/visit_tracker.db"):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def locations_by_employee_id(self, employee_id):
        self.cursor.execute("""
        SELECT *
        FROM location l
        JOIN property p ON l.id = p.location_fk
        JOIN property_visit pv ON p.id = pv.property_fk
        WHERE pv.employee_fk = ?
        )
        """, (employee_id,))
        rows = self.cursor.fetchall()

        locations = [ResponseLocation(id=row[0], latitude=row[1], longitude=row[2]) for row in rows]

        return locations

    def visit_properties_by_employee_id(self, employee_id):
        self.cursor.execute("""
        SELECT 
            a.id
            a.street,
            a.number,
            a.floor,
            a.apartment,
            a.zip_code,
            a.locality,
            a.country,
            l.id
            l.latitude,
            l.longitude,
            p.id,
            p.price
        FROM employee e
        JOIN property_visit pv ON e.id = pv.employee_fk
        JOIN property p ON pv.property_fk = p.id
        JOIN address a ON p.address_fk = a.id
        JOIN location l ON p.location_fk = l.id
        WHERE e.id = ?
        """, (employee_id,))
        rows = self.cursor.fetchall()

        properties = []

        for row in rows:
            address = ResponseAddress(
                id=row[0],
                street=row[1],
                number=row[2],
                floor=row[3],
                apartment=row[4],
                zip_code=row[5],
                locality=row[6],
                country=row[7]
            )
            location = ResponseLocation(
                id=row[8],
                latitude=row[9],
                longitude=row[10]
            )
            property = ResponseProperty(
                id=row[11],
                address=address,
                location=location,
                price=row[12]
            )
            properties.append(property)

        return properties
