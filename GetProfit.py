class GetProfit:
    @staticmethod
    def count_profit(csv_file_name, result_list):
        profit_sum = 0
        for row in result_list:
            profit_sum = round((float(row[4]) + profit_sum), 2)
        return profit_sum
