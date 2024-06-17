import sqlite3
from datetime import datetime

from src.dto.request_property_visit import RequestPropertyVisit
from src.dto.response_property_visit import ResponsePropertyVisit
from src.repository.employee_repository import EmployeeRepository
from src.repository.property_repository import PropertyRepository


class PropertyVisitRepository:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()

        self.employee_repository = EmployeeRepository("./src/db/visit_tracker.db")
        self.property_repository = PropertyRepository("./src/db/visit_tracker.db")

    def _create_table_if_not_exists(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS property_visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INT,
        property_id INT,
        date_time VARCHAR NOT NULL,
        comments VARCHAR,
        FOREIGN KEY (employee_id) REFERENCES employee (id),
        FOREIGN KEY (property_id) REFERENCES property (id)
        )
        """)
        self.conn.commit()

    def get_property_visit(self, property_visit_id):
        self.cursor.execute("SELECT * FROM property_visits WHERE id = ?", (property_visit_id,))
        row = self.cursor.fetchone()

        if row:
            response_employee = self.employee_repository.get_employee(row[1])
            response_property = self.property_repository.get_property(row[2])

            return ResponsePropertyVisit(id=row[0], employee=response_employee, property=response_property, date_time=row[3],
                                         comments=row[4])
        else:
            return "Not found"

    def create_property_visit(self, property_visit: RequestPropertyVisit):
        response_employee = self.employee_repository.get_employee(property_visit.employee_id)
        response_property = self.property_repository.get_property(property_visit.property_id)
        if response_employee == "Not found" or response_property == "Not found":
            return "Not created"

        self.cursor.execute(
            "INSERT INTO property_visits (employee_id, property_id, date_time, comments) VALUES (?, ?, ?, ?)",
            (response_employee.id, response_property.id, datetime.now(), property_visit.comments))
        self.conn.commit()

        row_id = self.cursor.lastrowid

        if row_id:
            return f"Property visit with propertyVisitId {row_id} is created"
        else:
            return "Not created"

    def update_property_visit(self, property_visit_id: str, property_visit: RequestPropertyVisit):
        response_employee = self.employee_repository.get_employee(property_visit.employee_id)
        response_property = self.property_repository.get_property(property_visit.property_id)
        if response_employee == "Not found" or response_property == "Not found":
            return "Not updated"

        response_property_visit = self.get_property_visit(property_visit_id)
        if response_property_visit == "Not found":
            return "Not updated"

        self.cursor.execute(
            "UPDATE property_visits SET employee_id = ?, property_id = ?, comments = ? WHERE id = ?",
            (
                response_employee.id, response_property.id, property_visit.comments,
                property_visit_id))
        self.conn.commit()

        rowcount = self.cursor.rowcount

        if rowcount != 0:
            return f"Property visit with propertyVisitId {property_visit_id} is updated"
        else:
            return "Not updated"

    def delete_property_visit(self, property_visit_id):
        self.cursor.execute("DELETE FROM property_visits WHERE id = ?", (property_visit_id,))
        self.conn.commit()

        rowcount = self.cursor.rowcount

        if rowcount != 0:
            return f"Property visit with propertyVisitId {property_visit_id} is deleted"
        else:
            return "Not deleted"

    def close_connection(self):
        self.conn.close()
