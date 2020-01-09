from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from .forms import FeedBackForm
from service_center import settings

GOOD = 85
FAILURE = 80

class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, GOOD, 'success')
        else:
            messages.add_message(request, FAILURE, 'failure')
        return redirect("/contacts")