from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.db.models.signals import post_delete


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
		ordering = ['name']


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

	class Meta:
		verbose_name = 'Log'
		verbose_name_plural = 'Logs'
		ordering = ['-date']



def register_save_log(sender, instance, created, **kwargs):
	if created:
		action_type = 0
	else:
		action_type = 1
	Log.objects.create(person=str(instance), action_type=action_type)


def register_delete_log(sender, instance, **kwargs):
	Log.objects.create(person=str(instance), action_type=2)


post_save.connect(register_save_log, sender=Person, dispatch_uid="apps.core.models.register_save_log")
post_delete.connect(register_delete_log, sender=Person, dispatch_uid="apps.core.models.register_delete_log")