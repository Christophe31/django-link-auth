import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_link_auth.settings import AUTH_LINK_LIFETIME
from django_link_auth.utils import utcnow
from django.utils.timezone import now


class ValidHashManager(models.Manager):
    def get_queryset(self):
        return super(ValidHashManager, self) \
            .get_query_set().filter(
                created_at__gte=utcnow() - datetime.timedelta(0, AUTH_LINK_LIFETIME)
            )


class ExpiredHashManager(models.Manager):
    def get_queryset(self):
        return super(ExpiredHashManager, self) \
            .get_query_set().filter(
                created_at__lt=utcnow() - datetime.timedelta(0, AUTH_LINK_LIFETIME)
            )


class Hash(models.Model):
    email = models.CharField( _('Email'), max_length = 40)
    hash = models.CharField(_('Hash'), max_length=32)
    next = models.TextField(_('Next'))
    created_at = models.DateTimeField(
        _('Date and time'),
        editable=False,
        auto_now_add=True,
    )

    valid = ValidHashManager()
    expired = ExpiredHashManager()

    def __unicode__(self):
        return 'Hash for %s' % self.email

