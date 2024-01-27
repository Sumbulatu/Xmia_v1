# # forms.py
#
# from django import forms
# from .models import Cars, CarImage, CarOnSale
#
#
# class CarForm(forms.ModelForm):
#     class Meta:
#         model = Cars
#         fields = ['car_make', 'car_brand', 'car_type', 'car_year', 'car_images']
#
#
# class CarOnSaleForm(forms.ModelForm):
#     class Meta:
#         model = CarOnSale
#         fields = ['seller_phone', 'seller_location', 'postal_code']
#
#
# class CarImageForm(forms.ModelForm):
#     class Meta:
#         model = CarImage
#         fields = ['image']
