#!/bin/bash

while true; do

  cd web/

	if [[ ! -d "/migrations/" ]]; then
   		echo "Not Exist"
      echo "FUCK YOU!!!"
      echo "$(ls)"
      echo  env
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

ls 

exec gunicorn -w 4 -b 0.0.0.0:5000 --access-logfile - --error-logfile - run_app:app