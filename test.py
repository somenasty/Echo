import csv
import os

from DeleteInfo import *
from GetProfit import GetProfit
from InsertInfo import *
from QueryInfo import *
from StcokInfo import *

flag = 0
csv_file_name = "test.csv"
headers = ["日期", "股票名称", "股票价格", "股票数量", "股票总价"]
headers_flag = True

while flag != 1:
    with open(csv_file_name, "r", newline="")as f1:
        read_csv = csv.reader(f1)
        headers_flag = [x for x in read_csv]
        if len(headers_flag) == 0:
            headers_flag = False
            insert_headers = InsertInfo()
            insert_headers.add_headers(headers, csv_file_name)
    get_choice = input("1.录入 2.查询 3.结算 4.退出\n")
    if get_choice == '1':
        get_input = input("股票名称 股票价格 股票数量 (买入0/卖出1)\n")
        try:
            get_list = get_input.split(" ")
            single_stock_info = StockInfo(get_list[0], get_list[1], get_list[2], get_list[3])
            single_stock_arr = single_stock_info.transfer_to_list()
            insert_stock_info = InsertInfo()
            insert_stock_info.insert_to_csv(single_stock_arr, csv_file_name)
            csv_file_path = os.getcwd() + "/" + csv_file_name
            print(csv_file_path + " has been updated!")
        except Exception as e:
            print("Error Message:", e)
    elif get_choice == '2':
        get_code_name = input("股票名称\n")
        result = QueryInfo.get_info_from_csv(get_code_name, csv_file_name)
        for item in result:
            print(item)
    elif get_choice == '3':
        cost_list = []
        profit_list =[]
        get_code_name = input("股票名称\n")
        result = QueryInfo.get_info_from_csv(get_code_name, csv_file_name)
        # print(result)
        get_profit_info = GetProfit.count_profit(csv_file_name, result)
        print("your profit is:")
        print(get_profit_info)
    elif get_choice == '4':
        flag = 1
    else:
        print("error")
