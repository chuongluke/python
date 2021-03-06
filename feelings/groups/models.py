import uuid
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from django.db import models


class Group(models.Model):
    create_at = models.DateTimeField(default=timezone.now)
    create_by = models.ForeignKey(User, related_name='%(class)s_created')
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(default='')


    class Meta:
        abstract = True


class Family(Group):
    members = models.ManyToManyField(User, related_name='families')

    class Meta:
        verbose_name_plural = 'families'


class Company(Group):
    members = models.ManyToManyField(User, related_name='companies')

    class Meta:
        verbose_name_plural = 'companies'


class Invite(models.Model):
    from_user = models.ForeignKey(User, related_name='%(class)s_created')
    to_user = models.ForeignKey(User, related_name='%(class)s_received')
    email_address = models.EmailField()
    accepted = models.BooleanField(default=False)
    uuid = models.CharField(max_length=32, default='')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.uuid = uuid.uuid4().hex
        super().save(*args, **kwargs)


class CompanyInvite(Invite):
    company = models.ForeignKey(Company, related_name='invites')


class FamilyInvite(Invite):
    family = models.ForeignKey(Family, related_name='invites')