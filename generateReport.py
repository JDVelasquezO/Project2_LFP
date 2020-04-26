import csv
myData = [
            ["PILA$ENTRADA$TRANSICION"]
        ]

def generateReport(eStack, eInput, eTransition):
    
    array = []
    string = f"{eStack}${eInput}${eTransition}"
    array.append(string)

    myData.append(array)

    myFile = open('report.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)

generateReport('epsilon', 'zazabzbz', '(p, epsilon, epsilon; q, S, epsilon)')
generateReport('S', 'zazabzbz', '(p, epsilon, epsilon; q, S, epsilon)')
generateReport('zMNz', 'zazabzbz', '(p, epsilon, epsilon; q, S, epsilon)')
    # print("Writing complete")