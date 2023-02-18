LSBnums = {1:"one", 2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
MSBnums = {1:"ten", 2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety",0:"zero"}
TENsNums = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}

def ReadTime(input):
    out = []
    hour, tail = input.split(":")
    min = tail[:2]
    
    if len(hour)==1: #fix one digit hours
        hour = "0" + hour

    if hour == "12": 
        if tail[2] == "P": #12PM/AM fix
            hour = "00"
        else:
            hour = "24"

    if tail[2] == "P": #add 12 to hour if PM
        hour = str(int(hour[0]) + 1) + str(int(hour[1]) + 2)
    
    if hour[0] == "1":
        out.append(TENsNums[int(hour)]) #fix for tens
    else:
        out.append(MSBnums[int(hour[0])]) #append hour
        out.append(LSBnums[int(hour[1])])

    if min == "00": 
        out.append("hundred") #fix for 00
    elif min[0] == "1":
        out.append(TENsNums[int(min)]) #fix for tens
    else:
        out.append(MSBnums[int(min[0])])
        if min[1]!="0":
            out.append(LSBnums[int(min[1])])

    return " ".join(out)

if __name__ == "__main__":
    inputTime = input("Input the time to be converted in the format 3:25PM: \n")
    print(ReadTime(inputTime))