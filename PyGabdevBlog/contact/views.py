from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

from .forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            send_mail(subject=subject, message=f"{message} \n de {email}", from_email=email,
                      recipient_list=["gabrieltrouve5@gmail.com", email])
            messages.add_message(request, messages.INFO,
                                 "Email envoyé, je réponds très vite :) Vous avez reçu une copie de l'email.")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", context={"form": form})
