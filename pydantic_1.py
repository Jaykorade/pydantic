from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : Annotated[str,Field(max_length=50,title="name of the patient",description="give name in max 50 char")]
    email : EmailStr
    linkdin : AnyUrl
    married: Annotated[bool,Field(default=None,description= "is patient married or not")]
    age : int
    weight : float = Field(gt=0,lt=100)
    allergies : Optional[List[str]]= None
    contact_details : Dict[str,str]

def paient_update(patient:Patient):
    print(patient1.name)
    print(patient1.allergies)
    print(patient1.email)
    print(patient1.linkdin)
    
patient_info ={"name":" jayesh","email" :"jaykorade@gmail.com", "linkdin":"hp://linkedi.com/1223","married":True,"age":30,"weight":80.3,
"allergies":["peanuts","shellfish"],"contact_details":{"phone":"1234567890","email":"jaykorade@gmail.com"}}


patient1= Patient(**patient_info) 
# *args unpacks a list or tuple → positional arguments

# **kwargs unpacks a dictionary → keyword arguments

paient_update(patient1)

