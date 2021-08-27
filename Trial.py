def inputs():
    Name = input("Enter your name :")
    Surname = input("Enter your surname :")
    Mob_No = input("Enter the mobile number :")
    if len(Mob_No) == 10:
        Birth_Date = input("Enter your birth date in dd-mm-yyyy format:")
        Age = float(input("Enter your age with months after decimal point :"))
        print("Form is submitted")
    else:
        print("Not a valid number. Please enter a valid number")
        inputs()
    print("\nThe details of the person are :\n","\nThe name is :\t", Name, "\nThe surname is :\t", Surname,
          "\nThe mobile number is :\t", Mob_No, "\nThe birth date is :\t", Birth_Date, "\nThe age is :\t", int(Age))
inputs()
