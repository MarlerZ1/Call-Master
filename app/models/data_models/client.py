from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from app.models.data_models.main import Base


class ClientModel(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    # email_verefied = Column(Boolean, nullable=False,default=False)
    phone_number = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return (f"ClientModel(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, "
                f"middle_name={self.middle_name}, email={self.email}, phone_number={self.phone_number})")
