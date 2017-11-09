# creates an env if env does not exist
if ! [ -d "./env" ]
then
	echo creating env
	virtualenv env
else
	echo env exists
fi

# fires up virtual env
source env/bin/activate
echo -\x1B "venv activated \x1B[42mDone\x1B[0m"
echo -------------------------------------------

# installs dependencies to the virtual environment
pip install -r requirements.txt
echo -\x1B "requirements installed \x1B[42mDone\x1B[0m"
echo -------------------------------------------

# builds docker containers using Dockerfiles
docker-compose up -d --build
echo -\x1B "docker-compose build successful \x1B[42mDone\x1B[0m"
echo -------------------------------------------

# runs docker containers and runs command to recreate db
# comment out recreate_db to avoid recreating db
docker-compose run blog python manage.py recreate_db
echo -\x1B "docker-compose run successful. DB recreated \x1B[42mDone\x1B[0m"
echo -------------------------------------------