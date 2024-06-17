from typing import List

from pydantic import BaseModel

from dto.response_property import ResponseProperty


class ResponseMetricsVisitsProperties(BaseModel):
    properties: List[ResponseProperty]

    def __init__(self, properties: List[ResponseProperty]):
        super().__init__(properties=properties)