import re
from django.shortcuts import render
from .models import Accounts
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
def accounts_index_view(request):
  accounts = Accounts.objects.all()
  context = {
    "accounts": accounts
  }
  return render(request, "accounts/index.html", context)

class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'