
def product(*args):
    if len(args) == 1:
        for i in args[0]:
            yield (i,)
    else:
        for x in args[0]:
            for y in product(*args[1:]):
                yield (x,) + y



aaa = [1,2,3]
bbb = ['a', 'b']
ccc = [1.0, 2.0]

# 算法/算法题/draft_general.py
for j in product(aaa, bbb, ccc):
    print(j)
