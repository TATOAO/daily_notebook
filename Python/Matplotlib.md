# General 
plt.hist()..

这些function 在jupyter 有时候不是一定会自动plot出来，需要配合plt.show()


# histograme

```py
import matplotlib.plot as plt
output = plt.hist(dataset: np.array, bins=30)
# output (array1, array2), array1: counts, array2: 区分点
plt.show()
```