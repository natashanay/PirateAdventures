from __future__ import unicode_literals
from django.db import models
from apps.log_reg_adventure_app.models import User
from datetime import datetime,timedelta
import re

class AdventureManager(models.Manager):
    def adventure_validator(self, postData):
        errors = {}
        if len(postData['name'])==0:
            errors["name"] = "Please enter a valid name"
        # adventure = Adventure.objects.filter(name=postData['name'])
        # add keys and values to errors dictionary for each invalid field

        if len(postData['destination'])==0:
            errors["destination"] = "Please enter a valid destination"
        if len(postData['start_date'])==0:
            errors["start_date"] = "Please enter a valid start date"
        if len(postData['end_date'])==0:
            errors["end_date"] = "Please enter a valid end date"
        if len(postData['plan'])==0:
            errors["plan"] = "Please enter a valid plan"
        if len(postData['destination']) < 3:
            errors["destination"] = "Destination should be at least 3 characters"
        if len(postData['plan']) < 3:
            errors["plan"] = "Plan should be at least 3 characters"
        if datetime.strptime(postData['start_date'], "%Y-%m-%d") <= datetime.now():
            errors["start_date"] = "Unlikely adventure date: please enter some date after today."
	    # elif:
		#Birthday at least 13 years ago validation
		# thirteen_years_ago = datetime.now() -timedelta(days=13*365)
        if datetime.strptime(postData['start_date'], "%Y-%m-%d") >= datetime.strptime(postData['end_date'], "%Y-%m-%d"):
			# messges.error(request, “Time travel is not an option. (Start date must be before end date)”, extra_tags=“birthday”)
            errors["start_time"] = "Time Travel is not an option"

        return errors


#validator to check if start date is in the future
#if end date is after start date
# inform user time travel is not allowed 

# class HasAttacked(models.Model):
#     attacker= models.ForeignKey(User, related_name="attack_list")
#     defender= models.ForeignKey(User, related_name="defend_list")
#     num_attacks = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Adventure(models.Model):
    name = models.CharField(max_length=45)
    #attending adventure is a list of User Objects of the pirates that are attending that adventure
    attending_adventure = models.ManyToManyField(User, related_name="pirates_attending_adventures_list", default = "")
    #hosting_adventure is a singular User object of the pirate that is the host of that adventure 
    hosting_adventure = models.ForeignKey(User, related_name="pirates_hosting_adventures_list", default = "")
    destination = models.CharField(max_length = 255)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AdventureManager()