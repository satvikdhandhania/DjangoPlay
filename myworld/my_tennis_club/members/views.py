from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    my_members = Member.objects.all() 
    context = {
        'mymembers': my_members,
    }
    template = loader.get_template('all_members.html')
    return HttpResponse(template.render(context=context, request=request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))