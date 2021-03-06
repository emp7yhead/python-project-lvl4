"""Mixins for Task Manager."""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class UserCheckMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Check user id."""

    def test_func(self):
        """Check id."""
        return self.kwargs['pk'] == self.request.user.id

    def handle_no_permission(self):
        """Handle errors."""
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                _("You don't have permission to change another user."),
            )
        else:
            self.success_url = ('login')
            messages.warning(
                self.request,
                _("You're not authorized. Please login."),
            )
        return redirect(self.success_url)
