from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


# Create your models here.
class product(models.Model):
    department       = models.ForeignKey("department",on_delete=models.RESTRICT,null=False,blank=False)
    barcode          = models.CharField(unique=True,max_length=16,blank = False,null=False)
    name             = models.CharField(max_length=125, blank = False, null = False)
    sales_price      = models.DecimalField(max_digits=7,decimal_places=2,null=False,blank = False)
    qty              = models.IntegerField(default=0,null=False)
    cost_price       = models.DecimalField(max_digits=7,decimal_places=2,default=0,null=False)
    tax_category     = models.ForeignKey("tax",on_delete=models.RESTRICT,null=False,blank=False)
    deposit_category = models.ForeignKey("deposit",on_delete=models.RESTRICT,null=False,blank=False)
    product_desc     = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return str(self.barcode) 
    
    def get_fields(self):
        return [
            ("Barcode", self.barcode),
            ("Name", self.name),
            ("Price", self.sales_price),
            ("Department Category",self.department.department_name),
            ("Tax Category",self.tax_category.tax_category),
            ("Deposit Category",self.deposit_category.deposit_category),
        ]

    def get_fields_2(self):
        return [
            ("Barcode", self.barcode),
            ("Name", self.name),
            ("Inventory Qty",self.qty),
            ("Sales Price", self.sales_price),
            ("Cost Price",self.cost_price),
            ("Department Category",self.department.department_name),
            ("Tax Category",self.tax_category.tax_category),
            ("Tax Percentage",self.tax_category.tax_percentage),
            ("Deposit Category",self.deposit_category.deposit_category),
            ("Deposit Value",self.deposit_category.deposit_value),
        ]


class department(models.Model):
    department_name = models.CharField(max_length=32,unique=True,null=False,blank=False)
    department_desc = models.TextField(blank=True)
    department_slug = models.SlugField(max_length=32,unique=True,blank=True)
    
    def __str__(self):
        return self.department_name
    
    def save(self,*args, **kwargs):
        self.department_slug= slugify(self.department_name)
        return super().save(*args, **kwargs)


class tax(models.Model):
    tax_category    = models.CharField(max_length=32,unique=True,null=False,blank=False)
    tax_desc        = models.TextField(blank=True)
    tax_percentage  = models.DecimalField(max_digits=6, decimal_places=3, validators=PERCENTAGE_VALIDATOR,null=False,blank=False)

    def __str__(self):
        return self.tax_category
    
    class Meta:
        verbose_name_plural = "Tax Information"


class deposit(models.Model):
    deposit_category    = models.CharField(max_length=32,unique=True,null=False,blank=False)
    deposit_desc        = models.TextField(blank=True)
    deposit_value       = models.DecimalField(max_digits=7,decimal_places=2,null=False,blank=False)

    def __str__(self):
        return self.deposit_category
    
    class Meta:
        verbose_name_plural = "Deposit Information"

