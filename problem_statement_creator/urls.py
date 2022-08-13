from django.urls import path
from django.views.generic.edit import UpdateView
from .views import PostDeleteView, PostUpdateView,nodal_officer_add, view_problem_statement, dashboard,problem_statement_creation, my_profile_view

url_patters = [
    path('psc_dashboard/', dashboard, name='psc-dashboard'),
    path('problem_statement_creation/', problem_statement_creation, name='addps'),
    path('nodal_officer/', nodal_officer_add, name='nodal'),
    path('view_prob_stat/', view_problem_statement, name='viewps'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='ps-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='ps-update'),
    path('my_profile/', my_profile_view, name="my-profile"),
]
