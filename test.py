from StcokInfo import *
from InsertInfo import *
from DeleteInfo import *
import os

# s = StockInfo("加多宝", "1000", "1000")
# s.debug_print()
# single_stock = s.transfer_to_list()
# print(single_stock)
# csv_file_name = "test.csv"
# # headers = ["日期", "股票名称", "股票价格", "股票数量", "股票总价"]
# i = InsertInfo()
# # i.add_headers(headers, csv_file_name)
# i.insert_to_csv(single_stock, csv_file_name)
# print(os.getcwd())
headers_flag = 0
flag = 0
csv_file_name = "test.csv"
headers = ["日期", "股票名称", "股票价格", "股票数量", "股票总价"]

while flag != 1:
    if headers_flag == 0:
        insert_headers = InsertInfo()
        insert_headers.add_headers(headers, csv_file_name)
        headers_flag += 1
    get_choice = input("1.录入 2.删除 3.退出\n")
    if get_choice == '1':
        get_input = input("股票名称 股票价格 股票数量 (买入0/卖出1)\n")
        get_list = get_input.split(" ")
        single_stock_info = StockInfo(get_list[0], get_list[1], get_list[2])
        single_stock_arr = single_stock_info.transfer_to_list()
        insert_stock_info = InsertInfo()
        insert_stock_info.insert_to_csv(single_stock_arr, csv_file_name)
        csv_file_path = os.getcwd()+"/" + csv_file_name
        print(csv_file_path + " has been updated!")
    elif get_choice == '2':
        delete_info = DeleteInfo()
    elif get_choice == '3':
        flag = 1
    else:
        print("error")