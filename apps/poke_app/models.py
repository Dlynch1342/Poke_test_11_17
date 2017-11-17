from __future__ import unicode_literals

from ..login.models import User
from django.db import models


class PokeManager(models.Manager):
	def Poke(self, id, Uid):
		try:
			userToPoke = User.objects.get(id=id)
			loggedUser = User.objects.get(id=Uid)
			Poke.objects.create(poker=loggedUser, pokie=userToPoke)
		
		except :
			print "No user with that id {}".format(id)


class Poke(models.Model):
	poker = models.ForeignKey(User, related_name="pokes_made")
	pokie = models.ForeignKey(User, related_name="pokes_recieved")
	created_at = models.DateTimeField(auto_now_add=True)
	objects = PokeManager()

		

