from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

from models import Barista, MenuItem, Vendor

class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/tiny_mce/textareas.js',)

# We have to unregister it, and then reregister
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Barista)
admin.site.register(MenuItem)
admin.site.register(Vendor)