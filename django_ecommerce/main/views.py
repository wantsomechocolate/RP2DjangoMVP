# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from payments.models import User
# from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib import messages


def index(request):
	uid = request.session.get('user')
	if uid is None:
		return render_to_response('index.html')
	else:
		return render_to_response(
			'user.html',
			{'user': User.objects.get(pk=uid)}
		)


# def index(request):
# 	return render_to_response(
# 		'index.html', context_instance=RequestContext(request)
# 	)

