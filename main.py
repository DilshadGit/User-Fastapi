from fastapi import FastAPI, Path
# we add optional for more practice to remove require msg in dosc fname
from typing import Optional

# named the api
app = FastAPI()

users = {
	1: {
		'id_num': 48,
		'fname': 'Dilshad',
		'lname': 'Abdulla',
		'email': 'dilshad.abdulla@icloud.com',
		'db': '01.01.1977'
	},
	2: {
		'db_id': 26,
		'fname': 'Alan',
		'lname': 'Shkar',
		'email': 'alan.shkar@gmail.com',
		'date_of_birth': '22.03.1999'
	},
	3: {
		'db_id': 39,
		'fname': 'Simone',
		'lname': 'David',
		'email': 'simone.david@outlook.com',
		'date_of_birth': '14.09.1986'
	}
}


# This is first simple api to create it
@app.get('/')
def index():
	data = {'app': 'FastAPI', 'msg': 'Welcome to FastAPI application', 'data': users}
	return data


@app.get('/user/{user_id}')
def get_user(user_id: int = Path(description='View user id details', gt=0, lt=4)):
	try:
		data = users[user_id]
		if data != None:
			return {'msg': 'success', 'data': users[user_id]}
		else:
			return {'msg': 'id not found'}

	except Exception as e:
		return {'msg': f'Error occurred: {e}'}	


# create retrive for user name
@app.get('/user_name')
def user_name(*, fname: Optional[str]=None, lname: Optional[str]=None, test: Optional[int]=None):
	for user_id in users:
		if users[user_id]['fname'] == fname or users[user_id]['lname'] == lname:
			return {'msg': 'success', 'data': users[user_id]}
	return {'msg': 'This user is not found'}



