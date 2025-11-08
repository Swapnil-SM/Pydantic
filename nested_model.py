
from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict) #creating pydantic object of Address model(class)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.city)  # Accessing nested model field

temp = patient1.model_dump()    # Converting pydantic model to dictionary
print(temp)
print(type(temp))

temp2 = patient1.model_dump_json()  # Converting pydantic model  to JSON
print(temp2)
print(type(temp2))


temp3 = patient1.model_dump(include={'name', 'pin'})  # Including specific fields from nested model
#we can also use exclude paramter to exclude specific fields
print(temp3)


temp4 = patient1.model_dump_json(exclude_unset=True)  # it will exclude fields which are not set by user(not converted to default values)
print(temp4)
# Explanation:


# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed
