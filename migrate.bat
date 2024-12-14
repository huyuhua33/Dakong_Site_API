@echo off
python ./DakongSite/manage.py makemigrations
python ./DakongSite/manage.py migrate
pause