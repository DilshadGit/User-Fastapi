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
We add another function where the user can search for both fname and lname as query parameters as an admin, but
as not admin in the front can get or find the user with the fname, the lname and test not able to find or get in front.

# Combining path and query parameters
This is exactly like Query parameter only add another new parameter say like user_id again as an examples or lname
The most important notice here we have set the user_name/{fname} as requested parameter and use Optional in front of str but
in the docs page display required

# Request body description and post method 
Admin or Developer can create a new user using post method with a new user_id if not exists will ask the body request like other 
field in the new class created but this is only to create in docs page this new user not saved in the database because our
application has not been connect to the database now when we refresh the page the new user will disapred. Also there is no body field for the new user only request as json application.

# Create update user using put method
In the update methods need new class to be able all fields put in Optional for update not as required because sometimes may need 
one field or two not all, so we have to create new class to give option for other fields to be optional.
Notice: there is internal error server not very clear because no database at the moment but if create cookie maye resolve it.


# Delete User using delete method
Selecet user_id and use del method to delete user throw user_id