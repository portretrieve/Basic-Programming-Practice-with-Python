
print("\n")
print("Employee Number | Employee Name  | Hours Worked")
print("-----------------------------------------------")

#Opening the file and saving the file object in a variable

openFile = open("data.txt")

#Now using the readlines() function to read all lines from file object and convert 
#file object into a list

lines = openFile.readlines()

#Now using the for loop to access line items in the list

for index in lines: 

    #using the strip() to remove the empty line after each line
    line = index.strip()
    
    #Using .split() method to split each line using seperater comma and printing using indentation
    value = line.split(",")
    print(f'{value[0]:>15} | {value[1] +" "+ value[2]:14} | {value[3]}')

openFile.close()

