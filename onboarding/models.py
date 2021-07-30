from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, contact, address, password, profile_pic):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            contact = contact,
            address = address,
            profile_pic=profile_pic,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, contact, address, password):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            contact = contact,
            address=address,
            password=password,
        )

        user.is_admin = True
        user.save()
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=250)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    city_name = models.CharField(max_length=100)
    ticket = models.CharField(max_length=100)
    date_of_booking = models.DateField(max_length=100)
    date_of_onboarding = models.DateField(max_length=100)
    date_of_returning = models.DateField(max_length=100)
    profile_pic = models.ImageField(upload_to='user/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class NewUserDetails(models.Model):
    first_name = models.CharField(max_length=250)
    city_name = models.CharField(max_length=100)
    ticket = models.CharField(max_length=100)
    date_of_booking = models.DateField(max_length=100)
    date_of_onboarding = models.DateField(max_length=100)
    date_of_returning = models.DateField(max_length=100)



class User_role(models.Model):
    role = models.CharField(max_length=200)


class User_details(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=250)
    phone_no = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    jobs_role = models.ForeignKey(User_role, on_delete=models.CASCADE, null=True)


    
def directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user, filename)

class Product_description(models.Model):
    user = models.ForeignKey(User_details, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    kitchen = models.CharField(max_length=200)
    rooms = models.CharField(max_length=200)
    image = models.ImageField(upload_to=directory_path)

    




    


