## Create virtual env
python3 -m venv venv

## Activate virtual env
source ~/venv/bin/activate

## Clone project 
git clone https://github.com/gmeda-dev/Application-reservations-test.git

## Install requirements
pip install -r requirements.txt

## Run migrations
./manage.py migrate

## To run tests
./manage.py test
