from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class SalesData(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)
    order_id = models.TextField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    ship_date = models.DateField(blank=True, null=True)
    ship_mode = models.TextField(blank=True, null=True)
    customer_id = models.TextField(blank=True, null=True)
    customer_name = models.TextField(blank=True, null=True)
    segment = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    postal_code = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    product_id = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    sales = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_data'


"""
class CustomUser(AbstractUser):
    pass


class SalesData(models.Model):
    order_id = models.CharField(max_length=100)
    order_date = models.DateField()
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    segment = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    product_id = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    sales = models.DecimalField(max_digits=10, decimal_places=2)

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.order_id} ({self.sales})"

    def total_sales_by_year(self, year):
        return SalesData.objects.filter(order_date__year=year).aggregate(models.Sum('sales'))['sales__sum']

    def total_orders_by_year(self, year):
        return SalesData.objects.filter(order_date__year=year).count()

    def customer_transactions_by_year(self, year):
        return SalesData.objects.filter(order_date__year=year).values('customer_name').distinct().count()

    def top_customers_by_sales(self, n=3):
        return SalesData.objects.values('customer_name').annotate(total_sales=models.Sum('sales')).order_by('-total_sales')[:n]
"""