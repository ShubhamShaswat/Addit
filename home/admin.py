from django.contrib import admin

# Register your models here.
from .models import SignUp,Login,HomePost

admin.site.register(SignUp)
admin.site.register(Login)
admin.site.register(HomePost)
