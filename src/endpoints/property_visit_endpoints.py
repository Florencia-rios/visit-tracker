from flask import jsonify
from flask_classful import FlaskView

from src.dto.request_property_visit import RequestPropertyVisit
from src.repository.property_visit_repository import PropertyVisitRepository


class PropertyVisitEndpoints(FlaskView):
    route_base = '/property-visit'
    property_visit_repository = PropertyVisitRepository("/src/db/visit_tracker.db")

    def get(self, property_visit_id: str):
        # '/property-visit/<property_visit_id>/' (GET)
        response = self.property_visit_repository.get_property_visit(property_visit_id)
        return jsonify(response), 200

    def post(self, property_visit: RequestPropertyVisit):
        # '/property-visit/' (POST)
        response = self.property_visit_repository.create_property_visit(property_visit)
        return jsonify(response), 201

    def put(self, property_visit_id: str, property_visit: RequestPropertyVisit):
        # '/property-visit/<property_visit_id>/' (PUT)
        response = self.property_visit_repository.update_property_visit(property_visit_id, property_visit)
        return jsonify(response), 200

    def delete(self, property_visit_id: str):
        # '/property-visit/<property_visit_id>/' (DELETE)
        response = self.property_visit_repository.delete_property_visit(property_visit_id)
        return jsonify(response), 200
