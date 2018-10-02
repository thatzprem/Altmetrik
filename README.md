# Altmetrik

An Article content creation application.

How ​to ​setup ​and ​install ​anything ​needed ​for ​testing ​the ​project, ​e.g. ​db ​schema ​scripts?

The project configured to use SQLite
You may have to use pip install mysqlclient incase not done before.
You may run the requirements.txt file or refer the same for the additional packages to be installed.
How ​to ​run ​the ​project?

Once you have installed the dependent packages from requirements.txt.
move to team_management folder inside the project
Do python manage.py makemigrations
Do python manage.py migrate
use python manage.py runserver to the run the project locally on your system.
How ​to ​test ​the ​project, ​ideally ​with ​example ​CURL ​commands ​that ​exercise ​the ​various rest ​endpoints?

I have used postman tool to test the API's
You may directly use this URL (http://127.0.0.1:8000/article/) to do CRUD operations on the Member table.
A detailed API documentation for the app is available on this postman URL https://documenter.getpostman.com/view/43395/RWgm3g5X

Create Member: curl --request GET 
--url http://127.0.0.1:8000/article

Update Member: curl --request PATCH 
--url http://127.0.0.1:8000/article/2/ 
--header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' 
--form first_name=New

Get Members: curl --request GET 
--url http://127.0.0.1:8000/article

Delete Member: curl --request DELETE 
--url http://127.0.0.1:8000/article/1 
--header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' 
--form first_name=New
