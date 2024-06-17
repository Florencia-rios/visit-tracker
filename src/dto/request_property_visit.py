from datetime import datetime

from pydantic import BaseModel

from src.dto.request_employee import RequestEmployee
from src.dto.request_property import RequestProperty


class RequestPropertyVisit(BaseModel):
    employee: RequestEmployee
    property: RequestProperty
    date_time: datetime
    comments: str

    def __init__(self, employee: RequestEmployee, property: RequestProperty, date_time: datetime, comments: str):
        super().__init__(employee=employee, property=property, date_time=date_time, commets=comments)
