# Generated by Django 4.2.1 on 2023-05-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('ship_date', models.DateField()),
                ('ship_mode', models.CharField(max_length=50)),
                ('customer_id', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('segment', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=100)),
                ('sales', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
