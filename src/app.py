from flask import Flask

from src.endpoints.employee_endpoints import EmployeeEndpoints
from src.endpoints.metrics_analysis_endpoints import MetricsAnalysisEndpoints
from src.endpoints.property_endpoints import PropertyEndpoints
from src.endpoints.property_visit_endpoints import PropertyVisitEndpoints

app = Flask(__name__)

# Registro las vistas de Flask-Classful
EmployeeEndpoints.register(app)
PropertyEndpoints.register(app)
PropertyVisitEndpoints.register(app)
MetricsAnalysisEndpoints.register(app)

if __name__ == '__main__':
    app.run(debug=True)
