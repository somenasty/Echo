import csv


class InsertInfo:
    @staticmethod
    def add_headers(headers, csv_file_name):
        with open(csv_file_name, "a", newline="") as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f.close()

    @staticmethod
    def insert_to_csv(single_stock, csv_file_name):
        with open(csv_file_name, "a", newline="") as f:
            f_csv = csv.writer(f)
            f_csv.writerow(single_stock)
            f.close()
