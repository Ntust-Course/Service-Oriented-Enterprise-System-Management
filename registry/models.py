from dataclasses import dataclass


@dataclass
class Service:
    name: str
    location: str

    @classmethod
    def from_form_data(cls, form_data):
        return cls(**form_data)
