from django.shortcuts import render, redirect
from _panel.models import Team, Worker
from _panel.forms import WorkerForm
from _utils.decorator import auth_supplier_required


@auth_supplier_required
def view_worker(request, supplier_id, team_id):
    team = Team.get_ById(team_id)
    return render(request, 'team/view.html', context={'team': team})
    

@auth_supplier_required
def add_worker(request, supplier_id, team_id):
    team = Team.get_ById(team_id)
    form = WorkerForm(request.POST or None, request.FILES or None)   
    
    if request.method == 'POST':
        if form.is_valid():
            worker = form.save(commit=False)
            worker.team = team
            worker.save()
            
            return redirect('panel:view_team', supplier_id=supplier_id, team_id=team_id)
    print(form)
    context = {
        'form': form,
        'team': team
    }
    
    return render(request, 'worker/add.html', context=context)

@auth_supplier_required
def edit_worker(request, supplier_id, team_id, worker_id):
    team = Team.get_ById(team_id)
    worker = Worker.get_ById(id=worker_id)
    form = WorkerForm(request.POST or None, request.FILES or None, instance=worker)
    
    if request.method == 'POST':
        if form.is_valid():
            worker = form.save(commit=False)
            worker.team = team
            worker.save()
            
            return redirect('panel:view_team', supplier_id=supplier_id, team_id=team_id)
    context = {
        'team': team,
        'form': form,
    }
    
    return render(request, 'worker/edit.html', context)

@auth_supplier_required
def delete_worker(request, supplier_id, team_id, worker_id):
    worker = Worker.get_ById(worker_id)   
    if worker:
        worker.active = False
        worker.save()
    
        return redirect('panel:view_team', supplier_id=supplier_id, team_id=team_id)