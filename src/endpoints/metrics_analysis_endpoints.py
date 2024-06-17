from flask import jsonify
from flask_classful import FlaskView, route
from metrics_analysis.metrics_analysis import MetricsAnalysis


class MetricsAnalysisEndpoints(FlaskView):
    route_base = '/metrics-analysis'
    metrics_analysis = MetricsAnalysis()

    @route('/visit-properties/<employee_id>/', methods=['GET'])
    def get_visit_properties(self, employee_id: str):
        # '/metrics-analysis/visit-properties/<employee_id>/' (GET)
        response = self.metrics_analysis.visit_properties(employee_id)

        return jsonify(response.dict()), 200

    @route('/total-distance-traveled/<employee_id>/', methods=['GET'])
    def get_total_distance_traveled(self, employee_id: str):
        # '/metrics-analysis/total-distance-traveled/<employee_id>/' (GET)
        response = self.metrics_analysis.total_distance_traveled(employee_id)

        return jsonify(response.dict()), 200
