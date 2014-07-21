#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time
import datetime


utcnow = lambda: datetime.datetime.utcnow()


def generate_link(**kwargs):
    email = kwargs.get('email', None)
    location = kwargs.get('next', '/')
    key = kwargs.get('key', None)

    if email and location:
        from django_link_auth.models import Hash
        hash = hashlib.md5(email + key + str(time.time())).hexdigest()
        h = Hash()
        h.email = email
        h.hash = hash
        h.next = location
        h.save()
        return h


def delete_hash(hash):

    from django_link_auth.models import Hash

    try:
        hash = Hash.valid.get(hash=hash)
    except Hash.DoesNotExist:
        return None

    if hash:
        hash.delete()
