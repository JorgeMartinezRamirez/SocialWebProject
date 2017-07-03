from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequieredMixin,
                                        PermissionRequieredMixin)
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.
class CreateGroup(LoginRequieredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
