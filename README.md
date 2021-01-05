# CSV-file-in-pycharm
reading , writing csv files in pycharm(python) for data analysing
import csv
with open ("updated.csv","w") as new_file:
    with open("SpendData.csv") as csv_file:
        new_data = csv.writer(new_file, delimiter=",")
        csv_data = csv.reader(csv_file, delimiter=",")
        count = 0
        for rows in csv_data:
            if count == 0:
                rows.append("diff")
                new_data.writerow(rows)
                #print(f"COLOMN-row :- {count}  {rows}")
                count += 1
            else:
                rows.append(float(rows[2]) - float(rows[3]))
                new_data.writerow(rows)
                #print (f"DATA-row :- {count}  {rows}")
                count += 1
        print(count)
