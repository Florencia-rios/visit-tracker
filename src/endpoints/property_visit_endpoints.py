from flask import jsonify, request
from flask_classful import FlaskView, route

from dto.request_property_visit import RequestPropertyVisit
from repository.property_visit_repository import PropertyVisitRepository


class PropertyVisitEndpoints(FlaskView):
    route_base = '/property-visit'
    property_visit_repository = PropertyVisitRepository()

    @route('/<property_visit_id>/', methods=['GET'])
    def get(self, property_visit_id: str):
        # '/property-visit/<property_visit_id>/' (GET)
        response = self.property_visit_repository.get_property_visit(property_visit_id)

        if response != "Not found":
            return jsonify(response.dict()), 200
        else:
            return jsonify(response), 404

    @route('/', methods=['POST'])
    def post(self):
        # '/property-visit/' (POST)
        request_data = request.json
        property_visit = RequestPropertyVisit(**request_data)
        response = self.property_visit_repository.create_property_visit(property_visit)
        return jsonify(response), 201

    @route('/<property_visit_id>/', methods=['PUT'])
    def put(self, property_visit_id: str):
        # '/property-visit/<property_visit_id>/' (PUT)
        request_data = request.json
        property_visit = RequestPropertyVisit(**request_data)
        response = self.property_visit_repository.update_property_visit(property_visit_id, property_visit)
        return jsonify(response), 200

    @route('/<property_visit_id>/', methods=['DELETE'])
    def delete(self, property_visit_id: str):
        # '/property-visit/<property_visit_id>/' (DELETE)
        response = self.property_visit_repository.delete_property_visit(property_visit_id)
        return jsonify(response), 200
