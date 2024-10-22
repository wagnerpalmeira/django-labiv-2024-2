from django import forms
from .models.promotion import Promotion

class MyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
      
       for visible in self.visible_fields():
           visible.field.widget.attrs['class'] = 'form-control'
  


class CreatePromotionForm(MyForm):
    class Meta:
        model = Promotion
        fields = ['title', 'description', 'url', 'price']
