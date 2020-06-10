from django.contrib.auth.views import LoginView as LoginViewBase

class LoginView(LoginViewBase):
    template_name = 'registration/login.html'