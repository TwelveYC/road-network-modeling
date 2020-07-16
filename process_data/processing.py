# from .config import output_dir
import json
import time


def process_data():
    total_lines = 32155500
    for j in range(1, 31):
        date = "data/gps_201611"
        output_dir = "data/json_data/"
        # if process_data_date <= 9:
        #     date += "0{}".format(process_data_date)
        # else:
        #     date += str(process_data_date)
        if j <= 9:
            date += "0{}".format(j)
            output_dir += "0{}".format(j)
        else:
            date += str(j)
            output_dir += str(j)

        for hours in range(24):
            with open(date, "r") as fp:
                index = 0
                # hours = 2
                hour_data = []
                while True:
                    i = fp.readline()
                    if not i:
                        break
                    else:
                        index += 1
                        tricks = i.split(",")
                        tricks[-1] = tricks[-1].replace("\n", "")
                        if index % 100 == 0:
                            print("已经完成百分之{}".format((index/total_lines)*100))
                        seconds = int(tricks[2])
                        time_hour = time.localtime(seconds).tm_hour
                        if time_hour == hours:
                            temp = [seconds]
                            temp.extend(tricks[3:])
                            hour_data.append(temp)
                output_file_name = "{}/{}_oclock.json".format(output_dir, hours)
                print(output_file_name)
                with open(output_file_name, "w") as fs:
                    json.dump(hour_data, fs)
                    hour_data.clear()
