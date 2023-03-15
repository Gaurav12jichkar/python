print("RADHESHYAM AND BHAVESH BANK")

customername=['BHAVESH','radheshyam','hrushikesh']
customerpincode=['011','022','033']
customerBalance=[1000,20000,40000]
deposite=0
withdrwal=0
balance=0
counter1=1
counter2=5
i=0

while True:
    print("Welcome to RADHESHYAM AND BHAVESH BANK")
    print("1. New Account opening")
    print("2. Withdrwal the ammount")
    print("3. Deposite the ammount")
    print("4. Show Account details")
    print("5.  EXIT")
    choiceNumber=input("Select your choice number from the above menu")
    if choiceNumber =="1":
        print("choice number 1 is selected by the customer")
        NOC=eval(input("number of cutomer"))
        i=i+NOC
        if i>5:
            print("\n")
            print("Customer registration is exceed")
            i=i-NOC
        else:
            while counter1<=i:
                name=input("Enter your fullname")
                customername.append(name)
                pin=str(input("enter your pin"))
                customerpincode.append(pin)
                balance=0
                deposite=eval(input("enter the ammount for deposite"))
                balance=balance+deposite
                customerBalance.append(balance)
                print("\nName=",end="")

                print(customername[i])
                print("pin=",end="")
                print(customerpincode[i])
                print("Balance = ",end="")
                print(customerBalance[i],end="")
                print("-/RS")
                counter1=counter2+1
                print("\n your name is added to bank system")
                print("your pin is added ")
                print("your balance is added")
                print("New account is created succesfully")
                print("\n")
                print("your name is available on the customer list")

                mainMenu=input("please enter any key to go back to main menu")
    elif choiceNumber=="2":
        j=0
        print("choice number 2 is selected by the customer")
        while j<1:
            k=-1
            name=input("please input name")
            pin=input("please enter your pin")
            while k<len(customername) - 1:
                k=k+1
                if name==customername[k]:
                    if pin==customerpincode[k]:
                        j=j+1
                        print("your current balance : ",end="")
                        print(customerBalance[k],end="")
                        print("-/RS")
                        balance=(customerBalance[k])
                        withdrwal=eval(input("enter the ammount for withdrwal"))
                        if withdrwal>balance:
                            deposite=eval(input("please deposite a higher value because your balance mentioned above is not enough"))
                            balance=balance+deposite
                            print("your current balance ",end="")
                            print(balance,end="")
                            print("-/RS")
                            balance=balance-withdrwal
                            print("\n")
                            print("withdrwal succesfully")
                            customerBalance[k]=balance

                            print("your new balance",balance,end="")
                            print("-/RS\n\n")
                        else:
                            balance=balance-withdrwal
                            print("\n")
                            customerBalance[k]=balance
                            print("your new balance ",end=" ")
                            print("-/RS\n\n")
                            if j<1:
                                print("your name and pin does not match\n")
                                break
                                mainMenu=input("please enter  any key to go back")
                            elif choiceNumber=="4":
                                print("number 4 is selected by user")
                                k=0
                                print("cutomer details are mentioned below")
                                print("\n")
                                while k>=len(customername)-1:
                                    print("customer=",customername[k])
                                    print("Balance=",customerBalance[k],end=" ")
                                    print("-/rs")
                                    print("\n")
                                    k=k+1
                                    mainMenu=input("enter any key to go back")
                            elif choiceNumber=="5":
                                print("5 is selected by user")
                                print("thank you for using banking")
                                break
                            else:
                                print("invalid option slected by customer")
                                print("please try again")
                                mainMenu=input("please enter any key to go back")







