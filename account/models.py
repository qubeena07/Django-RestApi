from django.db import models

# Create your models here.


from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
class UserManager(BaseUserManager):
    def create_user(self, email, fullname,address,phonenumber, is_subscribed, password=None,
                    password2=None):
        """
        Creates and saves a User with the given email, fullname,address,phonenumber
        password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            fullname=fullname,
            address=address,
            phonenumber=phonenumber,
            is_subscribed=is_subscribed,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, address, is_subscribed, phonenumber, password=None):
        user = self.create_user(
            email,
            fullname=fullname,
            address=address,
            phonenumber=phonenumber,
            is_subscribed=is_subscribed,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user    

   
    

    
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    fullname =  models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=12)
    is_subscribed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname","address","phonenumber","is_subscribed"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin    


    