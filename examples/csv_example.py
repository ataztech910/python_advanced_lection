
import csv
 
def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["first_name"]),
        print(line["last_name"])
 
def read_file():
    with open("output.csv") as f_obj:
        csv_dict_reader(f_obj)

def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
 
def write_in_file():
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    
    path = "output.csv"
    csv_writer(data, path)

read_file()