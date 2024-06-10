from django import forms
from.models import Коллекция, Поставщик, Бух_учет, Каталог

class КоллекцияForm(forms.ModelForm):
    class Meta:
        model = Коллекция
        fields = ['season', 'year']

class ПоставщикForm(forms.ModelForm):
    class Meta:
        model = Поставщик
        fields = ['trade_mark', 'address', 'phone_number']

class Бух_учетForm(forms.ModelForm):
    class Meta:
        model = Бух_учет
        fields = ['debt', 'sales', 'count_goods']

class КаталогForm(forms.ModelForm):
    class Meta:
        model = Каталог
        fields = ['id_seller', 'shirts', 't_shirts', 'hoodies']  
