import unittest

from repository.metrics_repository import MetricsRepository
from tests.data_base_preparation.db_preparation import Preparation


class TestMetricsRepository(unittest.TestCase):

    def setUp(self):
        db_preparation = Preparation()
        db_preparation.setUpDB()
        self.metrics_repository = MetricsRepository("./tests/data_base_preparation/fake_visit_tracker.db")

    def test_locations_by_exist_employee_id(self):
        # Set up
        employee_id = 1

        # Execute
        response = self.metrics_repository.locations_by_employee_id(employee_id)

        # Assertion
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].latitude, 1.545)
        self.assertEqual(response[0].longitude, -88.548)

    def test_visit_properties_by_exist_employee_id(self):
        # Set up
        employee_id = 1

        # Execute
        response = self.metrics_repository.visit_properties_by_employee_id(employee_id)

        # Assertion
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].location.latitude, 1.545)
        self.assertEqual(response[0].location.longitude, -88.548)
        self.assertEqual(response[0].address.street, "calle falsa")
        self.assertEqual(response[0].address.number, 123)
        self.assertEqual(response[0].price, 1251871)

    def test_locations_by_non_exist_employee_id(self):
        # Set up
        employee_id = 88

        # Execute
        response = self.metrics_repository.locations_by_employee_id(employee_id)

        # Assertion
        self.assertEqual(len(response), 0)

    def test_visit_properties_by_non_exist_employee_id(self):
        # Set up
        employee_id = 88

        # Execute
        response = self.metrics_repository.visit_properties_by_employee_id(employee_id)

        # Assertion
        self.assertEqual(len(response), 0)


if __name__ == '__main__':
    unittest.main()
