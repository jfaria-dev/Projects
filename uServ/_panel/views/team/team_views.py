from django.shortcuts import render, redirect
from _panel.models import Team
from _web.models import Supplier
from _panel.forms import TeamForm
from _utils.decorator import auth_supplier_required

@auth_supplier_required
def fetch_teams(request, supplier_id):
    supplier = Supplier.get_ById(supplier_id)
    context = {
        'supplier': supplier,
        'teams': supplier.teams.all()
    }   
    
    return render(request, 'team/teams.html', context=context)

@auth_supplier_required
def view_team(request, supplier_id, team_id):
    team = Team.get_ById(team_id)
    return render(request, 'team/view.html', context={'team': team})
    

@auth_supplier_required
def add_team(request, supplier_id):
    supplier = Supplier.get_ById(supplier_id)
    form = TeamForm(request.POST or None, request.FILES or None)
    
    if request.method == 'POST':
        if form.is_valid():
            team = form.save(commit=False)
            team.supplier = supplier
            team.save()
            
            return redirect('panel:fetch_teams', supplier_id=supplier_id)
    
    context = {
        'form': form,
        'supplier': supplier
    }
    
    return render(request, 'team/add.html', context=context)

@auth_supplier_required
def edit_team(request, supplier_id, team_id):
    supplier = Supplier.get_ById(supplier_id)
    team = Team.get_ById(team_id)
    form = TeamForm(request.POST or None, request.FILES or None, instance=team)
    
    if request.method == 'POST':
        if form.is_valid():
            team = form.save(commit=False)
            team.supplier = supplier
            team.save()
            
            return redirect('panel:fetch_teams', supplier_id=supplier_id)
    
    context = {
        'supplier': supplier,
        'form': form,
    }
    
    return render(request, 'team/edit.html', context)

@auth_supplier_required
def delete_team(request, supplier_id, team_id):    
    team = Team.get_ById(team_id)   
    if team:
        team.active = False
        team.save()    
        return redirect('panel:fetch_teams', supplier_id=supplier_id)