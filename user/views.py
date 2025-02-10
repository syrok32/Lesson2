from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from user.forms import UserRegisterForm


class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Привет'
        message = 'Привет, спасибо что зашел'
        from_email = 'stepstepan2@gmail.com'
        recipient_list = [user_email]
        from django.core.mail import send_mail
        send_mail(subject, message, from_email, recipient_list)
