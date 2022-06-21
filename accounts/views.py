import re
from django.shortcuts import render
from .models import Accounts
# Create your views here.
def accounts_index_view(request):
  accounts = Accounts.objects.all()
  context = {
    "accounts": accounts
  }
  return render(request, "accounts/index.html", context)
  