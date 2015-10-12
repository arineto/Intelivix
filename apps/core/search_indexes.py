from haystack import indexes

from .models import Person, Log


class PersonIndex(indexes.SearchIndex, indexes.Indexable):

	text = indexes.CharField(document=True, use_template=True)
	code = indexes.IntegerField(model_attr='code')
	name = indexes.CharField(model_attr='name')

	def get_model(self):
		return Person


class LogIndex(indexes.SearchIndex, indexes.Indexable):

	text = indexes.CharField(document=True, use_template=True)
	person = indexes.CharField(model_attr='person')
	action_type = indexes.CharField(model_attr='action_type')
	date = indexes.DateTimeField(model_attr='date')

	def get_model(self):
		return Log