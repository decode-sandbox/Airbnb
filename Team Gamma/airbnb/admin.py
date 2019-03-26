from django.contrib import admin
from airbnb.models import users, usersGroup, reservations, salles, categorie, image
# Register your models here.
admin.site.register(users)
admin.site.register(usersGroup)
admin.site.register(reservations)
admin.site.register(salles)
admin.site.register(categorie)
admin.site.register(image)