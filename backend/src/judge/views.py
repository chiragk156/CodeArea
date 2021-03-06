from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from .index import judge_main
from .contest import judge_main_contest
from django.contrib.auth.decorators import login_required

from .normal import judge_main_normal

@login_required
def run_judge(request):
    return judge_main(request)

@login_required
def run_judge_contest(request):
    return judge_main_contest(request)

def run_judge_normal(request):
    return judge_main_normal(request)
