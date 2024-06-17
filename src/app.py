from flask import Flask

from endpoints.employee_endpoints import EmployeeEndpoints
from endpoints.metrics_analysis_endpoints import MetricsAnalysisEndpoints
from endpoints.property_endpoints import PropertyEndpoints
from endpoints.property_visit_endpoints import PropertyVisitEndpoints

app = Flask(__name__)

# Registro las vistas de Flask-Classful
EmployeeEndpoints.register(app)
PropertyEndpoints.register(app)
PropertyVisitEndpoints.register(app)
MetricsAnalysisEndpoints.register(app)

if __name__ == '__main__':
    app.run(debug=True)
