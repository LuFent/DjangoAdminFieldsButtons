from django.db import models
from .adminbuttons import *


class TestClass(models.Model):
    test_field = models.CharField(max_length=50, blank=True)


class Human(models.Model):
    name = models.CharField(max_length=50, blank=True)
    height = models.IntegerField()

    def __str__(self):
        return 'human named ' + self.name


#TODO
# 1) Из кода в шаблоны
# 2) ОТдельный Js для обычной кнопки
# 3) Новые аргументы для функций js:
#   3.1) id полей для отправки
#   3.2) Ссылка REST IP
#   3.3) ???
# 4) Придумать чтото с флексом и ресайзом
#>>> apps.get_model('adminbuttons', 'TestClass')
#>>> from django.apps import apps
