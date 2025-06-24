from django.db import models
from datetime import datetime
import django
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser,AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.models import User, AbstractUser,AbstractBaseUser,BaseUserManager,PermissionsMixin     
from django.contrib.auth.models import BaseUserManager
from django.utils.timezone import now
from unicodedata import category
from django.db import models
from django.utils import timezone
#from viewflow.fields import CompositeKey
from io import BytesIO
from django.core.files import File
from datetime import date



# Create your models here.
class lbt_company(models.Model):
    col_co_code = models.CharField(primary_key=True, max_length=10)
    col_co_reg_no = models.CharField(max_length=50, unique=True)
    col_co_reg_date = models.DateField()
    col_co_name = models.CharField(max_length=100)
    col_co_shortname = models.CharField(max_length=20)
    col_co_phy_address = models.CharField(max_length=50)
    col_co_mailadd = models.CharField(max_length=50)
    col_co_telephone = models.CharField(max_length=100)
    col_co_mobile_no = models.CharField(max_length=100)
    col_co_email_add = models.EmailField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.col_co_code + " - " + self.col_co_name


class lbt_currency(models.Model):
    col_curr_code = models.CharField(primary_key=True,max_length=10)
    col_curr_name = models.CharField(max_length=100)
    col_curr_shortcode = models.CharField(max_length=10)
    col_curr_symbol = models.CharField(max_length=10)
    col_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
   
    
    def __str__(self):
        return self.col_curr_name
    
class lbt_exchange_rate(models.Model):
    col_exchange_id = models.AutoField(primary_key=True,)
    col_exchange_name = models.CharField(max_length=20)
    col_effective_date = models.DateField()
    col_expiry_date = models.DateField()
    col_base_curr=models.CharField(max_length=20)
    # col_base_curr_shortcode = models.CharField(max_length=10)
    col_destination_curr=models.CharField(max_length=20)
    # col_dest_curr_shortcode = models.CharField(max_length=10)
    col_base_amount = models.DecimalField(decimal_places=2, max_digits=13, default=None)
    col_dest_amount = models.DecimalField(decimal_places=2, max_digits=13, default=None)
    col_active = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    col_co_code = models.CharField(max_length=10)
   
    
class lbt_customer(models.Model):
    col_cust_no = models.CharField(max_length=30,primary_key=True)
    col_firstname = models.CharField(max_length=30)
    col_lastname = models.CharField(max_length=30)
    col_middlename = models.CharField(max_length=30, null=True)
    col_sex = models.CharField(max_length=10)
    col_grade=models.CharField(max_length=10)
    col_phys_add = models.CharField(max_length=100, null=True)
    col_mail_add = models.CharField(max_length=100, null=True)
    col_city = models.CharField(max_length=20,null=True)
    col_email = models.EmailField(max_length=50,null=True)
    col_mobi_num = models.CharField(max_length=50,null=True)
    col_telephone = models.CharField(max_length=100,null=True)
    col_group_code = models.CharField(max_length=15)
    col_active =models.BooleanField(default= True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    col_co_code = models.CharField(max_length=10)
    

    
class lbt_registration(models.Model):
    col_reg_id = models.AutoField(primary_key=True)
    col_cust_no = models.CharField(max_length=30)
    col_grade=models.CharField(max_length=100,default=3)
    col_group_code = models.CharField(max_length=15, null=True)
    col_session_id= models.IntegerField()
    col_registration_status = models.BooleanField(default=False)
    col_co_code = models.CharField(max_length=10)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
   

class lbt_transaction_log(models.Model):
    col_ref_num=models.IntegerField( primary_key=True)
    col_dr_cr = models.DecimalField(max_digits=10,decimal_places=2)
    col_acc_no = models.CharField(max_length = 30)
    col_naration=models.CharField(max_length=20)
    col_amount = models.DecimalField(decimal_places=2,max_digits=10 )
    col_balance = models.DecimalField(max_digits=10,decimal_places=2)
    col_closed = models.BigIntegerField()
    date = models.DateTimeField(default=timezone.now)

class lbt_invoice_hdr(models.Model):
    col_inv_no = models.CharField(max_length=10,unique=True)
    col_co_name = models.CharField(max_length=30)
    col_co_code = models.CharField(max_length=30)
    col_cust_no = models.CharField(max_length=30)
    col_acc_no = models.CharField(max_length = 30)
    col_group_code = models.CharField(max_length=15, null=True)
    col_session_id = models.IntegerField()
    col_inv_date = models.DateField()
    col_due_date = models.DateField()
    col_inv_total = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    col_curr_code= models.CharField(max_length=10)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
   
    
       
class lbt_invoice_dtl(models.Model):
    col_inv_line_no = models.IntegerField()
    col_inv_no = models.CharField(max_length=10,default=None)
    col_revenue_name = models.CharField(max_length=30)
    col_fee_amount = models.DecimalField(decimal_places=2, max_digits=13)
    col_line_total =  models.DecimalField(max_digits=13,decimal_places=2,null=True)
    col_quantity=models.IntegerField(default=1)
    col_inv_total =models.DecimalField(decimal_places=2, max_digits=13)
    col_co_code = models.CharField(max_length=10)
 
        
class lbt_remmitance_hdr(models.Model):
    col_rem_no = models.CharField(max_length=30)
    col_cust_no = models.CharField(max_length=30)
    col_inv_no = models.CharField(max_length=10,null=True)
    col_acc_no = models.CharField(max_length = 30)
    col_rem_date = models.DateField()
    col_session_id = models.IntegerField(null=True)
    col_rem_amount =models.DecimalField(max_digits=10,decimal_places=2,null=True)
    col_co_code = models.CharField(max_length= 30)
    col_payment_method=models.CharField(max_length= 30)
   
    col_curr_code= models.CharField(max_length=10)
    
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
   
           
class lbt_remmitance_dtl(models.Model):
    col_rem_lin_no = models.IntegerField()
    col_rem_no = models.CharField(max_length=15)
    col_inv_no = models.CharField(max_length=15,null=True)
    col_rem_date = models.DateTimeField(auto_now=True)
    col_cust_no = models.CharField(max_length=30)
    col_rem_amount =  models.DecimalField(max_digits=10,decimal_places=2,null=True)
    col_rem_line_amount =  models.DecimalField(max_digits=10,decimal_places=2)
    col_co_code = models.CharField(max_length=10)
   
    
    
class lbt_payment_type(models.Model):
    col_pay_type_code = models.CharField(max_length=10, primary_key=True)
    col_pay_type_desc = models.CharField(max_length=15)
    col_active = models.BooleanField()
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    col_co_code = models.CharField(max_length=10)
  

class ltb_cost_centres(models.Model):
    col_centre_code = models.CharField(max_length=10, primary_key=True)
    col_centre_name = models.CharField(max_length=15)
    col_active = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    col_co_code = models.CharField(max_length=10)

class ltb_session(models.Model):
    col_session_id = models.AutoField(primary_key=True)
    col_session_code = models.CharField(max_length=10,unique=True)
    col_session_name = models.CharField(max_length=15)
    col_session_year = models.IntegerField(default=2023)
    col_end_date = models.DateField()
    col_start_date = models.DateField()
    col_active = models.BooleanField(default=False)
    col_co_code = models.CharField(max_length=10)
 

class lbt_progresssion(models.Model):    
    col_grade_id = models.AutoField(primary_key=True)
    col_grade=models.CharField(max_length=100,default=3)
    col_co_code = models.CharField(max_length=100)

class lbt_level_class(models.Model):
    col_class_id= models.AutoField(primary_key=True)
    col_class_name= models.CharField(max_length=100)
    col_grade= models.CharField(max_length=100)
    col_level=models.CharField(max_length=100)
    col_co_code = models.CharField(max_length=10)
    
    
class ltb_ordinance(models.Model):
    col_ordinance_code = models.AutoField(primary_key=True)
    col_ordinance_name = models.CharField(max_length=100)
    col_effective = models.DateTimeField(auto_now=True)  # Update field name to col_effective
    col_active = models.BooleanField(default=False)
    col_co_code = models.CharField(max_length=10)
    
    
class  ltb_revenue_groups(models.Model):
    col_group_code = models.CharField(max_length=15,primary_key=True) 
    col_group_name = models.CharField(max_length=15)
    col_co_code = models.CharField(max_length=10)

class lbt_grades(models.Model):
    col_grade_name= models.CharField(max_length=100)
    
    
      
    def __str__(self):
        return self.col_group_code
    
class  ltb_revenue_object(models.Model):
    col_revenue_code = models.CharField(max_length=10, primary_key=True)
    col_revenue_name = models.CharField(max_length=15,default=None)
    col_active = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    col_co_code = models.CharField(max_length=10)
    

class ltb_revenue_structure(models.Model):
    col_ref_id = models.AutoField(primary_key=True)
    col_session_id =models.IntegerField()
    col_group_code = models.CharField(max_length=10)
    col_curr_code = models.CharField(max_length=10)
    col_ordinance_code = models.IntegerField()
    col_revenue_name = models.CharField(max_length=20)
    col_fee_amount =  models.DecimalField(max_digits=10,decimal_places=2)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    col_co_code = models.CharField(max_length=10)
   
    
class ltb_accounting_period(models.Model):
    col_period_period_name=models.CharField(max_length=20)
    col_period_code=models.IntegerField(primary_key= True)
    col_co_code = models.CharField(max_length=20)
    col_active = models.BooleanField(default=False)
    
    
    
class lbt_accounts(models.Model):
    col_cust_no = models.CharField(max_length=30)
    col_account_no = models.CharField(max_length=10,unique=True)
    col_curr_code = models.CharField(max_length=10)
    col_active =models.BooleanField(default= True)
    col_co_code = models.CharField(max_length=10)
  
   # col_account_type = models.CharField(max_length=15)

class lbt_payment_plan(models.Model):
    col_cust_no=models.CharField(max_length=20)
    col_acc_no=models.CharField(max_length=10,unique=True)
    col_date_registered=models.DateField()
    col_plan_amount= models.DecimalField(max_digits=10,decimal_places=2)
    col_number_of_installments=models.CharField(max_length=30,null=True)
    col_curr_code=models.CharField(max_length=10)
    col_expiry_date=models.DateField() 
    col_co_code = models.CharField(max_length=10)  
    
    
class FeeStatement(models.Model):
    col_cust_no = models.CharField(max_length=20)
    col_invoiced_amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_no = models.CharField(max_length=20)
    col_fees_paid = models.DecimalField(max_digits=10, decimal_places=2)
    col_date_generated = models.DateField()
    col_date_updated = models.DateField()
    col_balance = models.DecimalField(max_digits=10, decimal_places=2)
    

    class Meta:
        managed = False  # Set managed to False to indicate that this model is not managed by Django's migrations.
        db_table = 'fees_statements_view'  # Replace 'your_view_name' with the actual name of your database view.

class lbt_activity_trail_log(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    activity_type = models.CharField(max_length=20)
    model_name = models.CharField(max_length=50)
    model_id = models.CharField(max_length=50)
    action_details = models.CharField(max_length=255)
    old_data = models.TextField(blank=True, null=True)
    new_data = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.activity_type} - {self.model_name} ({self.model_id}) by User {self.user_id}"
    
class invoice_list_view(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_date = models.DateField()
    invoice_total = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    currency = models.CharField(max_length=21)
    name = models.CharField(max_length=61)
    invoice_number = models.CharField(max_length=10)
    customer_number = models.CharField(max_length=30)
    account=models.CharField(max_length=30)
    grade=models.CharField(max_length=10)

    class Meta:
        managed = False  # Set managed to False to indicate that this model is not managed by Django's migrations.
        db_table = 'invoice_list_view'    

class account_balances(models.Model):
    id = models.AutoField(primary_key=True)
    account_number =  models.CharField(max_length=30)
    customer_number =  models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
   
    class Meta:
        managed = False  # Set managed to False to indicate that this model is not managed by Django's migrations.
        db_table = 'Account_balances' 

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.EmailField(unique=True, default=None)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    date_joined = models.DateTimeField(max_length=150, null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    objects = UserManager()

