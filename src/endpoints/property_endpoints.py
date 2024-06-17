from flask import jsonify
from flask_classful import FlaskView

from src.dto.request_property import RequestProperty
from src.repository.property_repository import PropertyRepository


class PropertyEndpoints(FlaskView):
    route_base = '/property'
    property_repository = PropertyRepository("/src/db/visit_tracker.db")

    def get(self, property_id: str):
        # '/property/<property_id>/' (GET)
        response = self.property_repository.get_property(property_id)
        return jsonify(response), 200

    def post(self, property: RequestProperty):
        # '/property/' (POST)
        response = self.property_repository.create_property(property)
        return jsonify(response), 201

    def put(self, property: RequestProperty, property_id: str):
        # '/property/<property_id>/' (PUT)
        response = self.property_repository.update_property(property, property_id)
        return jsonify(response), 200

    def delete(self, property_id: str):
        # '/property/<property_id>/' (DELETE)
        response = self.property_repository.delete_property(property_id)
        return jsonify(response), 200
