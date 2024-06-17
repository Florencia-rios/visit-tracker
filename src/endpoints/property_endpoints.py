from flask import jsonify, request
from flask_classful import FlaskView, route

from src.dto.request_property import RequestProperty
from src.repository.property_repository import PropertyRepository


class PropertyEndpoints(FlaskView):
    route_base = '/property'
    property_repository = PropertyRepository("./src/db/visit_tracker.db")

    @route('/<property_id>/', methods=['GET'])
    def get(self, property_id: str):
        # '/property/<property_id>/' (GET)
        response = self.property_repository.get_property(property_id)

        if response != "Not found":
            return jsonify(response.dict()), 200
        else:
            return jsonify(response), 404

    @route('/', methods=['POST'])
    def post(self):
        # '/property/' (POST)
        request_data = request.json
        property = RequestProperty(**request_data)
        response = self.property_repository.create_property(property)

        return jsonify(response), 201

    @route('/<property_id>/', methods=['PUT'])
    def put(self, property_id: str):
        # '/property/<property_id>/' (PUT)
        request_data = request.json
        property = RequestProperty(**request_data)
        response = self.property_repository.update_property(property, property_id)

        return jsonify(response), 200

    @route('/<property_id>/', methods=['DELETE'])
    def delete(self, property_id: str):
        # '/property/<property_id>/' (DELETE)
        response = self.property_repository.delete_property(property_id)

        return jsonify(response), 200
