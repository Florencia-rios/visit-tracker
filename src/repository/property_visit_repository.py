import sqlite3
from datetime import datetime

from src.dto.request_property_visit import RequestPropertyVisit
from src.dto.response_employee import ResponseEmployee
from src.dto.response_property import ResponseProperty
from src.dto.response_property_visit import ResponsePropertyVisit


class PropertyVisitRepository:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS property_visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee VARCHAR NOT NULL,
            property VARCHAR NOT NULL,
            date_time VARCHAR NOT NULL,
            comments VARCHAR
        )
        """)
        self.conn.commit()

    def get_property_visit(self, property_visit_id):
        self.cursor.execute("SELECT * FROM property_visits WHERE id = ?", (property_visit_id,))
        row = self.cursor.fetchone()
        if row:
            employee = ResponseEmployee.parse_raw(row[1])
            property = ResponseProperty.parse_raw(row[2])
            date_time = datetime.fromisoformat(row[3])
            return ResponsePropertyVisit(id=row[0], employee=employee, property=property, date_time=date_time, comments=row[4])
        return None

    def create_property_visit(self, property_visit: RequestPropertyVisit):
        self.cursor.execute(
            "INSERT INTO property_visits (employee, property, date_time, comments) VALUES (?, ?, ?, ?, ?)",
            (property_visit.employee.json(), property_visit.property.json(), property_visit.date_time.isoformat(), property_visit.comments))
        self.conn.commit()

    def update_property_visit(self, property_visit_id: str, property_visit: RequestPropertyVisit):
        self.cursor.execute(
            "UPDATE property_visits SET employee = ?, property = ?, date_time = ?, comments = ? WHERE id = ?",
            (property_visit.employee.json(), property_visit.property.json(), property_visit.date_time.isoformat(), property_visit.comments, property_visit_id))
        self.conn.commit()

    def delete_property_visit(self, property_visit_id):
        self.cursor.execute("DELETE FROM property_visits WHERE id = ?", (property_visit_id,))
        self.conn.commit()

        return "Property visit deleted"

    def close_connection(self):
        self.conn.close()
