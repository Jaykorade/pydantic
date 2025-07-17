from pydantic import BaseModel

class Address(BaseModel):
    pin:str
    street: str
    city: str
    

class Patient(BaseModel):

    name: str = 'Jack'
    gender : str
    age: int
    address: Address

address_dict = {"pin": "410222",
    "street": "MG ROAD",
    "city": "Delhi"}

address1 = Address(**address_dict)

patient_dict = { "name":'Jack',
    "gender" : "male",
    "age": 35,
    "address": address1
}


Patient23 = Patient(**patient_dict)

print(Patient23.address.pin)