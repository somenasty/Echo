import csv


class QueryInfo:
    @staticmethod
    def get_info_from_csv(code_name, csv_file_name):
        result = []
        with open(csv_file_name, "r", newline="")as f1:
            f_csv = csv.reader(f1)
            for row in f_csv:
                if row[1] == code_name:
                    result.append(row)
            return result
