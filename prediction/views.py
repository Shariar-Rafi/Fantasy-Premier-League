
import random
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import random

from django.shortcuts import render
import random

def generate_prediction(request):
    prediction = None

    if request.method == 'POST':
        input_string = request.POST.get('input_string')
        if input_string:
            # You can use the input_string to calculate a random percentage
            prediction = random.uniform(1, 10)

    return render(request, 'prediction_page.html', {'prediction': prediction})

