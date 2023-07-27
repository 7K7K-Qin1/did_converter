from dataclasses import dataclass

@dataclass
class DidObject:
    name: str
    flat_number: str
    floor_number: str
    building_name: str
    area: str
    district: str
    city: str
    country: str
