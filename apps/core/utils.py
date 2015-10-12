from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q

from haystack.query import SearchQuerySet

from .models import Person, Log


class FormMessageMixin(object):

	message = 'Sucesso!'

	def form_valid(self, form):
		messages.info(self.request, self.message)
		return super(FormMessageMixin, self).form_valid(form)


class DeleteMessageMixin(object):

	message = 'Sucesso!'

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.message)
		return super(DeleteMessageMixin, self).delete(request, *args, **kwargs)


class DetailLogMixin(object):

	def get_context_data(self, **kwargs):
		context = super(DetailLogMixin, self).get_context_data(**kwargs)
		Log.objects.create(person=str(context['person']), action_type=3)
		return context


class NameListMixin(object):

	def get_context_data(self, **kwargs):
		context = super(NameListMixin, self).get_context_data(**kwargs)
		name_list = Person.objects.all().values_list('name')
		context['name_list'] = name_list
		return context


class PersonSearchMixin(object):

	def get_queryset(self):
		query = self.request.GET.get('query')
		
		if query is None or query == '':
			queryset = Person.objects.all()
		else:
			queryset = Person.objects.filter(
				Q(name__icontains=query) | Q(code__icontains=query)
			)

		return queryset


class LogSearchMixin(object):

	def get_queryset(self):
		query = self.request.GET.get('query')
		
		if query is None or query == '':
			queryset = Log.objects.all()
		else:
			queryset = Log.objects.filter(
				Q(person__icontains=query)
			)

		return queryset[:200]