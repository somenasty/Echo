import os

from InsertInfo import InsertInfo
from StcokInfo import StockInfo


class FuncInsertInfo:
    @staticmethod
    def main_function(code_name, price, amount, flag, csv_file_name):
        # try:
            single_stock_info = StockInfo(code_name, price, amount, flag)
            single_stock_arr = single_stock_info.transfer_to_list()
            insert_stock_info = InsertInfo()
            insert_stock_info.insert_to_csv(single_stock_arr, csv_file_name)
            csv_file_path = os.getcwd() + "/" + csv_file_name
            print(csv_file_path + " has been updated!")
        # except Exception as e:
        #     print("Error Message:", e)
