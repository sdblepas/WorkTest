from datetime import datetime

from pydantic import BaseModel


class ListItem(BaseModel):
    name: str
    description: str
    to_do_date: datetime
