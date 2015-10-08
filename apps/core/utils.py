from django.contrib import messages

from .models import Log

class MessageMixin(object):

	message = 'Sucesso!'

	def form_valid(self, form):
		messages.info(self.request, self.message)
		return super(MessageMixin, self).form_valid(form)
