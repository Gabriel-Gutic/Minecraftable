from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as gtl
from django.contrib.auth import get_user_model

from Minecraftable.printer import Error, print_error, print_info


class AccountManager(BaseUserManager):
    
    def create_user(self, email, username, password, **other_fields):
        
        if not email:
            raise ValueError(gtl("Please provide an email address"))

        other_fields.setdefault('is_active', True)
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)

        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(gtl("Superuser must be asssigned to is_staff=True"))

        if other_fields.get('is_superuser') is not True:
            raise ValueError(gtl("Superuser must be asssigned to is_superuser=True"))

        return self.create_user(email, username, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="users", null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def delete(self, *args, **kwargs):
        self.image.storage.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.username

    @staticmethod
    def validation(email, username, password, password_again):
        user_model = get_user_model()

        filtered_list = user_model.objects.filter(username=username)
        if len(filtered_list) != 0:
            return Error('Username already used!')

        for c in username:
            if not c.isalnum() and c != '_':
                print(c)
                return Error('Invalid username!') 

        filtered_list = user_model.objects.filter(email=email)
        if len(filtered_list) != 0:
            return Error('Email already used!')

        if password != password_again:
            return Error("Passwords don't match!")

        if len(password) < 8:
            return Error("Password must be at least 8 characters!")
        
        print_info("Data for user: %s is valid!" % username)
        return None


    @staticmethod
    def create_user(email, username, password, **other_fields):

        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)

        if other_fields.get('is_staff') is True:
            raise ValueError(gtl("Superuser must be asssigned to is_staff=False"))

        if other_fields.get('is_superuser') is True:
            raise ValueError(gtl("Superuser must be asssigned to is_superuser=False"))

        user_model = get_user_model()

        user = user_model.objects.create_user(
            email=email,
            username=username,
            password=password,
            **other_fields
        )

        print_info("User " + str(user) + " successfully created!")
        return user
    
    @staticmethod
    def find_user(data):
        try:
            user = User.objects.get(username=data)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=data)
            except User.DoesNotExist:
                return Error("User does not exist!")
        
        return user
        
class Datapack(models.Model):
    VERSIONS = [
        (4, ('1.13 - 1.14.4')),
        (5, ('1.15 - 1.16.1')),
        (6, ('1.16.2 - 1.16.5')),
        (7, ('1.17')),
    ]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    version = models.PositiveSmallIntegerField(choices=VERSIONS, default=7)

    user =  models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name + ' --- ' + self.user.username
    

from Minecraftable.recipes.creator_from_json import create_recipe_from_json

class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    json_data = models.TextField(blank=True)

    datapack = models.ForeignKey(Datapack, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' --- ' + self.datapack.name

    def set_recipe(self, recipe):
        self.json_data = recipe.get_json_data()

    def get_recipe(self):
        recipe = create_recipe_from_json(self.json_data)

        if recipe is not None:
            return recipe
        else:
            return Error('Recipe could not be created!')


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    image = models.ImageField(null=True, blank=True, upload_to="tags")
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.storage.delete()
        super().delete(*args, **kwargs)


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_name = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="items")

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.storage.delete()
        super().delete(*args, **kwargs)

def GetElementTypeAndName(**kwargs):
    if len(kwargs) == 0:
        print_error("Not enough args for function GetElementTypeAndName")
        return
    if 'data' in kwargs: #format type~id
        type_, id = kwargs['data'].split("~")
    elif 'type_' in kwargs and 'id' in kwargs:
        type_, id = kwargs['type_'], kwargs['id']
    else:
        print_error("Bad args for function GetElementTypeAndName")
        return

    if type_ == 'item':
        return (type_, Item.objects.get(id=id).id_name)
    elif type_ == 'tag':
        return (type_, Tag.objects.get(id=id).name)
    print_error("Unknown type: %s" % type_)
    return None


def GetElementTypeAndId(**kwargs):
    if len(kwargs) == 0:
        print_error("Not enough args for function GetElementTypeAndName")
        return
    if 'data' in kwargs: #format type~name
        type_, name = kwargs['data'].split("~")
    elif 'type_' in kwargs and 'name' in kwargs:
        type_, name = kwargs['type_'], kwargs['name']
    else:
        print_error("Bad args for function GetElementTypeAndName")
        return

    if type_ == 'item':
        return (type_, Item.objects.get(id_name=name).id)
    elif type_ == 'tag':
        tags = Tag.objects.filter(name=name)

        user = None
        if 'user' in kwargs:
            user = kwargs['user']

        for tag in tags:
            if tag.user == user or tag.user == None:
                return (type_, tag.id)
    print_error("Unknown type: %s" % type_)
    return None

