with open ('resultado.txt', 'r') as file:
    for match in file:
        info = match.replace("\n", '').split(' ')

        timeA = info[0]
        timeB = info[4]
        cestaA = int(info[1])    
        cestaB = int(info[3])
        if cestaA > cestaB:
            print(timeA, "venceu")
        else:
            print(timeB, "venceu")
        vitA = 0
        vitB = 0
