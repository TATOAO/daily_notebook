# read csv config

``` py

df = pd.read_csv("train.csv", nrows=1000)


df = pd.read_csv('train.csv', skiprows=[0,2,5]) 

df = pd.read_csv('train.csv', usecols=['product', 'cost'])

###### chunk process #####

chunksize = 10 ** 6
for chunk in pd.read_csv(filename, chunksize=chunksize):
    process(chunk)



chunksize = 10 ** 6
with pd.read_csv(filename, chunksize=chunksize) as reader:
    for chunk in reader:
        process(chunk)

```
