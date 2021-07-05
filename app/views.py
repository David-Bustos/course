from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from .models import *

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):

    if request.method == "POST":

        errors = Course.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)

            return redirect('/')

        else:
            Course.objects.create(
            name = request.POST['name'],
            date = request.POST['date'],
            desc = request.POST['desc'])

            messages.success(request, 'Course created!')

            return redirect('/')
    else:
        return HttpResponse('Invalid Method')

def delete(request, number):

    # messages.success(request, 'Show deleted!')

    c = Course.objects.get(id=number)
    c.delete()

    # return JsonResponse({'resultado': True})
    return redirect('/')

