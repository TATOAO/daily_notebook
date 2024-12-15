
# general

```js
var a = "fsfds"
typeof a

```

# ojbect

```js

var a = {"a" : 123, "b": 223}

Object.keys(a)
```


# list arrays


## reduce
比如 reverse object 的key和 value

``` js 


var obj = {'a': 1, 'b': 2}
Object.keys(obj).reduce((ret, key) => {
    ret[obj[key]] = key;
    return ret;
}, {});

```