from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Person, Log
from .forms import PersonForm
from .utils import MessageMixin


class PersonListView(ListView):
	# fazer mixin para adicionar uma lista como os nomes já existentes para ao autocomplete
	model = Person
	context_object_name = 'person_list'
	template_name = 'person_list'


class PersonCreateView(MessageMixin, CreateView):
	
	form_class = PersonForm
	template_name = 'core/form.html'
	message = 'Pessoa criada com sucesso!'


class LogListView(ListView):
	# fazer mixin para adicionar uma lista como os nomes já existentes para ao autocomplete
	model = Log
	context_object_name = 'log_list'
	template_name = 'log_list'
