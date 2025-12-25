class Events:
    Date = ""
    Time = ""

    def details(month, day, year, time):
        Date = str(month) + "/" + str(day) + "/" + str(year)
        Time = time 

        print( Date + Time)




    print(details(1,1,1, " 12:50"))