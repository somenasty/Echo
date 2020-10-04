import tkinter as tk
import csv

from FuncInsertInfo import FuncInsertInfo
from InsertInfo import InsertInfo


class featuretest(tk.Frame):
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

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets(csv_file_name='test.csv')

    def create_widgets(self, csv_file_name):
        self.menu = tk.Button(self)
        self.menu["text"] = "录入"
        self.menu["command"] = FuncInsertInfo.main_function()
        self.menu.pack(side="top")

        self.quit = tk.Button(self, text="exit", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")



root = tk.Tk()
app = featuretest(master=root)
app.mainloop()
