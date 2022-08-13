from django.http import HttpResponse
from django.shortcuts import render, redirect
from authentication.models import BaseUser


# Create your views here.
def index(request):
    return render(request, "landing.html")


def redirect_location(request):
    if request.user.is_authenticated:
        user = BaseUser.objects.get(email=request.user)
        if user.user_type == "SUPERUSER":
            return redirect("admin:index")
        elif user.user_type == "PROBLEM_STATEMENT_CREATOR":
            return redirect("psc-dashboard")
        else:
            return HttpResponse("Please Contact Admin.")
    else:
        return redirect(request, "login")


def process_flow(request):
    return render(request, "process_flow.html")
