from StcokInfo import *
from InsertInfo import *
import os

s = StockInfo("加多宝", "1000", "1000")
s.debug_print()
single_stock = s.transfer_to_list()
print(single_stock)
csv_file_name = "test.csv"
# headers = ["日期", "股票名称", "股票价格", "股票数量", "股票总价"]
i = InsertInfo()
# i.add_headers(headers, csv_file_name)
i.insert_to_csv(single_stock, csv_file_name)
print(os.getcwd())