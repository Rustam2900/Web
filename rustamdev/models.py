from django.db import models
from django.utils.translation import gettext_lazy as _


class Portfolio(models.Model):
    title = models.CharField(_("title"), max_length=120)
    description = models.TextField(_("description"))
    image = models.ImageField(upload_to='portfolio')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ClientFeedback(models.Model):
    name = models.CharField(_("name"), max_length=120, null=True, blank=True)
    company_name = models.CharField(_("company_name"), max_length=120, blank=True, null=True)
    comment = models.TextField(_("comment"))
    image = models.ImageField(upload_to='feedback')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    comment = models.TextField()
    is_checked = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(_("title"), max_length=120)
    description = models.TextField(_("description"))
    image = models.ImageField(upload_to='services')

    def __str__(self):
        return self.title


class Team(models.Model):
    full_name = models.CharField(_("full_name"), max_length=120)
    bio = models.TextField(_("bio"))
    position = models.CharField(_("position"), max_length=120)
    profile_image = models.ImageField(upload_to='profile_image')

    def __str__(self):
        return self.full_name
