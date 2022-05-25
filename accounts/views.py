# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# Authentication views from https://docs.djangoproject.com/en/4.0/topics/auth/default/#module-django.contrib.auth.views
# And: https://github.com/django/django/blob/b9cf764be62e77b4777b3a75ec256f6209a57671/django/contrib/auth/urls.py
# accounts/login/ [name="login"]
# accounts/logout/ [name="logout"]
# accounts/password_change/ [name="password_change"]
# accounts/password_change/done/ [name="password_change_done"]
# accounts/password_reset/ [name="password_reset"]
# accounts/password_reset/done/ [name="password_reset_done"]
# accounts/reset/<uidb64>/<token>/ [name="password_reset_confirm"]
# accounts/reset/done/ [name="password_reset_complete"]
