from fastapi import FastAPI, Path
# # You can use the jsonable_encoder to convert the input data to data that can be
# # stored as JSON (e.g. with a NoSQL database). For example, converting datetime to str.
# from fastapi.encoders import jsonable_encoder

# we add optional for more practice to remove require msg in dosc fname
from typing import Optional, Dict
from pydantic import BaseModel


# named the api
app = FastAPI()


users = {
    1: {
        'fname': 'Dilshad',
        'lname': 'Abdulla',
        'email': 'dilshad.abdulla@icloud.com',
        'date_of_birth': '01.01.1977'
    },
    2: {
        'fname': 'Alan',
        'lname': 'Shkar',
        'email': 'alan.shkar@gmail.com',
        'date_of_birth': '22.03.1999'
    },
    3: {
        'fname': 'Simone',
        'lname': 'David',
        'email': 'simone.david@outlook.com',
        'date_of_birth': '14.09.1986'
    }
}


class User(BaseModel):
    fname: str
    lname: str
    email: str
    date_of_birth: str

# for update clss User need to create another class to make all fields Optional
class UpdateUser(BaseModel):
    fname: Optional[str] = None
    lname: Optional[str] = None
    email: Optional[str] = None
    date_of_birth: Optional[str] = None



# This is first simple api to create it
@app.get('/')
def index():
    data = {'app': 'FastAPI',
            'msg': 'Welcome to FastAPI application', 'data': users}
    return data


@app.get('/user/{user_id}')
def get_user(user_id: int=Path(description='View user id details', gt=0, lt=4)):
    try:
        data = users[user_id]
        if data != None:
            return {'msg': 'success', 'data': users[user_id]}
        else:
            return {'msg': 'id not found'}

    except Exception as e:
        return {'msg': f'Error occurred: {e}'}


# create retrive for user name if we add {fname} or {lname} or {user_id} after user_name/
# in this case display in docs as required even put Optional 
@app.get('/user_name/{fname}')
def user_name(*, fname: Optional[str]=None, lname: Optional[str]=None, user_id: int=None, test: Optional[int]=None):
    for user_id in users:
        if users[user_id]['fname'] == fname or users[user_id]['lname'] == lname:
            return {'msg': 'success', 'data': users[user_id]}
    return {'msg': 'This user is not found'}

# We create a new user using POST methods
@app.post('/create_user/{user_id}')
def create_new_user(user_id: int, user: User):
    if user_id in users:
        return {'Error': 'This user id is exists, try again'}

    users[user_id] = user
    return users[user_id]

# Create update using put methods
@app.put('/user_update/{user_id}')
def update_user(user_id: int, user: UpdateUser, ):

    if user_id not in users:
        return {'Error': 'This user id does not exists, try again'}

    if user.fname != None:
        users[user_id].fname = user.fname

    if user.lname != None:
        users[user_id].lname = user.lname

    if user.email != None:
        users[user_id].email = user.email

    if user.date_of_birth != None:
        users[user_id].date_of_birth = user.date_of_birth

    return users[user_id]


# delete user
@app.delete('/delete/{user_id}')
def delete_user(user_id: int):
    if user_id not in users:
        return {'msg': 'This user id is not exisit, please try again'}

    del users[user_id]
    return {'msg': 'The user has been deleted sucessfully.'}