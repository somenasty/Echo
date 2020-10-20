import csv


class InsertInfo:
    @staticmethod
    def add_headers(headers, csv_file_name):
        with open(csv_file_name, "a", newline="", encoding='utf-8-sig') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f.close()

    @staticmethod
    def insert_to_csv(single_stock, csv_file_name):
        headers = ["日期", "股票名称", "股票价格", "股票数量", "股票总价"]
        temp_list = []
        with open(csv_file_name, "r", newline="", encoding='utf-8-sig') as f1:
            f1_csv = csv.reader(f1)
            for row in f1_csv:
                temp_list.append(row)
            if len(temp_list) == 0:
                InsertInfo.add_headers(headers, csv_file_name)

        with open(csv_file_name, "a", newline="", encoding='utf-8-sig') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(single_stock)
            f.close()
