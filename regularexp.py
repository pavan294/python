'''
re.findall()
re.split()
re.sub(pattern,replace,string)
re.subn()
re.search(),re.match()   <--- object group start,end,span -->
'''
import json
x = {'name':'Ram', 'color':'White'}
k=(json.dumps(x, indent = 4,sort_keys=True))
print(json.loads(k))