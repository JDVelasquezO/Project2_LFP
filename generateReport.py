import csv

myData = [
            ["PILA", "ENTRADA", "TRANSICION"],
            ['Alex', 'Brian', 'A']
        ]
 
myFile = open('report.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")