from datetime import datetime

from pydantic import BaseModel

from dto.response_employee import ResponseEmployee
from dto.response_property import ResponseProperty


class ResponsePropertyVisit(BaseModel):
    id: int
    employee: ResponseEmployee
    property: ResponseProperty
    date_time: datetime
    comments: str

    def __init__(self, id: int, employee: ResponseEmployee, property: ResponseProperty, date_time: datetime, comments: str):
        super().__init__(id=id, employee=employee, property=property, date_time=date_time, comments=comments)
