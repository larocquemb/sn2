# t1.py

import pysnow
from config import USER, PASSWORD, INSTANCE
from datetime import datetime, timedelta

today = datetime.today()
many_days_ago = today - timedelta(days=600)
qb_query = ( pysnow.QueryBuilder()
    .field('sys_created_on').between(many_days_ago, today)
    .AND()
    .field('priority').equals(['4'])
)
print(qb_query)

c = pysnow.Client(user=USER, password=PASSWORD, instance=INSTANCE)
print(c)

needit = c.resource(api_path='/table/x_58872_needit_needit')
print (needit)

response = needit.get(query=qb_query, fields=['number', 'priority', 'state', 'short_description'])
for record in response.all():
    print (record)

response = needit.get(query={'priority' : 4}, fields=['number', 'priority', 'state', 'short_description'])
for record in response.all():
    print(record)
