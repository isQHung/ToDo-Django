from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='todos:login')
def index(request):
    return redirect('/todos')