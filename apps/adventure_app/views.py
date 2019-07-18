from django.shortcuts import render,redirect
from django.contrib import messages
from apps.log_reg_adventure_app.models import User
from apps.adventure_app.models import Adventure
#Render Methds

def PirateAdventure(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return redirect('/dashboard')

def Dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')

    this_pirate_id = request.session["user_id"]
    this_pirate = User.objects.get(id=this_pirate_id)
    all_pirates = User.objects.all()
    attend_list = this_pirate.pirates_attending_adventures_list.all()
    host_list = this_pirate.pirates_hosting_adventures_list.all()
    all_adventures = Adventure.objects.all()
    other_pirate_adventures = Adventure.objects.exclude(attending_adventure = this_pirate_id) 

    all_logged_user_attending_adventures_list_of_adventure_objects = Adventure.objects.filter( attending_adventure = this_pirate_id)

    context={
       'this_pirate_template': this_pirate,
       'this_pirate_id_template': this_pirate_id,
       'all_pirates_template': all_pirates,
       'attend_list': attend_list,
       'host_list': host_list,
       'all_adventures_template': all_adventures,
       'other_pirate_adventures_template': other_pirate_adventures,
       'all_logged_user_attending_adventures_list_of_adventure_objects_template': all_logged_user_attending_adventures_list_of_adventure_objects,
    }
    return render(request, "adventure_app/dashboard.html", context )

def Update(request,adventure_id):

    if 'user_id' not in request.session:
        return redirect('/')

    this_pirate_id = request.session["user_id"]
    this_pirate = User.objects.get(id=this_pirate_id)
    all_pirates = User.objects.all()
    this_pirate_adventures_attending = this_pirate.pirates_attending_adventures_list
    this_pirate_adventures_hosting = this_pirate.pirates_hosting_adventures_list
    all_adventures = Adventure.objects.all()
    this_adventure = Adventure.objects.get(id=adventure_id)
    this_ad_start_date = this_adventure.start_date

    context={
        'this_ad_start_date': this_ad_start_date,
        'this_adventure_template': this_adventure,
       'this_pirate_template': this_pirate,
       'this_pirate_id_template': this_pirate_id,
       'all_pirates_template': all_pirates,
       'this_pirate_adventures_attending_template': this_pirate_adventures_attending,
       'this_pirate_adventures_hosting_template': this_pirate_adventures_hosting,
       'all_adventures_template': all_adventures,
    }   

    return render(request, "adventure_app/update.html", context)

def Read(request, adventure_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_pirate_id = request.session["user_id"]
    this_pirate = User.objects.get(id=this_pirate_id)
    this_adventure = Adventure.objects.get(id=adventure_id)
    attend_list = this_adventure.attending_adventure
    host_list = this_adventure.hosting_adventure
    

    context = {
        'this_pirate_template': this_pirate,
        'this_adv_template': this_adventure,
        'attend_list_template': attend_list,
        'host_list_template': host_list,
        
    }

    return render(request, "adventure_app/read.html", context)

def Create(request):
    if 'user_id' not in request.session:
        return redirect('/') 
        
        
    all_adventures = Adventure.objects.all()
    my_pirate = request.session["user_id"]
    my_pirate_object = User.objects.get(id=my_pirate)
    
    context={
        "all_adventures_template": all_adventures,
        "my_pirate_template" : my_pirate_object,
    }
    return render(request, "adventure_app/create.html", context )

#Process Methods

def ProcessDashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    pass
    return redirect("/pirates_adventure/dashboard" )

def ProcessUpdate(request,adventure_id):
    if 'user_id' not in request.session:
        return redirect('/')

    errors = Adventure.objects.adventure_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/pirates_adventure/edit/'+adventure_id)

    edit_adventure = Adventure.objects.get(id=adventure_id)

    edit_adventure.name = request.POST["name"]
    edit_adventure.destination = request.POST["destination"]
    edit_adventure.start_date = request.POST["start_date"]
    edit_adventure.end_date = request.POST["end_date"]
    edit_adventure.plan = request.POST["plan"]
    my_host = User.objects.get(id = request.session["user_id"])
    # Adventure.objects.create(name=name, hosting_adventure = my_host, destination = destination, start_date = start_date, end_date = end_date, plan = plan)
    edit_adventure.save()
    return redirect("/pirates_adventure/dashboard")

def ProcessCreate(request):
    if 'user_id' not in request.session:
        return redirect('/')
    # print(request.POST.keys())

    errors = Adventure.objects.adventure_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/pirates_adventure/adventures/new')

    name = request.POST["name"]
    my_attendee = User.objects.get(id = request.session["user_id"])
    my_host = User.objects.get(id = request.session["user_id"])
    destination = request.POST["destination"]
    start_date = request.POST["start_date"]
    end_date = request.POST["end_date"]
    plan = request.POST["plan"]
    the_most_epic_adventure = Adventure.objects.create(name=name, hosting_adventure = my_host, destination = destination, start_date = start_date, end_date = end_date, plan = plan)
    the_most_epic_adventure.attending_adventure.add(my_attendee)
    return redirect("/pirates_adventure/dashboard")

def ProcessJoin(request, adventure_id):
    if 'user_id' not in request.session:
        return redirect('/')

    my_user_id = request.session["user_id"]
    my_pirate = User.objects.get(id=my_user_id)
    my_adventure = Adventure.objects.get(id=adventure_id)
    my_adventure.attending_adventure.add(my_pirate)
    return redirect("/pirates_adventure/dashboard" )

def RemoveAdventure(request,adventure_id):
    if 'user_id' not in request.session:
        return redirect('/')
    my_user_id = request.session["user_id"]
    my_pirate = User.objects.get(id=my_user_id)
    my_adventure = Adventure.objects.get(id=adventure_id)
    if my_adventure.hosting_adventure.id == my_pirate.id:
        my_adventure.delete()


    return redirect( "/pirates_adventure/dashboard" )

def CancelAdventure(request, adventure_id):
    if 'user_id' not in request.session:
        return redirect('/')

    my_user_id = request.session["user_id"]
    my_pirate = User.objects.get(id=my_user_id)
    my_adventure = Adventure.objects.get(id=adventure_id)
    my_adventure.attending_adventure.remove(my_pirate)
    return redirect("/pirates_adventure/dashboard")

#MY TO DO LIST
# urlpatterns = [
#   url(r'^/dashboard$', views.Dashboard),
#     url(r'^/adventures/edit/(?P<PLACEHOLDER_id>\d+)$', views.Update),
#     url(r'^/adventures/(?P<PLACEHOLDER_id>\d+)$', views.Read,
#     url(r'^/adventures/new$', views.Create),
    # url(r'^$', views.Adventure),


#Process Routes-hidden routes that Redirect-these are process routes
#    url(r'^/adventures/$', views.ProcessDashboard),
#     url(r'^/processUpdate$', views.ProcessUpdate),
#     url(r'^/createAdventure$', views.ProcessCreate),
#     url(r'^/joinAdventure$', views.ProcessJoin),
#     url(r'^/removeAdventure$', views.RemoveAdventure),