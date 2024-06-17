from typing import List

from haversine import haversine, Unit

from src.dto.response_property import ResponseLocation, ResponseProperty
from src.repository.calculate_metrics_repository import MetricsRepository


class MetricsAnalysis:

    calculate_metrics_repository = MetricsRepository()

    def visit_properties(self, employee_id: str):
        properties: List[ResponseProperty] = self.calculate_metrics_repository.visit_properties_by_employee_id(employee_id)

        return properties

    def total_distance_traveled(self, employee_id: str):
        locations: List[ResponseLocation] = self.calculate_metrics_repository.locations_by_employee_id(employee_id)

        total_distance = 0
        for i in range(len(locations) - 1):
            coords_1 = locations[i]
            coords_2 = locations[i + 1]
            distance = haversine(coords_1, coords_2, unit=Unit.KILOMETERS)
            total_distance += distance

        return total_distance
