
axis{0 or ‘index’, 1 or ‘columns’}, default 0
Index to direct ranking.

method{‘average’, ‘min’, ‘max’, ‘first’, ‘dense’}, default ‘average’
How to rank the group of records that have the same value (i.e. ties):

```
average: average rank of the group

min: lowest rank in the group

max: highest rank in the group

first: ranks assigned in order they appear in the array

dense: like ‘min’, but rank always increases by 1 between groups.
```