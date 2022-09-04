from django.contrib import admin
from .adminbuttons import *

from .models import *

@admin.register(TestClass)
class BotUserAdmin(admin.ModelAdmin):

    buttons_function = AdminFieldButton([['button_5', 'data1'], ['button_2'], ['button_3', 123]], 'Обычные кнопки')
    text_button = TextAdminFieldButton([['button_5', 'data1'], ['button_2'], ['button_3', 123]], 'Кнопки с текстом')
    readonly_fields = ('buttons_function', 'text_button')


    class Media:
        js = ('admin_custom/myjs.js',)  # in static
        css = {'all': ('admin_custom/mycss.css',)}


