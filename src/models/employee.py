from pydantic import BaseModel


class Employee(BaseModel):
    id: int
    name: str
    mail: str
    document: str

    def __init__(self, name: str, mail: str, document: str):
        super().__init__(name= name, mail=mail, document= document)
