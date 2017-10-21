from django.contrib import admin
#importo solo la classe Post di models .models perchè si trova dentro alla cartella locale
from .models import Post
#registro post nella console di amministrazione di django
admin.site.register(Post)
