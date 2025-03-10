# mkvirtualenv fenv

# pip install fastapi
	annotated-types==0.7.0
	anyio==4.8.0
	fastapi==0.115.11
	idna==3.10
	pydantic==2.10.6
	pydantic_core==2.27.2
	sniffio==1.3.1
	starlette==0.46.1
	typing_extensions==4.12.2

# We install uvicorn to run the server of fastapi
# pip install uvicorn
	uvicorn==0.34.0
	click==8.1.8
	h11==0.14.0

# To make it run: uvicorn main:app --reload
# http://127.0.0.1:8000

## Create CRUD:
GET - GET An Information fron user
POST - CREATE new file
PUT - Update file
DELETE - Delete the file
###############################

# Check fastAPI admin for more details run:
http://127.0.0.1:8000/docs 

# To find out first details about click on (Try it out) and (Excute):
	output: http://127.0.0.1:8000/docs#/default/index__get

# Path Parameters:
DEFAULT PAGE: http://127.0.0.1:8000
USER PAGE: http://127.0.0.1:8000/user/1
DEV PAGE: http://127.0.0.1:8000/docs#/default/get_user_user__user_id__get

# add to import Path
## This is give more options to the user for viewing it: 
- add path to the get function but without Path(None) only description

### gt = greater than >
### lt = less than <
### ge = greater than or equal to >= 
### le = less than or equal to <=

# Query Parameters
We add another function where the user can search for both fname and lname as query parameters,
also adding optional to give user extra option to enter id number also optional not required
