from django.db import models
from django.core.validators import RegexValidator
from cafeapp.choices import ORDER_STATUS

# Customer model to add customer info
class Customer(models.Model):
    fname = models.CharField(max_length=25, null=False, verbose_name='First Name')
    mname = models.CharField(max_length=40, blank=True, default=None, verbose_name='Middle Name')
    lname = models.CharField(max_length=25, null=False, verbose_name='Last Name')
    email = models.EmailField(max_length=60, null=False, unique=True, db_index=True, verbose_name='Email')
    address = models.TextField(max_length=200,verbose_name= 'Address', blank=True, default=None)

    def __str__(self) -> str:
        return self.fname
    
class MobileNumber(models.Model):
    mobile_validation = RegexValidator(
        regex=r"^9(8|7)\d{8}$",
        message="mobile number must be 10 digits and start with 98 or 97",
        code='invalid_mobile_number',
    )
    mobile = models.PositiveIntegerField(
        unique=True,
        primary_key=True,
        validators=[mobile_validation,],
        verbose_name="Mobile"
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer")
    
    class Meta:
        verbose_name = "Mobile Number"
    
    def __str__(self) -> str:
        return f"{self.mobile} {self.customer.fname}"



class FoodCategory(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name="Category Name")
    class Meta:
        verbose_name_plural = "Food Categories"
    def __str__(self) -> str:
        return self.name


class Food(models.Model):
    item_name = models.CharField(max_length=30, unique=True, verbose_name="Food Item Name")
    price = models.IntegerField(verbose_name="Food Price")
    category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True, verbose_name="Category")
    f_slug = models.SlugField(db_index=True, verbose_name="Slug")
    # f_image = models.ImageField()

    class Meta:
        verbose_name = "Food Item"

    def __str__(self) -> str:
        return f"{self.item_name} - {self.price}"



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_DEFAULT, default='Deleted')
    food = models.ManyToManyField(Food)
    price = models.IntegerField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    status= models.CharField(max_length=1, choices=ORDER_STATUS, blank=False, default = 'u')

    def __str__(self) -> str:
        return f"{self.id} {self.customer.fname} {self.customer.lname} - {self.price}"
