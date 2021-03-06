"""Views for task manager."""
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic


class IndexView(generic.TemplateView):
    """Define view for index page."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Define the title."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager')
        return context


class LoginUserView(SuccessMessageMixin, LoginView):
    """Define view for login page."""

    form_class = AuthenticationForm
    template_name = 'form.html'
    success_message = _("You're logged in")

    def get_success_url(self):
        """Change redirect url."""
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Login')
        context['button'] = _('Login user')
        return context


class LogoutUserView(SuccessMessageMixin, LogoutView):
    """Define view for logout."""

    next_page = 'index'

    def dispatch(self, request, *args, **kwargs):
        """Log out and show a logout message."""
        messages.add_message(request, messages.INFO, _("You're logged out."))
        return super().dispatch(request, *args, **kwargs)
