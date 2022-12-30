from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

#class SubCategory(models.Model):
#    subcategory = models.CharField(max_length = 50)
#    #PLUS2CHOICES = [("Science"), ( "Management"), ("Commerce"), ("Others")]
#    #BACHELORSCHOICES = [("CSIT"), ( "BCA"), ("BIT"), ("Arts"), ("BBA")]
#    #MASTERSCHOICES = [("English"), ( "Arts"), ("Education"), ("Computer Science"), ("Nepali"), ("Management"]
#    #SECONDARYCHOICES = [("Under class 5"), ( "Under class 5"), ("Under class 10"), ("Nursery")]
#    def __str__(self):
#        return self.subcategory
#
#class Category(models.Model):
#    CHOICES = [("+2","+2"), ( "Bachelors","Bachelors"), ("Masters","Masters"), ("Secondary","Secondary")]
#    category = models.CharField(choices=CHOICES,max_length = 50)
#    subcategory = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, default=None)
#    def __str__(self):
#        return self.category

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, user_name = user_name, first_name = first_name, last_name = last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):
    #book = models.ManyToManyField(Books,blank=True)
    user_name = models.CharField(max_length=50, unique=True)
    level = models.CharField(max_length=50, null=True)
    faculty = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone = models.IntegerField(null=True,blank=True)
    #(validators=[MaxValueValidator(999999999)])
    email = models.EmailField(unique=True)
    credit = models.IntegerField(default = 10)
    #(validators=[MaxValueValidator(999)])
    note = models.CharField(max_length = 300,null=True, blank=True)
    invites = models.IntegerField(validators = [MaxValueValidator(2)], default=0)
    objects = CustomAccountManager()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Books(models.Model):


    def upload_path(instance,filename):
        return '/images/'.join([filename])


    bname = models.CharField(max_length = 300)
    user = models.ManyToManyField(NewUser, blank = True)
    author = models.CharField(max_length=300)
    revision = models.CharField(max_length = 4)
    publication = models.CharField(max_length=300)
    category = models.CharField(max_length=300)
    subcategory = models.CharField(max_length=300)
    #category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=upload_path,blank=True)
    description = models.TextField(blank=True)
    is_sold = models.BooleanField(default=False)
    credit = models.IntegerField(validators = [MaxValueValidator(100)], null=False)
    price = models.IntegerField(validators = [MaxValueValidator(10000)], null=True)
    def __str__(self):
        return self.bname

class Email(models.Model):
    email = models.EmailField(unique=True)
    is_registered = models.BooleanField(default=False)
    def __str__(self):
        return self.email
