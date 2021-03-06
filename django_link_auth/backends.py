import re
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django_link_auth.models import Hash


class LinkBackend(ModelBackend):
    def authenticate(self, hash=None):
        try:
            hash = Hash.valid.get(hash=hash)
        except Hash.DoesNotExist:
            return None

        try:
            user = User.objects.get(email=hash.email)
        except User.DoesNotExist:
            user = User(
                email=hash.email,
                username=re.sub('[.@]', '-', hash.email)
            )
            user.save()
        # hash.delete()
        return user


