from .config import output_dir, process_data_date
import json


def process_data():
    date = "data/gps_201611"
    if process_data_date <= 9:
        date += "0{}".format(process_data_date)
    else:
        date += str(process_data_date)
    with open(date, "r") as fp:
        a = fp.readline()
        print(a.split(","))