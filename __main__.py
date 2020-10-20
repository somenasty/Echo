from tkinter import *
from tkinter import messagebox
import os

from FuncInsertInfo import FuncInsertInfo
from GetProfit import GetProfit
from QueryInfo import QueryInfo

csv_file_name = "test.csv"
file_flag = 0
headers = ["日期", "股票名称", "股票价格", "股票数量", "股票总价"]
get_path = os.getcwd()
get_dir_list = os.listdir(get_path)
file_flag = get_dir_list.count(csv_file_name)
if file_flag == 0:
    file = open(get_path+r'\\'+csv_file_name, "w", newline="")


def submitted(e1, e2, e3, var, txt):
    code_name = e1.get()
    price = e2.get()
    amount = e3.get()
    flag = var.get()
    txt.insert(END, code_name)
    txt.insert(END, " ")
    txt.insert(END, price)
    txt.insert(END, " ")
    txt.insert(END, amount)
    txt.insert(END, " ")
    txt.insert(END, flag)
    txt.insert(END, "\n")
    FuncInsertInfo.main_function(code_name, price, amount, flag, csv_file_name)


def create():
    top = Toplevel()
    top.title('InsertInfo')
    top.geometry('600x600')
    var = StringVar()
    var1 = StringVar()
    show_panel = Text(top)

    lab_e1 = Label(top, text="股票名称")
    lab_e2 = Label(top, text="股票价格")
    lab_e3 = Label(top, text="股票数量")

    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)

    # b2 = Button(top, text='返回', command=back_to_menu)

    rd1 = Radiobutton(top, text="买入", variable=var, value=0)
    rd2 = Radiobutton(top, text="卖出", variable=var, value=1)

    lab_e1.grid(row=1, column=1)
    lab_e2.grid(row=2, column=1)
    lab_e3.grid(row=3, column=1)

    e1.grid(row=1, column=2)
    e2.grid(row=2, column=2)
    e3.grid(row=3, column=2)

    rd1.grid(row=4, column=2)
    rd2.grid(row=5, column=2)

    b1 = Button(top, text='提交', command=lambda: submitted(e1, e2, e3, var, show_panel))
    b1.grid(row=8, column=1)
    show_panel.grid(row=15, column=2, ipadx=1, ipady=1)


def query_cost(e4, text):
    cost_list = []
    cost_amount_list = []
    cost_sum = 0
    cost_amount_sum = 0
    result = QueryInfo.get_info_from_csv(e4.get(), csv_file_name)
    for item in result:
        if float(item[4]) < 0:
            cost_list.append(float(item[4]))
            cost_amount_list.append(float(item[3]))
    for cost in cost_list:
        cost_sum = cost_sum + cost
    for amount in cost_amount_list:
        cost_amount_sum = cost_amount_sum + amount
    # print("成本价格:")
    # print(round((cost_sum / cost_amount_sum), 2))
    cost_info = round((cost_sum / cost_amount_sum), 2)
    text.insert(END, chars=e4.get())
    text.insert(END, chars='  成本价格:  ')
    text.insert(END, chars=cost_info)
    text.insert(END, chars="\n")


def query_detail(e4, text):
    result = QueryInfo.get_info_from_csv(e4.get(), csv_file_name)
    for row in result:
        text.insert(END, chars=row)
        text.insert(END, '\n')


def clear_text_info(txt):
    txt.delete('1.0', END)


def query_menu():
    query_menu_window = Toplevel()
    query_menu_window.geometry('700x400')
    query_menu_window.title('Query')

    lab_e4 = Label(query_menu_window, text='股票名称')

    e4 = Entry(query_menu_window)
    show_cost_info = Text(query_menu_window)
    b2 = Button(query_menu_window, text='成本', command=lambda: query_cost(e4, show_cost_info))
    b3 = Button(query_menu_window, text='明细', command=lambda: query_detail(e4, show_cost_info))
    b4 = Button(query_menu_window, text='清空', command=lambda: clear_text_info(show_cost_info))

    lab_e4.grid(row=0, column=0)
    e4.grid(row=0, column=1)
    b2.grid(row=1, column=0)
    b3.grid(row=1, column=1)
    b4.grid(row=1, column=2)
    show_cost_info.grid(row=4, column=1)
    show_cost_info.insert(END, chars='     '.join(headers))
    show_cost_info.insert(END, chars='\n')


def get_balance(e5, txt):
    get_code_name = e5.get()
    result = QueryInfo.get_info_from_csv(get_code_name, csv_file_name)
    get_profit_info = GetProfit.count_profit(csv_file_name, result)
    if get_profit_info == 0:
        messagebox.askquestion(title='错误信息', message='没有找到购买记录')
    else:
        txt.insert(END, chars=get_code_name)
        txt.insert(END, chars="  获得利润:  ")
        txt.insert(END, chars=get_profit_info)
        txt.insert(END, chars='\n')


def balance_menu():
    balance_menu_panel = Toplevel()
    balance_menu_panel.geometry('600x600')
    balance_menu_panel.title('Balance')

    lab_e5 = Label(balance_menu_panel, text='股票名称')

    e5 = Entry(balance_menu_panel)
    show_balance_info = Text(balance_menu_panel)
    b4 = Button(balance_menu_panel, text='结算', command=lambda: get_balance(e5, show_balance_info))

    lab_e5.grid(row=0, column=3)
    e5.grid(row=0, column=4)
    b4.grid(row=1, column=3)
    show_balance_info.grid(row=2, column=4, ipadx=1, ipady=1)


root = Tk()
root.title('CountingSystem')
root.geometry('600x600')

Button(root, text='录入', command=create).grid(row=1, column=1, padx=1, pady=1)
Button(root, text='查询', command=query_menu).grid(row=1, column=2, padx=1, pady=1)
Button(root, text='结算', command=balance_menu).grid(row=1, column=3, padx=1, pady=1)
Button(root, text='退出', command=lambda: root.quit()).grid(row=1, column=4, padx=1, pady=1)

mainloop()
