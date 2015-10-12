import json

from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

from .models import Person, Log
from .forms import PersonForm
from .utils import FormMessageMixin, DeleteMessageMixin, DetailLogMixin, NameListMixin


class PersonListView(NameListMixin, ListView):

	model = Person
	context_object_name = 'person_list'
	template_name = 'core/person_list.html'
	paginate_by = 100


class PersonCreateView(FormMessageMixin, CreateView):
	
	model = Person
	form_class = PersonForm
	template_name = 'core/form.html'
	message = 'Pessoa criada com sucesso!'


class PersonDetailView(DetailLogMixin, DetailView):

	model = Person
	context_object_name = 'person'
	template_name = 'core/person_detail.html'


class PersonUpdateView(FormMessageMixin, UpdateView):
	
	model = Person
	form_class = PersonForm
	template_name = 'core/form.html'
	message = 'Pessoa atualizada com sucesso!'


class PersonDeleteView(DeleteMessageMixin, DeleteView):

	model = Person
	context_object_name = 'person'
	success_url = reverse_lazy('core:person_list')
	template_name = 'core/delete_form.html'
	message = 'Pessoa deletada com sucesso!'


class LogListView(ListView):

	model = Log
	queryset = Log.objects.all()[:200]
	context_object_name = 'log_list'
	template_name = 'log_list'
	paginate_by = 50
