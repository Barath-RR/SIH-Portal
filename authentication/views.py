from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from problem_statement_creator.models import ProblemStatementCreator
from .models import BaseUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import Error, IntegrityError
from .OTP import otp


@login_required
def logout_view(request):
    logout(request)
    return redirect("/")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("redirect")
    elif request.method == "POST":
        login_email = request.POST.get("login-email")
        login_password = request.POST.get("login-password")
        user = authenticate(request, email=login_email, password=login_password)
        if user is not None:
            login(request, user)
            if user.user_type == "PROBLEM_STATEMENT_CREATOR":
                return redirect("/psc_dashboard")
            elif user.user_type == "SUPERUSER":
                return redirect("/admin")
            else:
                return HttpResponse("Please contact admin.")
        else:
            messages.error(request, "Login Credentials Failed. Check your email and password.")
            return redirect("/login")
    else:
        content_parser = {'title': 'Login - Smart India Hackathon 2022'}
        return render(request, "login1.html", content_parser)


def register_as_problem_statement_creator(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email")
            password = request.POST.get("password")
            user_type = "PROBLEM_STATEMENT_CREATOR"
            ProblemStatementCreator.objects.create(
                name=request.POST.get("name"),
                email=email,
                organization=request.POST.get("org"),
                country=request.POST.get("country"),
                organization_type=request.POST.get("org_type"),
                state=request.POST.get("stt"),
                mobile=request.POST.get("mobile"),
                city=request.POST.get("city"),
                designation=request.POST.get("desig"),
                linked_in=request.POST.get("linkedin"),
                department=request.POST.get("dept"),
                nomination_letter=request.FILES.get("nomination"),
            )
            BaseUser.objects.create_user(email=email, password=password, user_type=user_type)
            messages.success(request, "Account Created Successfully.")
            return redirect('login')
        except IntegrityError as e:
            print(e)
            messages.error(request, "The email might have been used already. If you haven't registered with us, "
                                    "retry with the same email or try with a different email.")
        except Error:
            messages.error(request, "Something went wrong. Contact admin or try again later.")

    content_parser = {'title': 'Register - Smart India Hackathon 2022'}
    return render(request, "register_ps_creator1.html", content_parser)


@login_required(login_url="/login/")
def change_password(request):
    if request.method == "POST":
        u = BaseUser.objects.get(email__exact=request.user)
        if u.check_password(request.POST.get("current-password")):
            u.set_password(request.POST.get("new-password"))
            u.save()
            messages.success(request, "Password Changed.")
        else:
            messages.error(request, "Retype Current Password.")
    return render(request, "change_password.html")


@login_required(login_url='/login/')
def otp_validity(request):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        if otp.match_otp(entered_otp):
            try:
                user = ProblemStatementCreator.objects.get(email__exact=request.user.email)
                user.is_email_verified = True
                user.save()
            except Error:
                messages.error(request, "Something went wrong. Please try again later.")
                return redirect('login')
            messages.success(request, "Your email is successfully verified.")
            return redirect("redirect")
        else:
            messages.error(request, "Entered OTP is incorrect. Please retry.")
            return redirect("login")

    otp.send_otp(request.user)
    return render(request, "verify_email.html")
