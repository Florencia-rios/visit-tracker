from pydantic import BaseModel


class RequestPropertyVisit(BaseModel):
    employee_id: int
    property_id: int
    comments: str

    def __init__(self, employee_id: int, property_id: int, comments: str):
        super().__init__(employee_id=employee_id, property_id=property_id, comments=comments)
