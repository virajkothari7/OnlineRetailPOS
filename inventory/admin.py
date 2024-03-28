from django.contrib import admin
from .models import product, department, tax, deposit
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class ProductResource(resources.ModelResource):
    class Meta:
        model = product
        fields = ("id","barcode","name","sales_price","qty","cost_price",
            "department","department__department_name","department__department_desc",
            "department__department_slug", "tax_category", "tax_category__tax_category",
            "tax_category__tax_desc", "tax_category__tax_percentage", "deposit_category",
            "deposit_category__deposit_category","deposit_category__deposit_desc",
            "deposit_category__deposit_value", "product_desc")
        export_order = fields


@admin.register(product)
class ProductAdmin(ImportExportModelAdmin):
    editable_list = ["sales_price",'qty']
    list_display = ("barcode","name","sales_price","qty","department","tax_category","deposit_category")
    list_filter = ("department","tax_category", "deposit_category",)
    search_fields = ("name__startswith","barcode")

    # def has_import_permission(self,request):
    #     return False

    resource_class = ProductResource


@admin.register(department)
class DepartmentAdmin(ImportExportModelAdmin):
    list_display= ('department_name','department_desc','Products_In_Department')
    
    def Products_In_Department(self,obj):
        count = product.objects.filter(department=obj).count()
        url = (
            reverse("admin:inventory_product_changelist")
            + "?"
            + urlencode({"department__id": f"{obj.id}"})
        )
        return format_html('<a href="{}" style="color:green;padding-left:20px">{} Products</a>', url, count)


@admin.register(tax)
class TaxAdmin(ImportExportModelAdmin):
    list_display= ('tax_category','tax_percentage','tax_desc')


@admin.register(deposit)
class DepositAdmin(ImportExportModelAdmin):
    list_display= ('deposit_category','deposit_value','deposit_desc')
    