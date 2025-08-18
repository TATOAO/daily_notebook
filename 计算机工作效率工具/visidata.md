


# visidata 常用快捷键


## 异常处理
debug 
control + e
https://jsvine.github.io/intro-to-visidata/advanced/debugging-visidata/

## 常用问题

csv deliminator 

vd --csv-delimitor ';' data.csv

但是如果是 \t, \u0001, 直接输入进去会报错，只能接受1个字符，

一个最生硬的解决方法是，在报错的界面点击 control + e， 进入报错信息，然后
找到对应的csv.py 文件，在python 里面给他手动设置deliminator




## action

| key | 功能 |
| :----- | :----: |
| Shift-r | redo |
| Shift-u | undo |
| i  | 增加数字index列 |
| =  | 增加python expression列 |
| z;  | 增加bash expression列 |
| za  | 增加空白列 |
| a  | 增加空白行 |
| =  | 转化类型 |
| d  | 删除行 |
| e  | edit当前单元格 |
| x  | cut |

## 格式转换

| key | 功能 |
| :----- | :----: |
| % | numerical |
| $ | 金额 |

## Selection

| key | 功能 |
| :----- | :----: |
| s | 选中行(鸡肋) |
| t | toggle选中行 |
| gs | 选中全部行 |
| gt | toggle选中全部行(支持反选) |
|  &#124; | regex select column |


## plot
| key | 功能 |
| :----- | :----: |
|  F (shift f) | 统计条形图 |
| . | 使用当前行和 key column 画图 |
| ! | toggle 当前列为 key column |


## display


| key | 功能 |
| :----- | :----: |
| - | hide column |
| gv | unhide column |

## nevigation

| key | 功能 |
| :----- | :----: |
| gl | 到最右 |
| gh | 到最左 |
| gg | 到最上 |
| G | 到最下 |
| > | 同一列到下一个不同的值 |
| < | 同一列到上一个不同的值 |



## Search / filter

VisiData offers several methods to filter rows by value:

1. Filtering by Selection and Duplication:
Navigate to the relevant column: Position your cursor on the column you wish to filter.
Select rows by value:
Press | (pipe) to initiate a search-based selection.
Type the desired value you want to select.
Press Enter. This will select all rows containing that value in the current column.
Create a filtered sheet: Press " (double quote) to open a new sheet containing only the selected rows. This new sheet maintains a live reference to the original, meaning edits in the duplicate sheet will propagate to the source. 

2. Filtering via Frequency Tables:
Open the Frequency Table: Press Shift+F to view the frequency distribution of values in a column.
Select desired values: Use s or t to select the specific value(s) in the Frequency Table that you want to filter by. This action also selects the corresponding rows in the source sheet.
Return to the source sheet: Press q or Ctrl+^.
Create a filtered sheet: Press " to open a duplicate sheet containing only the rows selected from the Frequency Table.
Alternatively, from the Frequency Table, press Enter on a specific value to directly open a new sheet containing only the rows from the source sheet that match that value. 

3. Filtering using Python Expressions:
Initiate expression-based selection: Press z| or `z\` (backslash) while on the sheet.
Enter a Python expression: Type a Python expression that evaluates to True for the rows you want to keep and False for those you want to filter out. This expression can reference column names in your dataset.
Execute the expression: Press Enter to apply the filter. This will select the rows that satisfy the expression.
Create a filtered sheet: Press " to open a new sheet containing the selected rows.



## Copy

Use Shift + Y to copy a single cell (z then Shift + Y). For selected cells, use g z Shift + Y. For a single row, use Shift + Y.









