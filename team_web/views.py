from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TeamMember
from .forms import TeamMemberForm

# Display home page with a list of team members.
def home(request):
    teamMembers  = TeamMember.objects.all()
    return render(request, 'home.html', {'teamMembers': teamMembers})

# Display a team member in the editting form.
def update_team_member(request, id):
    member = get_object_or_404(TeamMember, id=int(id))
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, instance=member) #pass current member to form 
        if form.is_valid():
            form.save()
            messages.success(request, "Team member updated")
            return redirect('home')
    else:
        form = TeamMemberForm(instance=member) 

    return render(request, 'team_member.html', {'member':member, 'form': form})

# Display a empty form to add a new team member.
def add_team_member(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if not form.is_valid():
            print("Form is invalid. Errors:", form.errors) 
            messages.error(request, "Form is invalid.")
        else:
            form.save()
            messages.success(request, "Team member added")
            return redirect('home')
    else:
        form = TeamMemberForm()

    return render(request, 'add_team_member.html', {'form': form})

# Delete a team member.
def delete_team_member(request, id):
   member_to_delete = TeamMember.objects.get(id=id)
   member_to_delete.delete()
   messages.success(request, "Team member deleted")
   return redirect('home') 
