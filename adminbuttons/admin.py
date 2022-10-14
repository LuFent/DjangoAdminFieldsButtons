from django.contrib import admin
from .adminbuttons import AdminFieldButtonsSet
from .adminbuttons import AdminFieldButton as AdmBtn
from .tools import admin_model_with_buttons_decorator
from django.urls import reverse_lazy, reverse
from .models import *


@admin_model_with_buttons_decorator
@admin.register(TestClass)
class BotUserAdmin(admin.ModelAdmin):

    DefaultButtonsField = AdminFieldButtonsSet(buttons=[ [AdmBtn('Button 1_1'), AdmBtn('Button 1_2')],
                                                         [AdmBtn('Button 2_1'), AdmBtn('Button 2_2')],
                                                         [AdmBtn('Button 3_1'), AdmBtn('Button 3_2'), AdmBtn('Button 3_3')]],
                                        description = 'Обычные кнопки',
                                        url=reverse_lazy('adminbuttons:catch_button'))


    TextAdminButtons = AdminFieldTextButtonsSet(buttons=[[AdmBtn('Button 1_1'), AdmBtn('Button 1_2')],
                                                         [AdmBtn('Button 2_1'), AdmBtn('Button 2_2')],
                                                         [AdmBtn('Button 3_1'), AdmBtn('Button 3_2'), AdmBtn('Button 3_3')]],
                                        description = 'Кнопки с текстом',
                                        url=reverse_lazy('adminbuttons:catch_button'))

    readonly_fields = []


