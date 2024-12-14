from django.shortcuts import render, get_object_or_404, redirect
from .models import Peep
from .forms import PeepForm
from django.contrib.auth.decorators import login_required

# Home page view
def index(request):
    return render(request, 'index.html')

# List all peeps
@login_required
def peep_list(request):
    peeps = Peep.objects.all().order_by('-created_at')
    return render(request, 'peep_list.html', {'peeps': peeps})

# Create a new peep
@login_required
def peep_create(request):
    if request.method == "POST":
        form = PeepForm(request.POST, request.FILES)
        if form.is_valid():
            peep = form.save(commit=False)
            peep.user = request.user
            peep.save()
            return redirect('list_peeps')  # Ensure 'list_peeps' matches your URL name in urls.py
    else:
        form = PeepForm()
    return render(request, 'peep_form.html', {'form': form, 'form_title': 'Create Peep', 'submit_button': 'Create'})

# Edit an existing peep
@login_required
def peep_edit(request, peep_id):
    peep = get_object_or_404(Peep, pk=peep_id, user=request.user)
    if request.method == "POST":
        form = PeepForm(request.POST, request.FILES, instance=peep)
        if form.is_valid():
            form.save()
            return redirect('list_peeps')
    else:
        form = PeepForm(instance=peep)
    return render(request, 'peep_form.html', {'form': form, 'form_title': 'Edit Peep', 'submit_button': 'Save Changes'})

# Delete a peep
@login_required
def peep_delete(request, peep_id):
    peep = get_object_or_404(Peep, pk=peep_id, user=request.user)
    if request.method == "POST":
        peep.delete()
        return redirect('list_peeps')
    return render(request, 'peep_confirm_delete.html', {'peep': peep})
