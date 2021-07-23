import os
import json
import codecs

with codecs.open("ep.json", "r", "utf-8") as ej:
    data = json.load(ej)
#     data['dev_id'] = 'xxxx'
#     data['status'] = 'OK'
    
with codecs.open("ep.json", "w", "utf-8") as ej:
    data['dev_id'] = 'xxxx'
    data['status'] = 'OK'
    json.dump(data, ej, indent=4, sort_keys=True)
    
    

epstatuslist = [
    {"dev_id": "T12222xxx", "status": "stop"},
]

print(epstatuslist.append('xxx'))
print(epstatuslist)