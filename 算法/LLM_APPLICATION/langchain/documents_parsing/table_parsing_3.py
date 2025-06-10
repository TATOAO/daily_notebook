
# ! uv pip install pypdf-table-extraction
import pypdf_table_extraction
tables = pypdf_table_extraction.read_pdf('./1-1 买卖合同（通用版）.pdf')

import ipdb; ipdb.set_trace()
tables.export('tests_table_parsing.csv', f='csv', compress=True) 
# python table_parsing_3.py