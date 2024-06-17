from typing import Optional

from pydantic import BaseModel


class Address(BaseModel):
    id: int
    street: str
    number: int
    floor: Optional[int] = None
    apartment: Optional[str] = None
    zip_code: str
    locality: str
    country: str

    def __init__(self, street: str, number: int, floor: int, apartment: str, zip_code: int, locality: str, country: str):
        super().__init__(street=street, number=number, floor=floor, apartment=apartment,
                         zip_code=zip_code, locality=locality, country=country)


class Location(BaseModel):
    id: int
    latitude: str
    longitude: str

    def __init__(self, latitude: str, longitude: str):
        super().__init__(latitude=latitude, longitude=longitude)

class Property(BaseModel):
    id: int
    address: Address
    location: Location
    price: int

    def __init__(self, address: Address, location: Location, price):
        super().__init__(address=address, location=location, price=price)
