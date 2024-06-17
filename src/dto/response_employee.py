from pydantic import BaseModel


class ResponseEmployee(BaseModel):
    id: int
    name: str
    mail: str
    document: str

    def __init__(self, id: int, name: str, mail: str, document: str):
        super().__init__(id=id, name=name, mail=mail, document=document)
