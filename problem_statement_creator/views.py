from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from authentication.models import BaseUser
from .models import NodalOfficerNomination, ProblemStatementCreator
from problem_statements.models import ProblemStatementSubmitted
from django.views.generic import UpdateView, DeleteView
from django.db import IntegrityError, Error
from django.contrib import messages


@login_required(login_url='/login/')
def dashboard(request):
    objects = ProblemStatementSubmitted.objects.all().filter(submitted_by__email=request.user)
    users = ProblemStatementCreator.objects.get(email=request.user)
    try:
        post = NodalOfficerNomination.objects.get(submitted_by__email=request.user.email)
    except NodalOfficerNomination.DoesNotExist:
        post = None
    context = {
        "submitted_problem_statements": objects.count(),
        "approved_problem_statements": objects.filter(is_approved=True).count(),
        "rejected_problem_statements": objects.filter(is_rejected=True).count(),
        "user": users,
        "nodal": post,
        "title": "SMART INDIA HACKATHON 2022",
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='/login/')
def problem_statement_creation(request):
    user1 = ProblemStatementCreator.objects.get(email=request.user.email)
    if user1.is_approved:
        if request.method == 'POST':
            try:
                ProblemStatementSubmitted.objects.create(
                    title=request.POST.get('title'),
                    description=request.POST.get('des'),
                    dataset_file=request.FILES.get('datafile'),
                    youtube_link=request.POST.get('ytlink'),
                    category=request.POST.get('cat'),
                    domain_bucket=request.POST.get('dombuck'),
                    technology=request.POST.get('tech'),
                    submitted_by=ProblemStatementCreator.objects.get(email=request.user)
                )
            except IntegrityError as e:
                messages.error(request, "The title of the problem statement already exists. Check your 'View Problem "
                                        "Statement Section' and update from there or try a different title.")
            except Error:
                messages.error(request, "Something went wrong. Contact admin or try again later.")

        return render(request, 'dashboard_createProblemStatement.html', {'title': "CREATE PROBLEM STATEMENT"})
    else:
        context = {
            'prob_stats': ProblemStatementSubmitted.objects.all().filter(submitted_by__email=request.user),
            'title': "CREATE PROBLEM STATEMENT"
        }
        return render(request, 'problemstatementcreator_view_altr.html', context)


@login_required(login_url='/login/')
def view_problem_statement(request):
    user1 = ProblemStatementCreator.objects.get(email=request.user.email)
    if user1.is_approved:
        context = {
            'prob_stats': ProblemStatementSubmitted.objects.all().filter(submitted_by__email=request.user),
            'title': "VIEW PROBLEM STATEMENT"
        }
        return render(request, 'dashboard_viewProblemStatement.html', context)
    else:
        context = {
            'prob_stats': ProblemStatementSubmitted.objects.all().filter(submitted_by__email=request.user),
            'title': "VIEW PROBLEM STATEMENT"
        }
    return render(request, 'problemstatementcreator_view_altr.html', context)


class PostDeleteView(DeleteView):
    model = ProblemStatementSubmitted
    template_name = "problemstatementsubmissions_confirm_delete.html"
    success_url = '/view_prob_stat'


class PostUpdateView(UpdateView):
    model = ProblemStatementSubmitted
    template_name = "problemstatementsubmissions_update_form.html"
    fields = ['title', 'description', 'dataset_file', 'youtube_link', 'category', 'domain_bucket', 'technology']
    success_url = '/view_prob_stat'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required(login_url='/login/')
def nodal_officer_add(request):
    if request.method == 'POST':
        try:
            if NodalOfficerNomination.objects.filter(submitted_by__email=request.user.email).first():
                post = NodalOfficerNomination.objects.get(submitted_by__email=request.user.email)
            else:
                post = NodalOfficerNomination()

            post.email = request.POST.get('email')
            post.name = request.POST.get('name')
            post.organization = request.POST.get('org')
            post.organization_type = request.POST.get('org_type')
            post.country = request.POST.get('country')
            post.state = request.POST.get('stt')
            post.mobile = request.POST.get('mobile')
            post.city = request.POST.get('city')
            post.designation = request.POST.get('desig')
            post.linked_in = request.POST.get('linkedin')
            post.department = request.POST.get('dept')
            post.submitted_by = ProblemStatementCreator.objects.get(email=request.user)
            post.save()
            messages.success(request, "Successfully Added Nodal Officer Details.")
        except Error as e:
            messages.error(request, "An error as occurred. Please try again.")
            print(e)
    try:
        nodal_officer = NodalOfficerNomination.objects.get(submitted_by__email=request.user.email)
    except NodalOfficerNomination.DoesNotExist:
        nodal_officer = None
    context = {
        "nodal_officer": nodal_officer,
        "title": "NODAL OFFICER NOMINATION"
    }
    return render(request, 'dashboard_nodal_officer.html', context)


@login_required(login_url='/login/')
def my_profile_view(request):
    if request.method == "POST":
        post = ProblemStatementCreator.objects.get(email=request.user)
        post.name = request.POST.get('name')
        post.organization = request.POST.get('org')
        post.organization_type = request.POST.get('org_type')
        post.country = request.POST.get('country')
        post.state = request.POST.get('stt')
        post.mobile = request.POST.get('mobile')
        post.city = request.POST.get('city')
        post.designation = request.POST.get('desig')
        post.linked_in = request.POST.get('linkedin')
        post.department = request.POST.get('dept')
        post.save()

    user_data = ProblemStatementCreator.objects.get(email=request.user)
    context = {
        "user_data": user_data,
        'title': "MY PROFILE"
    }

    return render(request, "dashboard_myprofile.html", context)

# @login_required(login_url='/login/')
# def problem_update(request):
#     if request.method == "POST":
#         post=ProblemStatementSubmitted.objects.get(email=request.get.user) 
#         post.title = request.POST.get('title'),
#         post.description = request.POST.get('des'),
#         post.dataset_file = request.FILES.get('datafile'),
#         post.youtube_link = request.POST.get('ytlink'),
#         post.category = request.POST.get('cat'),
#         post.domain_bucket = request.POST.get('dombuck'),
#         post.technology = request.POST.get('tech'),
#         post.submitted_by = ProblemStatementSubmitted.objects.get(email=request.user)
#         post.save()

#     post_data = ProblemStatementSubmitted.objects.get(submitted_by__email=request.user)
#     context = {
#         "post_data": post_data
#     }

#     return render(request, "problem_statement_creator/problemstatementsubmissions_update_form.html", context)
