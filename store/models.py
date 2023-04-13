from django.db import models
import uuid



class ProductManager(models.Manager):

    def get_categories(self):
        return self.distinct().values_list('category', flat=True)


class Product(models.Model):

    genders = [
        ('b', 'Boy'),
        ('g', 'Girl'),
        ('w', 'Women')
    ]

    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, null=True, blank=True)
    clothes_for = models.CharField(max_length=250, choices=genders, null=True, blank=True)
    price = models.IntegerField()
    detail = models.ManyToManyField('Detail', blank=True)
    rating = models.IntegerField() # make a rating from 1 to 5
    main_image = models.ImageField(null=True, blank=True, 
    default='GettyImages_1177471633.jpg', upload_to='products/')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)

    objects = ProductManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-rating']

    def getRating(self):
        return [1 if i < self.rating else 0 for i in range(10)]


class Csqp(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1) # should be positiveinteger
    color = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey('Size', on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.product.name + ' ' + self.color.name + ' ' + self.size.name


class ColorManager(models.Manager):
    def get_names(self):
        return self.distinct().values_list('name', flat=True)


class Color(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
    objects = ColorManager()
        
    def __str__(self):
        return str(self.name)
        

class SizeManager(models.Manager):
    def get_names(self):
        return self.distinct().values_list('name', flat=True)


class Size(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
    
    objects = SizeManager()

    def __str__(self):
        return str(self.name)


class Image(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, 
    default='GettyImages_1177471633.jpg', upload_to='products/')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)

    class Meta:
        ordering = ['-created']
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/images/GettyImages_1177471633.jpg'
        return url


class Detail(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    material = models.CharField(max_length=250, null=True, blank=True)
    height = models.IntegerField()
    collar = models.IntegerField()
    shoulder = models.IntegerField()
    chest = models.IntegerField()
    waist = models.IntegerField()
    hips = models.IntegerField()
    wrist = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)



