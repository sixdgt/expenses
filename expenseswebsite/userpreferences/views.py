from django.shortcuts import render, redirect
from django.views import View
import os
import json
from django.conf import settings
from .models import UserPreference
from django.contrib import messages

# Create your views here.
class PreferenceView(View):
    def get(self, request):
        exists = UserPreference.objects.filter(user=request.user).exists()
        user_preference = None

        if exists:
            user_preference = UserPreference.objects.get(user=request.user)
        currency_data = []
        
        file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
        # import pdb
        # pdb.set_trace()
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            for k,v in data.items():
                currency_data.append({'name': k, 'value': v})

        return render(request, "preferences/index.html", {"currencies":currency_data, "user_preference": user_preference})

    def post(self, request):
        currency = request.POST.get('currency')
        exists = UserPreference.objects.filter(user=request.user).exists()

        if exists:
            user_preference = UserPreference.objects.get(user=request.user)
            user_preference.currency = currency
            user_preference.save()
        else:
            UserPreference.objects.create(user=request.user, currency=currency)
        messages.success(request, "Changes saved")
        return redirect("preferences")
