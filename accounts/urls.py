from django.urls import path
from .views import SignUpView, accounts_index_view

urlpatterns = [
  path('index/', accounts_index_view, name='accounts_index'),
  path('signup/', SignUpView.as_view(), name='signup')
]