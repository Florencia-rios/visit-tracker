from pydantic import BaseModel


class ResponseTotalDistanceTraveled(BaseModel):
    total_distance: float

    def __init__(self, total_distance: float):
        super().__init__(total_distance=total_distance)
