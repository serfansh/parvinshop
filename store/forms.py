from django.forms import ModelForm
from .models import Product, Image, Color, Size, Detail, Csqp



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__( *args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']


class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = '__all__'


class SizeForm(ModelForm):
    class Meta:
        model = Size
        fields = '__all__'


class DetailForm(ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'


class CsqpForm(ModelForm):
    class Meta:
        model = Csqp
        fields = '__all__'
        exclude = ['product']
    
