from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from . import models
import base64


def home(request):
    return render(request, "home.html")


def register(request):
    if request.session.has_key("username"):
        return redirect("profile")
    if request.POST:
        subs = models.SubscriberForm(request.POST)
        if subs.errors:
            return render(request, "register.html", {"errors": subs.errors})
        try:
            user = subs.save()
        except IntegrityError:
            return render(request, "register.html", {"errors": "User with that name already exists."})
        request.session["username"] = user.username
        return redirect("profile")
    return render(request, "register.html")


def profile(request):
    if not request.session.has_key("username"):
        return redirect("register")

    user = get_object_or_404(models.Subscriber, username=request.session["username"])

    return render(
        request,
        "profile.html",
        {"invoices":
            [
                {
                    "url": base64.urlsafe_b64encode((user.username + "-" + user.signup_date.isoformat()).encode()).decode(),
                    "display_name": user.signup_date.isoformat()
                }
            ]
        }
    )
