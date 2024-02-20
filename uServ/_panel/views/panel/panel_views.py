from django.shortcuts import render
from _utils.decorator import auth_supplier_required

# Create your views here.
@auth_supplier_required
def home(request, supplier_id):
    return render(request, 'panel/calendar.html', {})

