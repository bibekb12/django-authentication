from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

"""index"""


def index(request):
    return render(request, "index.html", {"title": "indextitle"})


"""register here"""


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            """mailing system"""
            htmly = get_template("email.html")
            d = {"username": username}
            subject, from_email, to = "welcome", "bibek@bibek.edu.np", email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            """registraion continue here"""
            messages.success(request, "User created successfully")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form, "title": "register here"})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password. view ma ho")
        else:
            messages.error(request, "else ko error in view")
    form = AuthenticationForm()
    return render(
        request, "login.html", {"form": form, "title": "log in here view bata"}
    )
