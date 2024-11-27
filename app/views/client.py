from datetime import datetime

from pydantic import BaseModel, ConfigDict


class NewClient(BaseModel):
    last_name: str
    first_name: str
    middle_name: str
    email: str
    phone_number: str
    password: str


class SavedClient(NewClient):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    timestamp: datetime


class ViewClient(SavedClient):
    model_config = ConfigDict(
        fields=[
            {'password': {'exclude': True}}
        ]
    )
