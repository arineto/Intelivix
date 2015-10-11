import requests

from random import randint

from .models import Person


def generatePeople():

	for i in range(0,1000):
		generatePerson()


def generatePerson():

	name = getName()
	code = randint(0,999999999)
	person = Person.objects.create(code=code, name=name)
	
	return person


def getName():

	data = requests.get('https://randomuser.me/api/')
	user = data.json()['results'][0]['user']
	name = "{0} {1}".format(
		user['name']['first'].capitalize(),
		user['name']['last'].capitalize()
	)

	return name