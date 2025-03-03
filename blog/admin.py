from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Post) # forma padrão de registrar um model no admin

@admin.register(Post) # forma mais elegante de registrar um model no admin
class Post(admin.ModelAdmin):
    list_display = ('author','title', 'text', 'created_date', 'published_date') # exibe esses campos na listagem do admin
    