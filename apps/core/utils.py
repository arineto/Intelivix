from django.contrib import messages

from .models import Log

class MessageMixin(object):

	message = 'Sucesso!'

	def form_valid(self, form):
		messages.info(self.request, self.message)
		return super(MessageMixin, self).form_valid(form)


class FormLogMixin(object):

	action_type = 0

	def form_valid(self, form):
		person = "%s (%d)" % (form.cleaned_data['name'], form.cleaned_data['code'])
		Log.objects.create(action_type=self.action_type, person=person)
		return super(FormLogMixin, self).form_valid(form)