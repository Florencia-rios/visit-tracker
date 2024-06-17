from flask import request

from flask import jsonify
from flask_classful import FlaskView, route

from src.dto.request_employee import RequestEmployee
from src.repository.employee_repository import EmployeeRepository


class EmployeeEndpoints(FlaskView):
    route_base = '/employee'
    employee_repository = EmployeeRepository("./src/db/visit_tracker.db")

    @route('/<employee_id>/', methods=['GET'])
    def get(self, employee_id: str):
        # '/employee/<employee_id>/' (GET)
        response = self.employee_repository.get_employee(employee_id)
        return jsonify(response), 200

    @route('/', methods=['POST'])
    def post(self):
        # '/employee/' (POST)
        request_data = request.json
        employee = RequestEmployee(**request_data)  # Crea un objeto RequestEmployee a partir de los datos JSON
        response = self.employee_repository.create_employee(employee)
        return jsonify(response), 201

    @route('/<employee_id>/', methods=['PUT'])
    def put(self, employee_id: str):
        # '/employee/<employee_id>/' (PUT)
        request_data = request.json
        employee = RequestEmployee(**request_data)  # Crea un objeto RequestEmployee a partir de los datos JSON
        response = self.employee_repository.update_employee(employee_id, employee)
        return jsonify(response), 200

    @route('/<employee_id>/', methods=['DELETE'])
    def delete(self, employee_id: str):
        # '/employee/<employee_id>/' (DELETE)
        response = self.employee_repository.delete_employee(employee_id)
        return jsonify(response), 200
