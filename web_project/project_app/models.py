from django.db import models

class Коллекция(models.Model):
    id_collection = models.AutoField(primary_key=True)
    season = models.IntegerField()
    year = models.IntegerField()

class Поставщик(models.Model):
    id_seller = models.AutoField(primary_key=True)
    trade_mark = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

class Бух_учет(models.Model):
    id_check = models.AutoField(primary_key=True)
    debt = models.FloatField()
    sales = models.FloatField()
    count_goods = models.IntegerField()

class Каталог(models.Model):
    id_catalog = models.AutoField(primary_key=True)
    id_seller = models.ForeignKey(Поставщик, on_delete=models.CASCADE)
    shirts = models.IntegerField()
    t_shirts = models.IntegerField()
    hoodies = models.IntegerField()
