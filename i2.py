# t1.py

import pysnow
from config import USER, PASSWORD, INSTANCE

c = pysnow.Client(user=USER, password=PASSWORD, instance=INSTANCE)

incident = c.resource(api_path='/table/incident')

# Set the payload
new_record = {
        'short_description': '7330 LT card reset',
        'description': 'This is awesome',
        'impact': '2',
        'urgency': '1',
        'priority': '2',
        'category': 'Network',
        'location': 'Winnipeg',
        'assigned_to': 'Andrae Johnson',
        'assignment_group': 'Wireline Access',
        'cmdb_ci': '7330 LT card',
        'caller_id': 'Goldeye',
        'comments': 'insert Elastic search results here'
}

response = incident.create(payload=new_record)
