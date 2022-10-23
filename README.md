# API-end-points-creation-using-FASTAPI

we can use this below format to run the fast api usng uvicorn server

`uvicorn <file_name>:<app_name> --reload`

eg. 

uvicorn main:app --reload

here
- uvicorn :- is server
- main : filename
- app : app name

**Note:** file name and app name can be anything

which the above command does not work use this pattern 

` python -m uvicorn <file_name>:<app_name> --reload `

eg:

python -m uvicorn main:app --reload
