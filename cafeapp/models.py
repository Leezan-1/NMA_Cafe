from django.db import models
from django.core.validators import RegexValidator
from cafeapp.choices import ORDER_STATUS

# Customer model to add customer info
class Customer(models.Model):
    fname = models.CharField(max_length=25, verbose_name='First Name')
    mname = models.CharField(max_length=40, blank=True, default=None, verbose_name='Middle Name')
    lname = models.CharField(max_length=25, verbose_name='Last Name')
    email = models.EmailField(max_length=60, unique=True, db_index=True, verbose_name='Email')
    password = models.CharField(max_length=40, verbose_name='Password')
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
    customer = models.ForeignKey(Customer, on_delete=models.SET_DEFAULT, default='Deleted', related_name="ordered_customer")
    food = models.ManyToManyField(Food, through="OrderItem", related_name="ordered_food")
    price = models.IntegerField(verbose_name="Order Price")
    initiated_date = models.DateField(auto_now=True, verbose_name="Ordered Date")
    initiated_time = models.TimeField(auto_now=True, verbose_name="Ordered Time")
    completion_date = models.DateField(blank=True, default=None, verbose_name="Completed Date")
    completion_time = models.TimeField(blank=True, default=None, verbose_name="Completed Time")
    status= models.CharField(max_length=1, choices=ORDER_STATUS, blank=False, default = 'u', verbose_name="Order Status")

    def __str__(self) -> str:
        return f"{self.id} {self.customer.fname} {self.customer.lname} - {self.price}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    fooditem = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="Quantity")

    def __str__(self) -> str:
        return f"{self.fooditem.item_name} - {self.quantity}"