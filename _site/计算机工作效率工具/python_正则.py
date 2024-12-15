import re
raw_text = '平安守护·这款保险是不是可以'
patten = f'平安.*?这款保险'


result = re.sub(patten, '这款保险', raw_text)
print(result)

# python -m 计算机工作效率工具.python_正则
