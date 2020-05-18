from django import forms 
from home import models
  
class ShipForm(forms.ModelForm): 
  
    class Meta: 
        model = models.ShipDetection 
        fields = ['ship_img']
