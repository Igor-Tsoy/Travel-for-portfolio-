from django import forms
from .models import Train
from core.models import City


class TrainForm(forms.ModelForm):
    name = forms.CharField(label="Поезд", widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Номер поезда'}))
    from_city = forms.ModelChoiceField(label="Откуда", queryset=City.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}), )
    to_city = forms.ModelChoiceField(label="Куда", queryset=City.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    travel_time = forms.IntegerField(label="Время в пути", widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'Время пути'}))

    class Meta:
        model = Train
        fields = ('name', 'from_city', 'to_city', 'travel_time')