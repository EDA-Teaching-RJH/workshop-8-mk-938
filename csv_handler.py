import csv
def write_to_csv(x):    
    file = open("data.csv", "w")
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames)
    writer.writeheader()
    writer.writerow


def read_from_csv():
    pass

def sort_csv_by_column(column):
