from pydantic import BaseModel


class RequestPropertyVisit(BaseModel):
    employee_id: str
    property_id: str
    comments: str

    def __init__(self, employee_id: str, property_id: str, comments: str):
        super().__init__(employee_id=employee_id, property_id=property_id, comments=comments)
