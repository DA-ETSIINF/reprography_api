from django.contrib import admin

# Register your models here.
from printapi.models import File, Folder, History, Funds

admin.site.register(File),
admin.site.register(Folder),
admin.site.register(History),
admin.site.register(Funds),

