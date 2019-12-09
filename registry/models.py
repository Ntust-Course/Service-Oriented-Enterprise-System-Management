from dataclasses import dataclass


@dataclass
class Service:
    name: str
    location: str

    @classmethod
    def from_form(cls, form: dict):
        return cls(**form)
