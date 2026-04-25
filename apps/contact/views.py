from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()  # ✅ Save to DB

            # 📩 Send Email to YOU
            subject = f"New Contact Message: {contact.subject or 'No Subject'}"

            message = f"""
You received a new message:

Name: {contact.name}
Email: {contact.email}
Phone: {contact.phone or 'N/A'}

Message:
{contact.message}
"""

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,   # from email
                [settings.EMAIL_HOST_USER],  # to your email
                fail_silently=False,
            )

            # 📩 Auto reply to user (optional but recommended)
            send_mail(
                "Thanks for contacting Kashvi Tech 🚀",
                "We received your message. Our team will contact you soon.",
                settings.EMAIL_HOST_USER,
                [contact.email],
                fail_silently=True,
            )

            messages.success(request, "Message sent successfully ✅")

            # ✅ FIXED redirect (namespace)
            return redirect('contact:contact')

        else:
            messages.error(request, "Please fix the errors below ❌")

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form
    })