"""csv_file = open("SpendData.csv")
for rows in csv_file:
    print (rows)"""




"""import csv
with open("SpendData.csv") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=",")
    count = 0
    for rows in csv_data:
        print(",".join(rows))
        count += 1
    print(count)"""





"""import csv
with open ("new_data.csv", "w") as new_data:
    out_data = csv.writer(new_data, delimiter=",")
    with open("SpendData.csv") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        count = 0
        for rows in csv_data:
            out_data.writerow(rows)
            #print(",".join(rows))
            count += 1
        print(count)"""



"""import csv
with open("new_data" , "w") as new_csv:
    new_file = csv.writer(new_csv, delimiter=",")
    with open("SpendData.csv") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        count = 0
        for rows in csv_data:
            new_file.writerow(rows)
            #print(",".join(rows))
            count += 1
        print(count)"""




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