#coding utf - 8
from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from student.forms import RegForm
from django.contrib.auth import logout

from student.models import Stud, Group



  
def group_list(request):

    g_list = Group.objects.all()
    variables = RequestContext(request, {
        'g_list': g_list,
    })
    return render_to_response(
        'g_list.html',
        variables
    )


def stud_list(request, group_id):
    current_group = get_object_or_404(Group, id=group_id)
    variables = RequestContext(request, {
        'current_group': current_group,
    })
    return render_to_response(
        's_list.html',
        variables
    )
def registration(request,template_name = 'registration/registration.html',
                redirect_field_name=REDIRECT_FIELD_NAME,
                form_class = RegForm,extra_context = None,callback = None,autologin = True):

    redirect_to = request.REQUEST.get(redirect_field_name, '')

    form = form_class(request.POST or None)
    if form.is_valid():
        user = frm.save(request)

        if autologin:
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username = email,password = password)
            login(request, user)

        if callback:
            callback(request,user)

        return HttpResponseRedirect(redirect_to)

        context = {
            'form':form
        }
        context.update(extra_context or {})

        return direct_to_template(request,template_name,context)

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')