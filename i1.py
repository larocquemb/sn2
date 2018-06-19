# t1.py

import pysnow
from config import USER, PASSWORD, INSTANCE
from datetime import datetime, timedelta

today = datetime.today()
many_days_ago = today - timedelta(days=900)
qb_query = ( pysnow.QueryBuilder()
    .field('sys_created_on').between(many_days_ago, today)
    .AND()
    .field('state').equals(['1'])
)
print(qb_query)

c = pysnow.Client(user=USER, password=PASSWORD, instance=INSTANCE)
print(c)

incident = c.resource(api_path='/table/incident')
print (incident)

response = incident.get(query=qb_query, fields=['number', 'opened', 'state', 'short_description'])
for record in response.all():
    print (record)
