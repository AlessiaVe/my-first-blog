from django.db import models
from django.utils import timezone
# as per fare un alias-> si usa quando le librerie cambiano nome per non cambiare tutto il codice

class Post(models.Model):

	"""
		Modello del post
		
		il costruttore in python è la definizione della funzione init. qui non è presente
		class Post(models.Model) si usa per dire che estende Model. Se lo lasci vuoto estende Object
		tutte le asseganzioni passano per models che ci modella le nostre tabelle 
		'auth.User' e' un link ad un altro modello
	"""
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	""" 
	per fare un metodo deve avere sempre come primo argomento self, quando lo richiami questo e' ignorato quindi publish()
	se non metti self è come se fosse un metodo static
	"""
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	# è il to string della classe
	def __str__(self):
		return self.title
