from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    occupants = models.PositiveIntegerField()
    health_contact = models.PositiveIntegerField()
    police_contact = models.PositiveIntegerField()
    hood_pic = models.ImageField(upload_to='images/', blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()

    @classmethod
    def find_neigborhood(cls, neigborhood_id):
        hood = cls.objects.get(id=neigborhood_id)
        return hood

    @classmethod
    def update_neighborhood(cls, id, name):
        cls.objects.filter(pk=id).update(name=name)
        new_name_object = cls.objects.get(name=name)
        new_name = new_name_object.name
        return new_name

    @classmethod
    def update_occupants(cls, id, occupants):
        cls.objects.filter(pk=id).update(occupants=occupants)
        new_occupants_object = cls.objects.get(pk__id=id)
        new_occupants = new_name_object.occupants
        return new_occupants

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True)
    profile_pic = models.ImageField(upload_to='images/', blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Business(models.Model):
    bName = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    bEmail = models.EmailField(max_length=100)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        business = cls.objects.get(id=business_id)
        return business

    @classmethod
    def search_by_bName(cls, search_term):
        business = cls.objects.filter(bName__icontains=search_term)
        return business

    @classmethod
    def update_business(cls, id, name):
        cls.objects.filter(pk=id).update(bName=name)
        new_name_object = cls.objects.get(bName=name)
        new_name = new_name_object.bName
        return new_name

    def __str__(self):

        return self.bName

    class Meta:
        ordering = ['bName']


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_single_post(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def update_post(cls, id, content):
        cls.objects.filter(pk=id).update(title=content)
        new_name_object = cls.objects.get(pk=id)
        new_name = new_name_object.title
        return new_name

    def __str__(self):

        return self.title

    class Meta:
        ordering = ['-date_posted']
