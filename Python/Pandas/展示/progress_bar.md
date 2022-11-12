
# progress bar for pd.read

## csv 

```py

import pandas as pd


def read_csv_pgbar(csv_path, chunksize = 10000, filter_query="", **args):
	
	# get file line count
	N = 0
	if "nrows" in args:
		N = nrows
	else:
		# get lines
		N = sum(1 for _ in open(csv_path, 'r')) - 1
	
	chunk_list = []
	with tqdm(total=rows, desc = 'Rows read: ') as bar:
		for chunk in pd.read_csv(csv_path, **args, chunksize = 10000):
		if filter_query != "":
			chunk = chunk.query(filter_query)

		chunk_list.append(chunk)
		bar.update(len(chunk))
	
	df = pd.concat((f for f in chunk_list), axis = 0)

	return df
```

## excel

excel not allows chunksize, it is not  a line structure file,

[Link](https://stackoverflow.com/questions/44764892/is-there-a-chunksize-argument-for-read-excel-in-pandas ":)")


