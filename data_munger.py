import csv
import os

fileDir = "./data"
outputFile = "./formatted_daily_sales_data.csv"
with open(outputFile, "w") as output:
    writer = csv.writer(output)
    header = ["sales", "date", "region"]
    writer.writerow(header)
    for file in os.listdir(fileDir):
        with open(f"{fileDir}/{file}", "r") as input:
            reader = csv.reader(input)
            for row in reader:
                product, price, quantity, date, region = [i for i in row]
                if product == "pink morsel":
                    price = float(price[1:])
                    sale = price * int(quantity)
                    output_row = [sale, date, region]
                    writer.writerow(output_row)