# Create your models here.
from django.db import models
from decimal import Decimal
from colorfield.fields import ColorField
from django.conf import settings
from django.shortcuts import redirect
import pandas as pd
from inventory.models import product as Product


class Cart(object):
    def __init__(self, request):
        self.request            = request
        self.session            = request.session
        self.register_counter   = settings.CART_SESSION_ID 
        cart = self.session.get(self.register_counter)
        if not cart:
            # save an empty cart in the session
            cart = self.session[self.register_counter] = {}
        self.cart = cart

    def add(self, product, quantity, action=None):
        """
        Add a product to the cart or update its quantity.
        """
        if product.barcode in self.cart.keys():
           self.cart[product.barcode]['quantity'] += quantity
           if self.cart[product.barcode]['quantity'] == 0:
                self.remove(product)
                return
        else:
            self.cart[product.barcode] = {'barcode' : product.barcode,
                                        'name': product.name,
                                        'price': str(product.sales_price),
                                        'quantity' : quantity, 
                                        }
        self.cart[product.barcode]['tax_value'] = f"{product.sales_price * self.cart[product.barcode]['quantity']* (product.tax_category.tax_percentage/100):.2f}"
        self.cart[product.barcode]['deposit_value'] = f"{self.cart[product.barcode]['quantity']* product.deposit_category.deposit_value:.2f}"
        self.cart[product.barcode]['line_total'] = f"{(product.sales_price * self.cart[product.barcode]['quantity']) + Decimal(self.cart[product.barcode]['tax_value']) + Decimal(self.cart[product.barcode]['deposit_value']):.2f}"
        self.save()

    
    def save(self):
        # update the session cart
        self.session[self.register_counter] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = product.barcode
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.barcode):

                value['quantity'] = value['quantity'] - 1
                if(value['quantity'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        # empty cart
        self.session[self.register_counter] = {}
        self.session.modified = True

    def isNotEmpty(self):
        return bool(len(self.cart))
    
    def cartTotal(self):
        return round(pd.DataFrame(self.cart).T["line_total"].astype(float).sum(),2)

    def returns(self):
        for key, value in self.cart.items():
            value['quantity'] = value['quantity'] * (-1)
            value['tax_value'] =float(value['tax_value']) if float(value['tax_value'])==0.0 else float(value['tax_value']) * (-1) 
            value['deposit_value'] = float(value['deposit_value']) if float(value['deposit_value']) == 0.0 else float(value['deposit_value']) * (-1) 
            value['line_total'] = float(value['line_total']) * (-1)
        self.save()


# Create your models here.transaction_dt
class displayed_items(models.Model):
    barcode          = models.CharField(unique=True,max_length=16,blank = False,null=False)
    display_name     = models.CharField(max_length=125, blank = False, null = False)
    display_info     = models.CharField(max_length=125, blank = True, null = False, default = "")
    display_color    = ColorField(default='#575757')
    variable_price   = models.BooleanField(blank = False,null=False)
    
    def __str__(self):
        return self.barcode

    def save(self,*args, **kwargs):
        if Product.objects.filter(barcode=self.barcode).first():
            return super().save(*args, **kwargs)
        return False
    class Meta:
        verbose_name_plural = "Displayed Item"