from django.shortcuts import render

# Create your views here.
def home(request, supplier_id):
    return render(request, 'panel/calendar.html', {})

