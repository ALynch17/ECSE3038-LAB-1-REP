def parallel(list):
      
    #numres=int(input("Please enter the number of resistors in parallel"))

    Reqinv=0

    for x in list:       
        Reqinv+=(1/x)

    Req=pow(Reqinv,-1)
    print(Req, "ohms")

parallel([330,1000,2200])

