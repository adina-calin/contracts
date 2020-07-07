# contracts
django-apl-contracte
Aplicatie de contracte pentru proiectul de la cursul de Python

Local setup
System requirements
Please have Docker and docker-compose (bundled with Docker for Mac/Windows) installed

Initial setup
This is a first-time setup step.

On the first run of the application we need to run the migrations to populate the database structure.

docker-compose run console django-admin migrate
As the other containers are missing they will be built/downloaded prior to running the command.

So this basically also calls docker-compose pull and docker-compose build prior to building.

Startup the project
docker-compose up
Go to http://localhost:8080 to view the newly created Django application
