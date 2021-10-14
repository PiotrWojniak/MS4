from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """A view to render the contact page"""

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            """Send the user a confirmation email"""

            contact_form.save()
            instance = contact_form.save()

            sender_email = instance.email
            subject = render_to_string(
                'contact/confirmation_emails/subject_contact_email.txt',
                {'instance': instance})
            body = render_to_string(
                'contact/confirmation_emails/body_contact_email.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body, settings.DEFAULT_FROM_EMAIL,
                [sender_email]
            )
            messages.info(request, 'Your message was submitted successfully. \
                We will be in touch soon')
            return redirect(reverse('products'))
        else:
            messages.error(
                request,
                'There was a problem with the form. \
                Please resubmit')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'on_contact_page': True
    }
    template = 'contact/contact.html'
    return render(request, template, context)
