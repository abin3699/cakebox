from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=200)


class Catagory(models.Model):
    
    options=(
        ("plum-cake","plum-cake"),
        ("fresh_cream","fresh_cream"),
        ("marble-cake","marble-cake"),
        ("cup-cake","cup-cake"),
        ("cream-cake","cream-cake"),
    )
    types=models.CharField(max_length=200,choices=options,default="cream-cake")
    is_available=models.BooleanField(default=True)


    def __str__(self):
        return self.types
    

class Cakes(models.Model):
    
    options=(
        ("carrot-cake","carrot-cake"),
        ("Red_velvet-cake","Red_velvet-cake"),
        ("cheese-cake","cheese-cake"),
        ("fruit-cake","fruit-cake"),
        ("chiffon-cake","chiffon-cake"),
        ("pound-cake","pound-cake"),
        ("chocolate-cake","chocolate-cake"),
        ("vanila-cake","vanila-cake"),
        ("mango-cake","mango-cake"),
        ("strawberry-cake","strawberry-cake"),
        ("butter-scotch","butter-scotch"),

    )
    name=models.CharField(max_length=200,choices=options)
    image=models.ImageField(upload_to="image")
    Catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Cake_variant(models.Model):
    Cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    options=(
        ("500-gm","500-gm"),
        ("750-gm","750-gm"),
        ("1-kg","1-kg"),
        ("2-kg","2-kg"),
        ("3-kg","3-kg"),
        ("5-kg","5-kg"),
    )
    size=models.CharField(max_length=200,choices=options,default="1-kg")
    price=models.PositiveIntegerField()


class Offer(models.Model):
    Cake_variant=models.ForeignKey(Cake_variant,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    start_date=models.DateTimeField()
    due_date=models.DateField()


class Cart(models.Model):
    Cake_variant=models.ForeignKey(Cake_variant,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Cake_variant=models.ForeignKey(Cake_variant,on_delete=models.DO_NOTHING)
    options=(
      
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatced","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    orderd_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)


from django.core.validators import MinValueValidator,MaxValueValidator

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Cake_variant=models.ForeignKey(Cake_variant,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)



    

