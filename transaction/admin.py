from django.contrib import admin
from .models import transaction, productTransaction
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateTimeRangeFilter

# from import_export import resources
# class TransactionResource(resources.ModelResource):
#     class Meta:
#         model = transaction
#         exclude = ('imported', )


# Register your models here.
@admin.register(transaction)
class TransactionAdmin(ImportExportModelAdmin):
    list_display= ("transaction_dt","transaction_id","total_sale","tax_total","payment_type","products_link","receipt_link",)
    fields = ["user","transaction_dt","transaction_id", "total_sale","sub_total","tax_total","deposit_total","payment_type","receipt","receipt_link","products_link"]
    list_filter = (("transaction_dt",DateTimeRangeFilter),"transaction_dt","user","payment_type",)
    search_fields = ["transaction_id"] 

    def receipt_link(self,obj=None):
        if obj is not None:
            return format_html(f'<a href="/transaction_receipt/{obj}" style="color:green;" target="_blank">View Receipt</a>')

    def products_link(self,obj):
        count = productTransaction.objects.filter(transaction=obj).count()
        url = (
            reverse("admin:transaction_producttransaction_changelist")
            + "?"
            + urlencode({"transaction__id": f"{obj.id}"})
        )
        return format_html('<a href="{}" style="color:#4e73df;">{} Product Transaction</a>', url,count)

    def has_add_permission(self, request, *args):
        return False

    def has_change_permission(self, request, *args):
        return False

    def has_delete_permission(self, request, *args):
        return False

    def has_import_permission(self,request, *args):
        return False

    def get_rangefilter_created_at_title(self, request, field_path):
        return 'Date and Time Filter'
    
    class Media:
        js = ["js/jquery.js","js/list_filter_collapse.js",]


@admin.register(productTransaction)
class ProductTransactionAdmin(ImportExportModelAdmin):
    list_display= ("transaction_date_time","barcode","name","qty","sales_price","sales_amount","tax_amount","deposit_amount","total_amount","link_transaction",)
    fields = ["transaction_date_time","barcode","name","department","qty","sales_price","cost_price","profit_per_item","Profit_amount","tax_category","tax_percentage","deposit_category","deposit","sales_amount","tax_amount",
        "deposit_amount","total_amount","payment_type","link_transaction",]
    list_filter = [("transaction_date_time",DateTimeRangeFilter),"department","tax_category","deposit_category","payment_type"]
    search_fields = ["transaction_id_num","barcode","name",] 

    def link_transaction(self,obj= None):
        if obj is not None:
            return format_html(f'<a href="/staff_portal/transaction/transaction/{obj.transaction.id}/change/" style="color:#4e73df;">{obj.transaction}</a>')
    link_transaction.short_description ="Transaction"

    def sales_amount(self,obj=None):
        return obj.qty * obj.sales_price
    
    def total_amount(self,obj=None):
        return  (obj.qty * obj.sales_price) + obj.tax_amount+obj.deposit_amount

    def profit_per_item(self,obj=None):
        return   obj.sales_price - obj.cost_price
    profit_per_item.short_description = "P/L per Item"

    def Profit_amount(self,obj=None):
        return   (obj.sales_price - obj.cost_price)*obj.qty
    Profit_amount.short_description = "P/L amount"

    def has_add_permission(self, request, *args):
        return False

    def has_change_permission(self, request, *args):
        return False

    def has_delete_permission(self, request, *args):
        return False

    def has_import_permission(self,request, *args):
        return False

    class Media:
        js = ["js/jquery.js","js/list_filter_collapse.js",]
