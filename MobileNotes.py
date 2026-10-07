from pydantic import BaseModel

class MobileNote(BaseModel):
    battery_power: int
    px_height: int
    px_width: int
    ram: int
