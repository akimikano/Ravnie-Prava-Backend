"Равные права" is a mobile application created for people with disabilities
Here is backend part of our application.

https://www.figma.com/file/r4iNHlMFicv8lZoToGJN9d/%D0%A0%D0%B0%D0%B2%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%B0%D0%B2%D0%B0?node-id=264%3A119
design of mobile application

http://127.0.0.1:8000/swagger/ - Documentation of endpoints

Instructions to launch backend:
by the way, you need python 3.7

1) create venv by command: python3.7 -m venv venv 

2) activate venv by command: source venv/bin/activate

3) install dependencies by command: pip install -r requirements.txt

4) create db by command: python manage.py migrate

5) launch project by command: python manage.py runserver

To come into admin page create admin by typing: python manage.py createsuperuser

than go to http://127.0.0.1:8000/admin/ and login

by the way, in last modification we added statistics 
