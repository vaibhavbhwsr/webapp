from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView

from .forms import RegistrationForm, MyLoginForm

User = get_user_model()

# Create your views here.


class IndexView(TemplateView):
    template_name = "core/index.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class MySignupView(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = "core/signup.html/"
    success_url = "/"
    success_message = (
        "%(username)s was created successfully! Now Login with"
        " the same username and password!"
    )

    def test_func(self):
        """
        This is necessary function to use with UserPassesTextMixin
        """
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        """
        This function stop accessing signup page to logged in user
        """
        return HttpResponseRedirect(reverse("users:home"))


class MyLoginView(SuccessMessageMixin, LoginView):
    """
    Here it stops logged in user to access log in page.
    And add success message
    """

    form_class = MyLoginForm
    template_name = "core/login.html"
    redirect_authenticated_user = True
    success_message = "%(username)s, Welcome Here!"
