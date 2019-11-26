from .forms import UserRegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class RegisterView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'
    success_message = 'Account created successfully!'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        return super().form_valid(form)