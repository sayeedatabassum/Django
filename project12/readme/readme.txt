pgrm 12 database connection

how to check django database connection:

    we can check whether configuration is done properly using command

    shell window /intractive mode

    command to open the shell/interactive console mode:

    python manage.py shell

    command to check the connection:

    >>from django.db import connection

    command to create cursor object:
    >>my_cursor = connection.cursor()

    command to exit from the shell/icm:
    quit()





run db
    python manage.py sqlmigrate dbapp 0001

    table apears

python manage.py migrate

python manage.py runserver

python manage.py createsuperuser
username
email
password

pytohn manage.py runserver

