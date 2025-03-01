from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, UpdateView

# Create your views here.

User = get_user_model()


class HomePage(TemplateView):
    template_name = "users/home.html"


class MentorView(TemplateView):
    template_name = "users/mentors.html"


@method_decorator(login_required, name="dispatch")
class UpdateProfileView(UpdateView, SuccessMessageMixin):
    model = User
    template_name = "users/update_profile.html"
    fields = ["first_name", "last_name", "email", "phone", "address", "dp"]
    success_url = "/users/home/"
    success_message = "Your Profile Updated Successfully!"

    def get_object(self, **kwargs):
        return self.request.user
