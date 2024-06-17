from datetime import datetime

from pydantic import BaseModel

from src.models.employee import Employee
from src.models.property import Property


class PropertyVisit(BaseModel):
    id: int
    employee: Employee
    property: Property
    date_time: datetime
    comments: str

    def __init__(self, employee: Employee, property: Property, date_time: datetime, comments: str):
        super().__init__(employee=employee, property=property, date_time=date_time, commets=comments)
