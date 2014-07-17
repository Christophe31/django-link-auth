Simple library to generate authentication link
====

* Function to generate link

```python
values = {'email': 'test@test.com', 'referer': '/', 'key': 'funky key}
hash = generate_link(**values)
```


* Simple view to use hash

```python
from django_link_auth.utils import delete_hash

def login(request, hash):
    add_site(request)

    try:
        obj = Hash.valid.get(hash=hash)
    except Hash.DoesNotExist:
        raise Http404

    user = authenticate(hash=hash)
    auth_login(request, user)

    delete_hash(hash)

    return redirect(obj.next)
```
