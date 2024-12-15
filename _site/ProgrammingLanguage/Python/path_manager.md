
# 路径问题


经常如果当工作路径切换的时候，有些路径就会报无法找到的错误，可以使用这个方法来避免



```py

import os
import json

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the JSON file
json_file_path = os.path.join(script_dir, 'the_file.json')

# Load the JSON file
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Example usage
print(data)


```
