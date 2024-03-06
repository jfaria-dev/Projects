from django.http import HttpResponse
from django.shortcuts import render, redirect
from _panel.models import Service, Worker
from _web.models import SupplierDetails, Supplier, UserCart
from _web.forms.user.user_cart_form import UserCartForm
from datetime import datetime, timedelta, time
import calendar
from calendar import HTMLCalendar

# ------------------- LIST OF DAYS OF WEEK -------------------
DAYS_OF_WEEK = {'Seg': 'Segunda', 
                'Ter': 'Terça', 
                'Qua': 'Quarta', 
                'Qui': 'Quinta', 
                'Sex': 'Sexta', 
                'Sáb': 'Sábado', 
                'Dom': 'Domingo' }

DAYS_OF_WEEK_COMPLETE = {'Segunda': 'Segunda', 
                         'Terça': 'Terça', 
                        'Quarta': 'Quarta', 
                        'Quinta': 'Quinta', 
                        'Sexta': 'Sexta', 
                        'Sábado': 'Sábado', 
                        'Domingo': 'Domingo' }

# ------------------- AJAX -------------------
def availability_by_worker(request):
    worker_id = request.GET.get('worker_id')
    supplier_id = request.GET.get('supplier_id')
    day_of_week = request.GET.get('day_of_week')
    day = request.GET.get('day')
    month = request.GET.get('month')    
    dayOfWeek = DAYS_OF_WEEK_COMPLETE.get(day_of_week.strip())
    
    if worker_id:    
        worker = Worker.get_ById(worker_id)
        supplier:Supplier = worker.team.supplier  
    else:
        supplier = Supplier.get_ById(supplier_id)        
    
    at = supplier.get_availabilities_by_day(dayOfWeek)        
    open = int(at.open_time.split(':')[0])
    close = int(at.close_time.split(':')[0])   
    
    # CRIAR LOGICA PARA EXCLUIR OS HORARIOS QUE JÁ FORAM AGENDADOS
    
    times =[]
    for i in range(open, close+1):
        times.append(f"{i}:00")
        
    print(times)
    
    return render(request, 'user/schedule/partials/_options_hour.html', 
                  context= { 'times': times })

def add_schedule_to_cart(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        date = request.POST.get('date')
        time = request.POST.get('time')
        price = request.POST.get('price')
        service_id = request.POST.get('service_id')
        worker_id = request.POST.get('worker_id')
        user_id = request.POST.get('user_id')       
        
        
        schedule = { 'quantity': quantity, 'date': date, 'time': time, 'price': price, 'service_id': service_id, 'worker_id': worker_id, 'user_id': user_id}
        try:            
            if 'schedule_cart' in request.session:   
                schedule_cart = request.session['schedule_cart']        
                if service_id in schedule_cart:                
                    schedule_cart[service_id] = schedule
                else: 
                    request.session['schedule_cart'][service_id] = schedule
                return HttpResponse({'message':'Agendamento adicionado ao carrinho com sucesso!', 'status': 200,})
            else:
                request.session['schedule_cart'] = schedule
                return HttpResponse({'message':'Agendamento adicionado ao carrinho com sucesso!', 'status': 200,})
        except:
            return HttpResponse('Erro ao adicionar agendamento ao carrinho!')
    

# ------------------- VIEWS -------------------
def service(request, service_id):
    if 'schedule_cart' in request.session:
        print(request.session['schedule_cart'])
    
    service = Service.get_ById(service_id)
    form = UserCartForm(request.POST or None, service=service, )
    
    if request.method == 'POST':
        print(request.POST)
        # form.service = service
        if form.is_valid():
            form.instance.user = request.user.user_client
            print(form)
            form.save()
            return redirect('schedule:checkout', user_id=request.user.user_client.id)
    
    current_date = datetime.now().date()
    next_week = []
    # Dicionário para mapear números de dias da semana para nomes de dias
    days_of_week = { 0: 'Seg', 1: 'Ter', 2: 'Qua', 3: 'Qui', 4: 'Sex', 5: 'Sáb', 6: 'Dom' }
   # Dicionário para mapear números de meses para nomes de meses
    months = { 1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun', 7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez' }
    # Adiciona os próximos 7 dias com o dia da semana e o nome do mês à lista
    for i in range(7):
        day = current_date + timedelta(days=i)
        day_name = days_of_week[day.weekday()]
        month_name = months[day.month]
        next_week.append({'day': day.strftime('%d'), 'complete_date': day.strftime('%d/%m/%Y'), 'week_day':day_name, 'month': month_name, 'current_date': current_date})
    
    return render(request, 'user/schedule/service.html', 
                  context={ 'service': service, 'form': form, 'next_week': next_week})

def supplier(request, supplier_id):
    supplier_details = SupplierDetails.get_ById(supplier_id)
    print(supplier_details.company_name)
    print(supplier_details.supplier.email)   
    services = supplier_details.supplier.offered_services.filter(active=True)
    
    return render(request, 'user/schedule/supplier.html', context= { 'supplier_details': supplier_details, 'services': services })

def checkout(request, cart_id):
    cart = UserCart.get_ById(cart_id)
    
    context = { 'cart': cart }
    
    return render(request, 'user/schedule/checkout.html', context=context)