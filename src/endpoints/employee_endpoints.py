from flask import jsonify
from flask_classful import FlaskView

from src.dto.request_employee import RequestEmployee
from src.repository.employee_repository import EmployeeRepository


class EmployeeEndpoints(FlaskView):
    route_base = '/employee'
    employee_repository = EmployeeRepository("/src/db/visit_tracker.db")

    def get(self, employee_id: str):
        # '/employee/<employee_id>/' (GET)
        response = self.employee_repository.get_employee(employee_id)
        return jsonify(response), 200

    def post(self, employee: RequestEmployee):
        # '/employee/' (POST)
        response = self.employee_repository.create_employee(employee)
        return jsonify(response), 201

    def put(self, employee_id: str, employee: RequestEmployee):
        # '/employee/<employee_id>/' (PUT)
        response = self.employee_repository.update_employee(employee_id, employee)
        return jsonify(response), 200

    def delete(self, employee_id: str):
        # '/employee/<employee_id>/' (DELETE)
        response = self.employee_repository.delete_employee(employee_id)
        return jsonify(response), 200
