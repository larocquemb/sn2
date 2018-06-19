# t1.py

import pysnow
from config import USER, PASSWORD, INSTANCE

c = pysnow.Client(user=USER, password=PASSWORD, instance=INSTANCE)
print(c)

needit = c.resource(api_path='/table/x_58872_needit_needit')
print (needit)

new_record = {
        'short_description': 'Pysnow created incident',
        'priority': '4',
        'state': '1'
}

# create new needit record
result = needit.create(payload=new_record)
print(result)
