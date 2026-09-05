#My first project 

#Expense Tracker Project

expenses=[]    #list of expenses in form of dictionary
print("Welcome to Expenses Tracker: Enjoy the life with financial discipline")

while True:
    print("==========MENU==========")
    print("1.Add Expenses")
    print("2.View All Expenses")
    print("3.View Total Expenditure")
    print("4.Exit")

    choice=input("Please enter your choice:")
    if choice=='1':     #adding expenses 
        date=input("Enter expending date (DD/MM/YYYY) : ")
        category=input("Type of Expenditure ? (Food,Travel,Shopping,Health,Bills)")
        description=input("Description about the expenses :")
        amount=float(input("Enter the expenditure amount:"))

        expense = {
                    "Date": date,
                    "Category": category,
                    "Description": description, 
                    "Expense": amount
                }
        
        expenses.append(expense)
        print("\n Successfully addded the expenses")

    elif choice=='2':      #viewing all the expenses
        if len(expenses)==0:
            print("No expenses are done.")
        else:
            print("===========This are your Expenses===========")
            count=1
            for i in expenses:
                print(f"Expenditure No.{count} -> Date: {i['Date']}, Category: {i['Category']}, Description: {i['Description']}, Amount: ₹{i['Expense']}\n")
                count+=1
    elif choice=='3':      #View total spending
        total=0
        for i in expenses:
            total+=i["Expense"]
        print("\n Total Expenditure = ",total)
    elif choice=='4':       #for exiting user
        print("Thank You for visiting.")
        break
    else:
        print("Invalid choice.\nPlease enter a valid option (1-4)\n")

        