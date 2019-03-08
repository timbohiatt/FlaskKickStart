#!/bin/bash

while true; do

	if [[ ! -d "/migrations/" ]]; then
   		echo "Not Exist"
   		flask db init
   		flask db migrate
	fi

    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    sleep 5
done

exec gunicorn -w 4 -b 0.0.0.0:5000 --access-logfile - --error-logfile - run_app:app