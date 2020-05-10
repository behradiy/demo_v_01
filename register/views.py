from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.core.mail import send_mail
# rom django.contrib import settings


# views for sign in things
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            #
        # here , after registering, we will see the login page as we agreed on
        return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
