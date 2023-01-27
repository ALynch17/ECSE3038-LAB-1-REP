def parallel(list):
      
    #numres=int(input("Please enter the number of resistors in parallel"))

    Reqinv=0

    for x in list:       
        Reqinv+=(1/x)

    Req=pow(Reqinv,-1)
    print(Req, "ohms")

parallel([330,1000,2200])

def potential_divider(vsval,list):
    rtotal=0
    for x in list:
        rtotal+=x
    current=vsval/rtotal
    for x in list:
        vdrop=current*x
        print(vdrop, "volts")
    
potential_divider(9,[3000,1000])

def temperature_check(num,let):
    if (let =='C'):
     if (num>=40):
          print("The patient is hyperthermic")
     elif (num<=35):
         print("The patient is hypothermic")
     elif ((num>35) and (num<40)):
         print("The patient's temperature is normal")

    if (let =='F'):
     if (num>104):
         print("The patient is hyperthermic")
     elif (num<95):
         print("The patient is hypothermic")
     elif ((num>95) and (num<104)):
         print("The patient's temperature is normal")    

temperature_check(45,'C')
temperature_check(37,'C')
temperature_check(37,'F')

