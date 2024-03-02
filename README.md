# python version 3.8+
# commands for install or setup


# create virtualenv
python3 -m venv env

# clone repository
git clone https://github.com/Diman2003/homble-assessment.git

# install requirements package
pip install -r requirements.txt

# run migration
python3 manage.py makemigrations
python3 manage.py migrate

# run project
python3 manage.py runserver




# additional als add  admin_honeypot for admin panel security
# url - http://localhost/admin1/      you change this accordingly
