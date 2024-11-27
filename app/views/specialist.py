from datetime import datetime
from enum import Enum
from typing import List

from pydantic import ConfigDict

from app.views.client import NewClient


class SpecializationEnum(str, Enum):
    cardiologist = 'tv'
    dermatologist = 'pc'


class NewSpecialist(NewClient):
    specialization: List[SpecializationEnum]


class SavedSpecialist(NewSpecialist):
    id: int

class ViewSpecialist(NewClient):
    id: int
    model_config = ConfigDict(
        fields=[
            {
                'password': {'exclude': True}
             }
        ]
    )
    timestamp: datetime