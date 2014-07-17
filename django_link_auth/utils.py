import hashlib
import time
import datetime
from django_link_auth.models import Hash

utcnow = lambda: datetime.datetime.utcnow()


def generate_link(**kwargs):
    email = kwargs.get('email', None)
    location = kwargs.get('location', '/')
    key = kwargs.get('key', None)

    if email and location:
        hash = hashlib.md5(email + key + str(time.time())).hexdigest()
        Hash(email=email, hash=hash, next=location).save()
        return True
    else:
        return False


def delete_hash(hash):
    try:
       hash = Hash.valid.get(hash=hash)
    except Hash.DoesNotExist:
       return None