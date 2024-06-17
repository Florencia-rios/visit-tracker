import unittest

from dto.request_employee import RequestEmployee
from repository.employee_repository import EmployeeRepository
from tests.data_base_preparation.db_preparation import Preparation


class TestEmployeeRepository(unittest.TestCase):

    def setUp(self):
        db_preparation = Preparation()
        db_preparation.setUpDB()
        self.employee_repository = EmployeeRepository("./tests/data_base_preparation/fake_visit_tracker.db")

    def test_get_employee_with_exist_id(self):
        # Set up
        employee_id = 1

        # Execute
        response = self.employee_repository.get_employee(employee_id)

        # Assertion
        self.assertEqual(response.name, "Marcelo")
        self.assertEqual(response.mail, "test@com")
        self.assertEqual(response.document, "11111111")

    def test_get_employee_with_non_exist_id(self):
        # Set up
        employee_id = 88

        # Execute
        response = self.employee_repository.get_employee(employee_id)

        # Assertion
        self.assertEqual(response, "Not found")

    def test_create_employee_with_exist_id(self):
        # Set up
        employee_id = 2
        employee = RequestEmployee(name="Marcelo", mail="test@com", document="11111111")

        # Execute
        response = self.employee_repository.create_employee(employee)

        # Assertion
        self.assertEqual(response, f"Employee with employeeId {employee_id} is created")

    def test_update_employee(self):
        # Set up
        employee_id = 2
        employee = RequestEmployee(name="Florencia", mail="test@com", document="11111111")

        # Execute
        response = self.employee_repository.update_employee(employee_id, employee)

        # Assertion
        self.assertEqual(response, f"Employee with employeeId {employee_id} is updated")

    def test_delete_employee(self):
        # Set up
        employee_id = 1

        # Execute
        response = self.employee_repository.delete_employee(employee_id)

        # Assertion
        self.assertEqual(response, f"Employee with employeeId {employee_id} is deleted")


if __name__ == '__main__':
    unittest.main()
