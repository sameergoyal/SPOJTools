from django.shortcuts import render_to_response
from django.template.context import RequestContext
from SPOJTools.forms import CompareUsersForm
from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.spoj.com"

USER_URL = BASE_URL + "/users/"

def getSolved(user):
	html = urlopen(USER_URL+user).read()
	soup = BeautifulSoup(html, "lxml")
	content = soup.find("td","content")
	table = content.findAll("table")
	main = table[2]
	problems = [a.contents for a in main.findAll("a")]
	for prob in problems:
		if prob == []:
			problems.remove(prob)
	return problems

def home(request):
	if request.method == 'POST':
		form = CompareUsersForm(request.POST)
		if form.is_valid():
			user1 = request.POST['user1']
			user2 = request.POST['user2']
			solved1 = getSolved(user1)
			solved2 = getSolved(user2)
			diff = solved1
			for prob in solved2:
				if prob in diff:
					diff.remove(prob)
			diff.sort()
			return render_to_response('result.html',{'diff':diff},context_instance=RequestContext(request))
	else:
		form = CompareUsersForm()
	return render_to_response('index.html',{'form':form},context_instance=RequestContext(request))