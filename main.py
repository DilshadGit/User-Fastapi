from fastapi import FastAPI, Path


# named the api
app = FastAPI()

users = {
	1: {
		'id_num': 33,
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
		'date_of_birth': '22.03.1985'
	}
}


# This is first simple api to create it
@app.get('/')
def index():
	data = {'app': 'FastAPI', 'msg': 'Welcome to FastAPI application', 'data': users}
	return data


@app.get('/user/{user_id}')
def get_user(user_id: int = Path(description='View user id details', gt=0, lt=3)):
	try:
		data = users[user_id]
		if data != None:
			return {'msg': 'success', 'data': users[user_id]}
		else:
			return {'msg': 'id not found'}

	except Exception as e:
		return {'msg': f'Error occurred: {e}'}	