from django.shortcuts import render, redirect
from django.contrib import auth
from ...models import User, UserAuth
from ...models import Supplier, SupplierDetails
from _panel.models import Service, GeneralService, Category

# --------------- PRIVATE FUNCTIONS --------------- 
def _create_user_and_login(request, email, password):
    user = UserAuth.get_ByEmail(email)
    if not user:
        user_auth = UserAuth.create_user(email=email, password=password, is_supplier=False)       
        print(user_auth)      
    # LOGIN USER                 
    return auth.authenticate(request=request, username=email, password=password)

# --------------- AJAX FUNCTIONS ---------------
# Save location in session
def save_location_session(request):
    if request.method == 'POST':
        request.session['latitude'] = request.POST['latitude']
        request.session['longitude'] = request.POST['longitude']
        request.session['city'] = request.POST['city']

# Search
def search(request):
    query = request.GET.get('q')
    city = request.GET.get('city')
    if query != '':
        if city != '':            
            services = GeneralService.get_Services(query, city)
            suppliers_details = SupplierDetails.get_BySuppliersName(query, city)    
            print('services', services)    
            return render(request, 'user/partials/_service_card.html', context= { 'services': services, 'suppliers_details': suppliers_details })
    return render(request, 'user/partials/_segments.html', context= { 'segments': Category.get_Segments()[:3]})


# --------------- VIEWS --------------

def home(request):
    if request.user.is_authenticated:
        if request.user.is_supplier:
            logout(request)
    segments = Category.get_Segments()[:3] 
    
    context = {
        'segments': segments,
    }
    return render(request, 'user/index.html', context=context)

def login(request):
    message = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_logged = auth.authenticate(request=request, username=email, password=password)
        if user_logged is not None and user_logged.is_client:
            auth.login(request, user_logged) 
            return redirect('home')
        message = 'Usuário não existe.'
    
    return render(request, 'user/authenticate/login.html', context={'message': message})

def logout(request):
    auth.logout(request)
    return redirect("home")

def register(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user_auth = _create_user_and_login(request, email, password)   
        if not user_auth:
            return render(request, 'user/register/register.html', {'error': 'Email já cadastrado.'})       
        auth.login(request, user_auth)
        user = User(user_auth=user_auth, name=request.POST['name'], phone=request.POST['phone'])
        user.save()
        
        return redirect('home')
    return render(request, 'user/register/register.html')
