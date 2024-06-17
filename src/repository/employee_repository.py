import sqlite3

from dto.request_employee import RequestEmployee
from dto.response_employee import ResponseEmployee


class EmployeeRepository:
    def __init__(self, db_file="./db/visit_tracker.db"):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR NOT NULL,
            mail VARCHAR NOT NULL,
            document VARCHAR NOT NULL
        )
        """)
        self.conn.commit()

    def get_employee(self, employee_id):
        self.cursor.execute("SELECT * FROM employee WHERE id = ?", (employee_id,))
        row = self.cursor.fetchone()

        if row:
            return ResponseEmployee(id=row[0], name=row[1], mail=row[2], document=row[3])
        else:
            return "Not found"

    def create_employee(self, employee: RequestEmployee):
        self.cursor.execute("INSERT INTO employee (name, mail, document) VALUES (?, ?, ?)",
                            (employee.name, employee.mail, employee.document))

        self.conn.commit()

        row_id = self.cursor.lastrowid

        if row_id:
            return f"Employee with employeeId {row_id} is created"
        else:
            return "Not created"

    def update_employee(self, employee_id, employee: RequestEmployee):
        self.cursor.execute("UPDATE employee SET name = ?, mail = ?, document = ? WHERE id = ?",
                            (employee.name, employee.mail, employee.document, employee_id))
        self.conn.commit()

        rowcount = self.cursor.rowcount

        if rowcount != 0:
            return f"Employee with employeeId {employee_id} is updated"
        else:
            return "Not updated"

    def delete_employee(self, employee_id):
        self.cursor.execute("DELETE FROM employee WHERE id = ?", (employee_id,))
        self.conn.commit()

        rowcount = self.cursor.rowcount

        if rowcount != 0:
            return f"Employee with employeeId {employee_id} is deleted"
        else:
            return "Not deleted"

    def close_connection(self):
        self.conn.close()
