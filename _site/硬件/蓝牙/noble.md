

## Install

``` js
npm install noble

var noble = require('noble');
```


## Connect

```js 

noble.startScanning();

device = noble._perpheral["your_id"]

device.connect()
device.disconnect()

```


## write service and characteristic

``` js


target_service = device.serices[2]

target_characteristic = target_service.characteristics[3]

target_characteristic.write('some buffer')


```


