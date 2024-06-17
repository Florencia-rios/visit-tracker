import os

from dto.request_employee import RequestEmployee
from dto.request_property import RequestAddress, RequestLocation, RequestProperty
from dto.request_property_visit import RequestPropertyVisit
from repository.employee_repository import EmployeeRepository
from repository.property_repository import PropertyRepository
from repository.property_visit_repository import PropertyVisitRepository


class Preparation:

    def setUpDB(self):
        db_path = "./tests/data_base_preparation/fake_visit_tracker.db"

        # Employee
        employee_repository = EmployeeRepository(db_path)
        employee = RequestEmployee(name="Marcelo", mail="test@com", document="11111111")
        employee_repository.create_employee(employee)

        # Property
        property_repository = PropertyRepository(db_path)
        address = RequestAddress(street="calle falsa", number=123, floor=1, apartment="A", zip_code=1456, locality="Ciudadela", country="Argentina")
        location = RequestLocation(latitude=1.545, longitude=-88.548)
        property = RequestProperty(address=address, location=location, price=1251871)
        property_repository.create_property(property)

        # Property visit
        property_visit_repository = PropertyVisitRepository(db_path)
        property_visit = RequestPropertyVisit(employee_id=1, property_id=1, comments="Estuvo muy bueno el asesoramiento!")
        property_visit_repository.create_property_visit(property_visit)
