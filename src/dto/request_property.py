from typing import Optional

from pydantic import BaseModel


class RequestAddress(BaseModel):
    street: str
    number: int
    floor: Optional[int] = None
    apartment: Optional[str] = None
    zip_code: int
    locality: str
    country: str

    def __init__(self, id: int, street: str, number: int, floor: int, apartment: str, zip_code: int, locality: str,
                 country: str):
        super().__init__(id=id, street=street, number=number, floor=floor, apartment=apartment,
                         zip_code=zip_code, locality=locality, country=country)


class RequestLocation(BaseModel):
    latitude: str
    longitude: str

    def __init__(self, id: int, latitude: str, longitude: str):
        super().__init__(id=id, latitude=latitude, longitude=longitude)


class RequestProperty(BaseModel):
    address: RequestAddress
    location: RequestLocation
    price: int

    def __init__(self, id: int, address: RequestAddress, location: RequestLocation, price):
        super().__init__(id=id, address=address, location=location, price=price)
