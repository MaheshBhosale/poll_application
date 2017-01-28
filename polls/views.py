from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at polss index.")

def detail(request, question_id):
	return HttpResponse("You're looking at question %s". % question_id

def results(request, question_id):
	response="you,re looking at the result of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("you're voting on question %s." % question_id)

