from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

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
