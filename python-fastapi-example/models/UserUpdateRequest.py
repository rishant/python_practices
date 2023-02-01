
from typing import List, Optional
from pydantic import BaseModel

from models.user import Role

class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]