from django.contrib import messages
from ..login.models import User
from .models import Poke
from django.db.models import Count

root = 'poke_app:home'
login_root = 'login:root'

def home(request):
	if 'user_id' in request.session:
		Uid = request.session['user_id']
		loggedUser = User.objects.get(id=Uid)
		poked_by = loggedUser.pokes_recieved.all().values("poker_name")
		otherUsers = User.objects.exclude(id=Uid)
		context = {
			'loggedUser': loggedUser,
			'otherUsers': otherUsers,
			'poked_by': poked_by
		}
		return render(request, 'poke_app/home.html', context)
	return redirect(reverse(login_root))

def poke(request, id):
	if 'user_id' in request.session:
		Uid = request.session['user_id']
		Poke.objects.Poke(id, Uid)
		return redirect(reverse(root))
	return redirect(reverse(login_root))