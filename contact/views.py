from django.shortcuts import render

from .models import contact_message

from django.contrib import messages
# Create your views here.

from django.core.mail import send_mail
from django.core.mail import EmailMessage


def contact(request):
    """ A view to return the contact page """

    return render(request, 'contact/contact.html')


def contact_form_post(request):

    template = 'contact/contact.html'

    if request.method == 'POST':

        message_name = request.POST['full_name']
        message_email = request.POST['email']
        message_message = request.POST['message']

        # Send an email

        send_mail(
            'The Veggie Fitness contact form',
            message_message,
            message_email,
            ['antony_thornton_p@outlook.com'],
            )

        email = EmailMessage('Test', 'Test', to=['antony_thornton_p@outlook.com'])
        email.send()

        messages.success(request, f'Thank you {message_name} for your message. We \
                         will get back to you as soon \
                         as possible via {message_email}.')
        return render(request, template, {})
        #  return render(request, template, {'message_name': message_name, }) 
        #  If you were to stay on the contact page.

    else:
        #    messages.error(request, "Not working.")

        return render(request, template, {})