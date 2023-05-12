from django.shortcuts import render
from django.db import models
# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from reportlab.pdfgen import canvas

from .models import SalesData
from .serializers import SalesDataSerializer

@csrf_exempt
@api_view(['POST'])
def create_sales_data(request):
   
    if request.method == 'POST':
        serializer = SalesDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def sales_data_detail(request, pk):
    try:
        sales_data = SalesData.objects.get(pk=pk)
    except SalesData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SalesDataSerializer(sales_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SalesDataSerializer(sales_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sales_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def generate_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, 750, "Sales Report")

    orders_per_year = SalesData.objects.values('order_date__year').annotate(count=models.Count('order_id')).order_by('order_date__year')
    distinct_customers_count = SalesData.objects.values('customer_id').distinct().count()
    top_customers = SalesData.objects.values('customer_id', 'customer_name').annotate(total_sales=models.Sum('sales')).order_by('-total_sales')[:3]
    transactions_per_year = SalesData.objects.values('customer_id', 'order_date__year').annotate(count=models.Count('order_id')).order_by('customer_id', 'order_date__year')
    top_subcategories = SalesData.objects.values('sub_category').annotate(total_sales=models.Sum('sales')).order_by('-total_sales')[:3]
    region_sales = SalesData.objects.values('region').annotate(total_sales=models.Sum('sales')).order_by('-total_sales')
    sales_over_time = SalesData.objects.values('order_date__year').annotate(total_sales=models.Sum('sales')).order_by('order_date__year')

    p.setFont("Helvetica", 12)
    y = 700
    p.drawString(50, y, "Total Orders per Year")
    for i, order in enumerate(orders_per_year):
        y -= 20
        p.drawString(70, y, f"{order['order_date__year']}: {order['count']}")


    p.setFont("Helvetica", 12)
    p.drawString(50, y - 50, f"Distinct Customers Count: {distinct_customers_count}")

    p.showPage()
    y = 800
    p.setFont("Helvetica", 12)
    p.drawString(50, y, "Top 3 Customers by Total Sales")
    for i, customer in enumerate(top_customers):
        y -= 20
        p.drawString(70, y, f"{customer['customer_name']}: {customer['total_sales']}")

    p.showPage()
    y = 800
    p.setFont("Helvetica", 12)
    p.drawString(50, y, "Transactions per Year")
    for i, transaction in enumerate(transactions_per_year):
        y -= 20
        p.drawString(70, y, f"{transaction['customer_id']} - {transaction['order_date__year']}: {transaction['count']}")

    p.showPage()
    y = 800
    p.setFont("Helvetica", 12)
    p.drawString(50, y , "Top Selling Subcategories")
    y -= 50
    for i, subcategory in enumerate(top_subcategories):
        y -= 20
        p.drawString(70, y, f"{subcategory['sub_category']}: {subcategory['total_sales']}")

    p.showPage()
    p.setFont("Helvetica", 12)
    y = 800
    p.drawString(50, y, "Region Sales Performance")
    for i, region in enumerate(region_sales):
        y -= 20
        p.drawString(70, y, f"{region['region']}: {region['total_sales']}")

    p.showPage()
    p.setFont("Helvetica", 12)
    y = 800
    p.drawString(50, y, "Sales Performance Over Time")
    for i, sales in enumerate(sales_over_time):
        y -= 20
        p.drawString(70, y, f"{sales['order_date__year']}: {sales['total_sales']}")

    p.showPage()
    p.save()

    return response
