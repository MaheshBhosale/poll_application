from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question

def index(request):
	latest_question_list= Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template('polls/index.html')
	context={
	'latest_question_list': latest_question_list,
	}
	return render(request,'polls/index.html',context)
	
def detail(request, question_id):
	try:
		question=Question.objects.get(pk=question_id)
	except Question.DoesNotExists:
		raise Http404("Question does not exists")
	return render(request,'polls/detail.html'.{'question:',question})

def results(request, question_id):
	response="you,re looking at the result of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("you're voting on question %s." % question_id)

