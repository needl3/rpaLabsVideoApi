#!/usr/bin/bash
RED=$'\e[31m'
GREEN=$'\e[32m'
ENDCOLOR=$'\e[0m'
YELLOW=$'\e[33m'

if ! which pip &> /dev/null;
then
    echo "${RED}[X] Pip not installed. ${YELLOW}Refer: https://pip.pypa.io/en/stable/installation/${ENDCOLOR}"
    exit 1
elif ! which virtualenv &> /dev/null;
then
    echo "${RED}[X] virtualenv not installed. Install from your package manager${ENDCOLOR}"
    exit 1
fi

echo "${GREEN}[-] Initializing virtualenv${ENDCOLOR}"
virtualenv venv
. venv/bin/activate

echo "${GREEN}[-] Installing packages${ENDCOLOR}"
pip install -r requirements.txt

echo "${GREEN}[-] Creating a environment file${ENDCOLOR}"
echo "APP_SECRET=thisisadummyappsecretbutalongone" > videoApp/.env

echo "${GREEN}[-] Making migrations${ENDCOLOR}"
python manage.py makemigrations
python manage.py migrate

echo "${GREEN}[-] Done! You can now start the server with ${YELLOW}python manage.py runserver${ENDCOLOR}"