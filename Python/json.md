
## read 

``` py
import json
  
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

```

## save
``` py
a = {'aaa': 'shit'}
json.dump(a, file_name, ensure_ascii=False, indent=4)

# json.dump(a, file_name, ensure_ascii=False, indent=4)
# intent=4 is to prettify 
# ensure 中文不乱码
```