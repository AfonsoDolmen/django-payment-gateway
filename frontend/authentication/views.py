from django.views.generic import FormView, RedirectView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from authentication.forms import LoginForm, RegisterForm


class AuthLoginView(FormView):
    """
    View de login
    """
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Autentica o usuário
        """
        email = form.cleaned_data.get('email', '')
        password = form.cleaned_data.get('password', '')

        # Verifica se há usuário
        try:
            user = User.objects.get(username=email)
            username = user.username
        except User.DoesNotExist:
            raise form.ValidationError('Usuário não encontrado.')

        user = authenticate(self.request, username=username, password=password)

        # Verifica as credenciais
        if user is None:
            raise form.ValidationError('Password Incorrect.')

        # Autentica o usuário
        login(self.request, user)

        return super().form_valid(form)


class AuthRegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Cria um novo usuário
        """
        email = form.cleaned_data.get('email', '')
        password = form.cleaned_data.get('password', '')

        # Cria uma nova instância do usuário
        new_user = User.objects.create(
            username=email,
        )

        # Criptografa a senha do usuário
        new_user.set_password(password)

        # Salva o usuário no banco
        new_user.save()

        return super().form_valid(form)


class AuthLogoutView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        """
        Realiza logout do usuário
        """
        logout(request)

        return super().get(request, *args, **kwargs)
