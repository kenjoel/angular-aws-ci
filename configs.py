import os.path
import pandas as pd
import csv

commands = [
    "undo FTP server-source",
    "undo telnet server",
    "clock timezone",
    "jhdjdhdjhd"
]

filepath = "/home/kenjoel/Downloads/14084_THK_NE9000-8_PE_01.txt"


def read_file(file : str) -> list:
    op = open(file,  )


#
# def config_check(file):
#     empty = []
#     goto = pd.DataFrame()
#     for i in commands:
#         with open(file, "r") as f:
#             data = f.read().find(i)
#             if data > 0:
#                 goto.columns.__add__(data)
#                 goto.to_csv("./soe.csv")
#                 print("command " + i + " returns " + str(data))
#             else:
#                 print("command " + i + " returns " + str(data))
#
#     # for file in files:


if __name__ == "__main__":
    pass
    # config_check(filepath)
