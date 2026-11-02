from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, EquipmentInt

NameStr=Annotated[str,StringConstraints(min_lenght=2, max_length=60)]
equipment_id=Annotated[int, ConfigDict]

class UserCreate(BaseModel):

    equipment_id:EquipmentInt  
    borrower_name:NameStr
    loan_days:int=Field(ge=1, lt=14)
    purpose:str=Field(ge=5, lt=100)
    status:str="Pending"

    class UserRead(BaseModel):
        model_config=ConfigDict(from_attributes=TRUE)
        equipment_id:EquipmentInt
        borrower_name:NameStr
        loan_days:int
        purpose:str
        status:str
        
