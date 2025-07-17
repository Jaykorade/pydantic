from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
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

    @model_validator(mode="after")
    def validae_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("ateience older than 60 are not allowed if emergency no not added")
        return model



    @field_validator('email')
    @classmethod
    def email_validatior(cls,value):
        valid_domains =['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not in valid domain')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transformname(cls,value):
        return value.upper()
    
    @field_validator('age',mode="before")
    @classmethod
    def validate_age(cls,value):
        if 0 < value <100:
            return value
        else:
            raise ValueError("age should be between 0 and 100") 


def paient_update(patient:Patient):
    print(patient1.name)
    print(patient1.allergies)
    print(patient1.email)
    print(patient1.linkdin)
    
patient_info ={"name":" jayesh","email" :"jaykorade@icici.com", "linkdin":"hp://linkedi.com/1223","married":True,"age":69,"weight":80.3,
"allergies":["peanuts","shellfish"],"contact_details":{"phone":"1234567890","emergency":"8983490996","email":"jaykorade@gmail.com"}}


patient1= Patient(**patient_info) 
# *args unpacks a list or tuple → positional arguments

# **kwargs unpacks a dictionary → keyword arguments

paient_update(patient1)

