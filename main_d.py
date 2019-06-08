import pandas
import datetime

FILES = "/home/dipanshu/Downloads/DummyData-20190608T084707Z-001/DummyData/"

def get_dt(s):
    y=int(s.split(" ")[0].split("-")[0])
    m=int(s.split(" ")[0].split("-")[1])
    d=int(s.split(" ")[0].split("-")[2])
    h=int(s.split(" ")[1].split(":")[0])
    mn=int(s.split(" ")[1].split(":")[1])
    s=int(s.split(" ")[1].split(":")[2])
    return datetime.datetime(y,m,d,h,mn,s)

a = pandas.read_excel(FILES + "DailyConsumption.xlsx")
