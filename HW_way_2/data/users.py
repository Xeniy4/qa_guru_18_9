from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile: str
    currentAddress: str

