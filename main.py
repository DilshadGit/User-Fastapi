from fastapi import FastAPI, Path
# we add optional for more practice to remove require msg in dosc fname
from typing import Optional
from pydantic import BaseModel

# named the api
app = FastAPI()

users = {
    1: {
        'id_num': 48,
        'fname': 'Dilshad',
        'lname': 'Abdulla',
        'email': 'dilshad.abdulla@icloud.com',
        'date_of_birth': '01.01.1977'
    },
    2: {
        'id_num': 26,
        'fname': 'Alan',
        'lname': 'Shkar',
        'email': 'alan.shkar@gmail.com',
        'date_of_birth': '22.03.1999'
    },
    3: {
        'id_num': 39,
        'fname': 'Simone',
        'lname': 'David',
        'email': 'simone.david@outlook.com',
        'date_of_birth': '14.09.1986'
    }
}

class User(BaseModel):
    id_num: int
    fname: str
    lname: str
    email: str
    date_of_birth: str




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
