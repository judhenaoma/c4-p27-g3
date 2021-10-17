from django.contrib import admin


from .models import User
from .models import Inmueble
admin.site.register(Inmueble)
admin.site.register(User)



