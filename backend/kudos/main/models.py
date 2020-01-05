from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
    name = models.CharField(max_length=255, default='')
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    kudos_count = models.SmallIntegerField(default=3)
    orgranization = models.ForeignKey(
        Organization, related_name="user_organization",
        null=True, blank=True,on_delete=models.DO_NOTHING
    )


    def __str__(self):
        return self.username

class Kudos(models.Model):
    # remove this shit
    HEADER_CHOICES = (
        ('Thank You', 'Thank You'),
        ('Going Above and Beyond', 'Going Above and Beyond'),
        ('Team Player', 'Team Player'),
        ('Great Job!', 'Great Job!')
    )
    kudos_header = models.CharField(max_length=255, choices=HEADER_CHOICES, default='')
    kudos_message = models.CharField(max_length=255, default='')
    from_user = models.ForeignKey(CustomUser, related_name="kudos_from_user", null=True, blank=True, on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name="kudos_to_user", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.kudos_header + self.kudos_message
