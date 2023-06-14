
# dict to url 


```
>>> import urllib.parse
>>> params = {'a':'A', 'b':'B'}
>>> urllib.parse.urlencode(params)
```

# url to dict 


```

# import module
import urllib.parse
 
# initializing string
test_str = 'gfg=4&is=5&best=yes'
 
# printing original string
print("The original string is : " + str(test_str))
 
# parse_qs gets the Dictionary and value list
res = urllib.parse.parse_qs(test_str)

```
