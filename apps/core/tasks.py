from __future__ import absolute_import

import requests
import random

from celery.decorators import task, periodic_task
from celery.task.schedules import crontab

from .models import Person


@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def generatePeople():

	for i in range(0,10):
		generatePerson.delay()


@task()
def generatePerson():

	name = getName()
	code = random.randint(0,999999999)
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


@task()
def teste():
	print('aee')