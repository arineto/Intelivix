from django.db import models
from django.core.urlresolvers import reverse


class Person(models.Model):

	code = models.IntegerField(verbose_name="Código")
	name = models.CharField(max_length=150, verbose_name="Nome")

	def __str__(self):
		return "%s (%d)" % (self.name, self.code)

	def get_absolute_url(self):
		return reverse(
			'core:person_list', args=[]
		)

	class Meta:
		verbose_name = 'Pessoa'
		verbose_name_plural = 'Pessoas'


class Log(models.Model):

	CREATE = 0
	UPDATE = 1
	DELETE = 2
	DETAIL = 3

	ACTION_TYPE = (
			(CREATE, 'Create'),
			(UPDATE, 'Update'),
			(DELETE, 'Delete'),
			(DETAIL, 'Detail'),
		)

	# Decided to use a String instead of a Foreign Key to Person because if we use the Foreign Key the data will be lost once the instace is deleted
	person = models.CharField(max_length=100, verbose_name='Pessoa')
	action_type = models.IntegerField(choices=ACTION_TYPE, verbose_name='Tipo da Ação')
	date = models.DateTimeField(auto_now_add=True, verbose_name='Data')

	def __str__(self):
		return "%s %s - %s" % (self.get_action_type_display(), self.person, self.date.strftime('%d/%m/%Y %H:%M'))