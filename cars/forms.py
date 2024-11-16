from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'user',
            'car_title',
            'state',
            'city',
            'color',
            'model',
            'year',
            'condition',
            'price',
            'description',
            'car_photo',
            'car_photo_1',
            'car_photo_2',
            'car_photo_3',
            'car_photo_4',
            'car_photo_5',
            'car_photo_6',
            'car_photo_7',
            'car_photo_8',
            'car_photo_9',
            'car_photo_10',
            'features',
            'body_style',
            'engine',
            'transmission',
            'interior',
            'miles',
            'doors',
            'passengers',
            'vin_no',
            'milage',
            'fuel_type',
            'no_of_owners',
            'is_featured',
        ]
