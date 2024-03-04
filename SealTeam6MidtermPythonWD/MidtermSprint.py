#Midterm Sprint Python Project
#Study Group Six: Bradley Ayers, Angela Flynn, Kyle Hollett
#February 17 - 28, 2024

#Main Program Imports (Other modules will be imported as needed)
import sys
import re
import datetime
import string

#Functions:

#The following function advances the program after any key is pressed. First, end='' and flush=True are used to make the print function behave (keeping the cursor at the end of that line) Next, the code checks the operating system and then proceeds accordingly. In windows, the msvcrt.getch() function records the keystroke as a byte string, but doesn't produce anything in the console. In Unix systems (such as Linux or MacOS), the terminal is set to raw mode in the try statement,temporarilly (for one keystroke) preventing the character from appearing on the console. The finally statement brings the terminal back out of raw mode. This isn't the extra feature lol. I chose to import the modules within the function because it crashed the code for me otherwise.
def AnyKey(prompt):
    print(prompt, end='', flush=True)
    if sys.platform.startswith('win'):
        import msvcrt
        msvcrt.getch()
    else:
        import tty
        import termios
        FileDesc = sys.stdin.fileno()
        OldSettings = termios.tcgetattr(FileDesc)
        try:
            tty.setraw(FileDesc)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(FileDesc, termios.TCSADRAIN, OldSettings)

#This function is a little escape hatch to allow the users to get out of a program without running it.
def Whoops(prompt):
    print(prompt, end='', flush=True)
    Oops = input().upper()
    print()
    if Oops == "END":
        return False
    else:
        return True

#This function uses regex to ensure that a number is not only a float, but has no more than the two decimal places expected for a monetary value. There were fewer monetary inputs than expected, but we're proud of this and it will definitely be recycled in future code.
def FloatTest(prompt):
    pattern = r'^\d+(\.\d{1,2})?$'
    while True:
        UserFloat = input(prompt)
        if not UserFloat:
            print()
            print("Error: cannot be blank.")
            print()
        elif not re.match(pattern, UserFloat):
            print()
            print("Error: Please double check your value.")
            print()
        else:
            return float(UserFloat)

#Welcome Screeen
print()
print("     _______. _______     ___       __ ")
print("    /       ||   ____|   /   \\     |  | ")
print("   |   (----`|  |__     /  ^  \\    |  | ")
print("    \\   \\    |   __|   /  /_\\  \\   |  | ")
print(".----)   |   |  |____ /  _____  \\  |  `----. ")
print("|_______/    |_______/__/     \\__\\ |_______| ")
print()                                              
print(".___________. _______     ___      .___  ___. ")
print("|           ||   ____|   /   \\     |   \\/   | ")
print("`---|  |----`|  |__     /  ^  \\    |  \\  /  | ")
print("    |  |     |   __|   /  /_\\  \\   |  |\\/|  | ")
print("    |  |     |  |____ /  _____  \\  |  |  |  | ")
print("    |__|     |_______/__/     \\__\\ |__|  |__| ")
print()                                             
print("              _______. __  ___   ___ ")
print("             /       ||  | \\  \\ /  / ")
print("            |   (----`|  |  \\  V  / ")
print("             \\   \\    |  |   >   < ")
print("         .----)   |   |  |  /  .  \\ ")
print("         |_______/    |__| /__/ \\__\\ ")
print()
print()

AnyKey("         *Press any key to continue*")

#Main Program: This is the menu outlined in script 6 in the Python section. Each of the other five scripts will be called within elif statements depending on the number chosen by the user. Question 6 answered by Bradley Ayers.
while True:
    print()
    print()
    print("##############################################")
    print("#                                            #")
    print("#          Midterm Sprint-Main Menu:         #")
    print("#                                            #")
    print("#     1.Complete a Travel Claim              #")
    print("#     2.Fun Interview Question               #")
    print("#     3.Cool Stuff with Strings and Dates    #")
    print("#     4.A Little Bit of Everything           #")
    print("#     5.Something Old, Something New         #")
    print("#     6.Quit                                 #")
    print("#                                            #")
    print("##############################################")
    print()
    
    MenuChoice = input("Enter choice (1-6): ")
    print()
    if not MenuChoice:
        print("Error: Choice cannot be blank.")
        AnyKey("Press any key to return to the main menu screen.")
        continue
    
    elif MenuChoice == "1":
        # Project #1- Program #1 Enter an Employee Travel Claim
        # Description: Program for the NL Chocolate Company to process salesperson travel
        # claims upon arrival from a business trip by entering the information from the
        # Travel Claim Form.
        # Author: Angela Flynn
        # Date(s): Feb. 17, 2024

        # Define program constants (comments indicate dollar or percent value)
        DAILY_RATE = 85.00 #$
        MILEAGE_RATE = 0.17 #$
        RENTAL_RATE = 65.00 #$
        HST_RATE = 0.15 #%
        DAY_BONUS_RATE = 100.00 #$
        KM_BONUS_RATE = 0.04 #$
        EXEC_BONUS_RATE = 45.00 #$
        DATE_BONUS_RATE = 50.00 #$
        
        # Define program functions
        
        # Main program
        while True:
            if not Whoops("If you accidentally chose Option 1,\ntype END and press return to go back to the main menu.\nOtherwise, press return to continue: "):
                break
            
            # Gather user input
            print()
            while True:
                EmpNum = input("Enter the employee number (99999): ")
                if EmpNum == "":
                    print("Data Entry Error - Employee number cannot be blank.")
                elif not EmpNum.isdigit():
                    print("Data Entry Error - Employee number must be digits only.")
                elif len(EmpNum) != 5:
                    print("Data Entry Error - Employee number must be 5 digits only.")
                else:
                    break
                
            while True:
                EmpFName = input("Enter the employee's first name: ").title()
                if EmpFName == "":
                    print("Data Entry Error - Employee first name cannot be blank.")
                else:
                    break
                
            while True:
                EmpLName = input("Enter the employee's last name:  ").title()
                if EmpLName == "":
                    print("Data Entry Error - Employee's last name cannot be blank.")
                else:
                    break
            print()
            
            while True:
                TripLoc = input("Enter the trip location: ")
                if not TripLoc:
                    print("Data Entry Error - Trip location cannot be blank.")
                else:
                    TripLoc = string.capwords(TripLoc)
                    break
        
            while True:
                try:
                    StartDate = input("Enter the trip start date (YYYY-MM-DD): ")
                    StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
                except:
                    print("Data Entry Error - Trip start date must be entered in valid format.")
                else:
                    break
        
            while True:
                try:
                    EndDate = input("Enter the trip end date (YYYY-MM-DD): ")
                    EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
                except:
                    print("Data Entry Error - Trip end date must be entered in valid format.")
                else:
                    if EndDate < StartDate or EndDate > StartDate + datetime.timedelta(days=7):
                        print("Data Entry Error - Trip end date must be after the start date by no more than 7 days.")
                    else:
                        break
            print()
            
            while True:
                Vehicle = input("Enter if the employee used their own vehicle or rented a vehicle (O or R): ").upper()
                if Vehicle == "":
                    print("Data Entry Error - Vehicle cannot be blank.")
                    print()
                elif Vehicle != "O" and Vehicle != "R":
                    print("Data Entry Error - Vehicle must be entered as O or R only.")
                    print()
                elif Vehicle == "R":
                    TotalKm = 0
                    break    
                elif Vehicle == "O":
                    while True:
                        TotalKm = input("Enter the total kilometers traveled: ")
                        if not TotalKm.isdigit():
                            print("Data Entry Error - Total kilometers must be a numeric value (whole number).")
                            print()
                        elif int(TotalKm) > 2000:
                            print("Data Entry Error - Total kilometers traveled cannot exceed 2000.")
                            print()
                        else:
                            TotalKm = int(TotalKm)
                            print()
                            break      
                    break
                
            while True:
                Claim = input("Enter the claim type as standard or executive (S or E): ").upper()
                if Claim == "":
                    print("Data Entry Error - Claim type cannot be blank.")
                elif Claim != "S" and Claim != "E":
                    print("Data Entry Error - Claim type must be entered as either S or E only.")
                else:
                    break
            
            # Perform calculations  
            TotalKm = int(TotalKm)    
            NumDays = (EndDate - StartDate).days
            PerDiem = NumDays * DAILY_RATE
            if Vehicle == "O":
                MileageAmt = TotalKm * MILEAGE_RATE
                MileageAmt = float(MileageAmt)
            else:
                MileageAmt = 0
            if Vehicle == "R":
                RentalAmt = NumDays * RENTAL_RATE
                RentalAmt = float(RentalAmt)
            else:
                RentalAmt = 0
            if NumDays > 3:
                NumDayBonus = DAY_BONUS_RATE
                NumDayBonus = float(NumDayBonus)
            else:
                NumDayBonus = 0
            if TotalKm > 1000:
                TotalKmBonus = TotalKm * KM_BONUS_RATE
                TotalKmBonus = float(TotalKmBonus)
            else:
                TotalKmBonus = 0
            if Claim == "E":
                ClaimBonus = NumDays * EXEC_BONUS_RATE
                ClaimBonus = float(ClaimBonus)
            else:
                ClaimBonus = 0
            if StartDate.month == 12 and StartDate.day >= 15 and StartDate.day <= 22:
                DateBonus = NumDays * DATE_BONUS_RATE
                DateBonus = float(DateBonus)
            else:
                DateBonus = 0
            
            TotalBonus = NumDayBonus + TotalKmBonus + ClaimBonus + DateBonus
            TotalBonus = float(TotalBonus)
            ClaimAmt = PerDiem + MileageAmt + RentalAmt + TotalBonus
            ClaimAmt = float(ClaimAmt)
            HST = ClaimAmt * HST_RATE
            ClaimTotal = ClaimAmt + HST
        
            # Display results
            if Vehicle == "O":
                VehicleDsp = "Owned"
            elif Vehicle == "R":
                VehicleDsp = "Rented"
            if Claim == "S":
                ClaimDsp = "Standard"
            elif Claim == "E":
                ClaimDsp = "Executive"
            PerDiemDsp =    "${:,.2f}".format(PerDiem)
            MileageAmtDsp = "${:,.2f}".format(MileageAmt)
            RentalAmtDsp =  "${:,.2f}".format(RentalAmt)
            TotalBonusDsp = "${:,.2f}".format(TotalBonus)
            ClaimAmtDsp =   "${:,.2f}".format(ClaimAmt)
            HSTDsp =        "${:,.2f}".format(HST)    
            ClaimTotalDsp = "${:,.2f}".format(ClaimTotal)
            StartDateDsp =  datetime.datetime.strftime(StartDate,"%Y-%m-%d")
            EndDateDsp =    datetime.datetime.strftime(EndDate,"%Y-%m-%d")
            print()
            print()
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"         NL Chocolate Company")
            print(f"      Employee Travel Claim Form")
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print(f" Employee Number: {EmpNum}")
            print()
            print(f" First Name: {EmpFName}")
            print(f" Last Name:  {EmpLName}")
            print()
            print(f" Trip Location:  {TripLoc}")
            print()
            print(f" Start Date (YYYY-MM-DD): {StartDateDsp}")
            print(f" End Date   (YYYY-MM-DD): {EndDateDsp}  ")
            print()
            print(f" The vehicle used for trip: {VehicleDsp}")
            print()
            if Vehicle == "O":
                print(f" Mileage: {TotalKm}")
                print()
            print(f" Claim Type: {ClaimDsp}")
            print()
            print(f" Number of trip days: {NumDays}")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print(f"  Per Diem Amount:         {PerDiemDsp:>9s}")
            if MileageAmt > 0:
                print(f"  Mileage Amount:          {MileageAmtDsp:>9s}")
            else:
                print(f"  Vehicle Rent Amount:     {RentalAmtDsp:>9s}")
            print(f"  Bonus Amount:            {TotalBonusDsp:>9s}")
            print(" ------------------------------------")
            print(f"  Claim Amount:            {ClaimAmtDsp:>9s}")
            print(f"  HST Amount:              {HSTDsp:>9s}")
            print(" ------------------------------------")
            print(f"  Claim Total:             {ClaimTotalDsp:>9s}")
            print()
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("Would you like to continue the program?")
            Continue = input("Enter Y or N: ").upper()
            print()
            if Continue == "N":
                break
        
        # Housekeeping
        print()
        print("Thank you, have a great day!")
        print()
    
    elif MenuChoice == "2":
        #A common program used at interviews for programming position is the FizzBiss problem. Create a loop to execute 100 times. For each value if the number is divisible by 5 display the word Fizz. If the value is divisible by 8 display the word Buzz. If the value is divisible by both 5 and 8 display the word FizzBizz – be careful of the order of the if’s in this problem. Otherwise display just the number.
        #Author: Kyle Hollett
        #Date: 2024-02-19
        
        print("Welcome to Fizz Buzz!")
        print("For numbers 1 to 100, this program will display\n'Fizz' if the number is a multiple of 5,\n'Buzz' if the number is a multiple of 8,\n and 'FizzBuzz' if the number is a multiple of both 5 and 8.")
        print()
        
        while True:
            if not Whoops("If you accidentally chose Option 2,\ntype END and press return to go back to the main menu.\nOtherwise, press return to continue: "):
                break

            for Number in range(1, 101):
                if Number % 5 == 0 and Number % 8 == 0:
                    print("FizzBuzz")
                elif Number % 5 == 0:
                    print("Fizz")
                elif Number % 8 == 0:
                    print("Buzz")
                else:
                    print(f"{Number}")
            
            print()
            AnyKey("Press any key to return to the main menu.")
            break
    
    elif MenuChoice == "3":
    # Cool Stuff with Strings and Dates
    # Author: Angela Flynn
    # Date: Feb. 22, 2024
    
        # Import libraries
        import random

        # Define progarm constants
        RETIRE_AGE = 65
        CUR_DATE = datetime.datetime.now()

        # Define program functions
        def generate_random_sentence():
                verbs = ['will win', 'will lose', 'will discover', "may encounter",]
                objects = ['money unexpectedly today', 'love from a stranger today', 'a promotion at work soon', 'patience in a time of need', 'many challenges in life']

                sentence = f"You {random.choice(verbs)} {random.choice(objects)}."
                return sentence

        # Main program
        while True:
            if not Whoops("If you accidentally chose Option 3,\ntype END and press return to go back to the main menu.\nOtherwise, press return to continue: "):
                break
            
            # Gather user input
            print()
            print(f"Enter Employee's Information")
            print(f"----------------------------")
            print()
            allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
            while True:
                FirstName = input("Enter the employee's first name: ").title()
                if FirstName == "":
                    print("Data Entry Error - Employee's first name cannot be blank.")
                elif set(FirstName).issubset(allowed_char) == False:
                    print("Data Entry Error - Employee's first name contains invalid characters.")
                else:
                    break
            
            while True:
                LastName = input("Enter the employee's last name: ").title()
                if LastName == "":
                    print("Data Entry Error - Employee's last name cannot be blank.")
                elif set(LastName).issubset(allowed_char) == False:
                    print("Data Entry Error - Employee's last name contains invalid characters.")
                else:
                    break

            while True:
                PhoneNum = input("Enter the employee's phone number (9999999999): ")
                if PhoneNum == "":
                    print("Data Entry Error - Phone number cannot be blank.")
                elif len(PhoneNum) != 10:  
                    print("Data Entry Error - Phone number must be 10 digits only.")
                elif PhoneNum.isdigit() == False: 
                    print("Data Entry Error - Phone number must be 10 digits only.")
                else:
                    break
            
            while True:
                try:
                    StartDate = input("Enter the employee's start date (YYYY-MM-DD): ")
                    StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
                except:
                    print("Data Entry Error - Employee's start date is not in a valid format.")
                else:
                    break

            while True:
                try:
                    BirthDate = input("Enter the employee's birthdate (YYYY-MM-DD): ")
                    BirthDate = datetime.datetime.strptime(BirthDate, "%Y-%m-%d")
                except:
                    print("Data Entry Error - Employee's birthdate is not in a valid format.")
                    continue
                
                if BirthDate > StartDate:
                    print("Data Entry Error - Employee's birthdate cannot be after start date.")
                    continue
                else:
                    break
                    
            # Perform calculations
            Age = CUR_DATE.year - BirthDate.year - ((CUR_DATE.month, CUR_DATE.day) < (BirthDate.month, BirthDate.day))
            Retire = RETIRE_AGE - Age
            Tenure = round((CUR_DATE.year - StartDate.year) + ((CUR_DATE.month - StartDate.month)/12))
            
            RandomNum = random.randint(10,99)
            RandomNum = str(RandomNum)
            RandomAlpha = random.choice(string.ascii_letters)
            RandomAlpha = str(RandomAlpha)

            EmployeeID = FirstName[0:3] + LastName[0]+ PhoneNum[6:10] + RandomNum + RandomAlpha
            
            if (BirthDate.month == 3 and BirthDate.day >= 21) or (BirthDate.month == 4 and BirthDate.day <= 19):
                Zodiac = "Aries"
                ZMessage = "According to zodiac,\nmay exhibit competitive but insecure behaviour."
            elif (BirthDate.month == 4 and BirthDate.day >= 20) or (BirthDate.month == 5 and BirthDate.day <= 20):
                Zodiac = "Taurus"
                ZMessage = "According to zodiac,\nmay exhibit loyal but stubborn behaviour."
            elif (BirthDate.month == 5 and BirthDate.day >= 21) or (BirthDate.month == 6 and BirthDate.day <= 20):
                Zodiac = "Gemini"
                ZMessage = "According to zodiac,\nmay exhibit versatile but impatient behaviour."
            elif (BirthDate.month == 6 and BirthDate.day >= 21) or (BirthDate.month == 7 and BirthDate.day <= 22):
                Zodiac = "Cancer"
                ZMessage = "According to zodiac,\nmay exhibit passionate but uncommunicative behaviour."
            elif (BirthDate.month == 7 and BirthDate.day >= 23) or (BirthDate.month == 8 and BirthDate.day <= 22):
                Zodiac = "Leo"
                ZMessage = "According to zodiac,\nmay exhibit confident but dominating behaviour."
            elif (BirthDate.month == 8 and BirthDate.day >= 23) or (BirthDate.month == 9 and BirthDate.day <= 22):
                Zodiac = "Virgo"
                ZMessage = "According to zodiac,\nmay exhibit perfectionist but self-critical behaviour."
            elif (BirthDate.month == 9 and BirthDate.day >= 23) or (BirthDate.month == 10 and BirthDate.day <= 22):
                Zodiac = "Libra"
                ZMessage = "According to zodiac,\nmay exhibit empathetic but indecisive behaviour."
            elif (BirthDate.month == 10 and BirthDate.day >= 23) or (BirthDate.month == 11 and BirthDate.day <= 21):
                Zodiac = "Scorpio"
                ZMessage = "According to zodiac,\nmay exhibit intense but secretive behaviour."
            elif (BirthDate.month == 11 and BirthDate.day >= 22) or (BirthDate.month == 12 and BirthDate.day <= 21):
                Zodiac = "Sagittarius"
                ZMessage = "According to zodiac,\nmay exhibit spontaneous but flighty behaviour."
            elif (BirthDate.month == 12 and BirthDate.day >= 22) or (BirthDate.month == 1 and BirthDate.day <= 19):
                Zodiac = "Capricorn"
                ZMessage = "According to zodiac,\nmay exhibit goal-orientated but unforgiving behaviour."
            elif (BirthDate.month == 1 and BirthDate.day >= 20) or (BirthDate.month == 2 and BirthDate.day <= 18):
                Zodiac = "Aquarius"
                ZMessage = "According to zodiac,\nmay exhibit philosophical but detached behaviour."
            else:
                Zodiac = "Pisces"
                ZMessage = "According to zodiac,\nmay exhibit whimsical but over-sensitive behaviour."
            
            if Retire >= 20:
                RetireMessage = "Not anytime soon."
            elif Retire >= 10 and Retire <= 20:
                RetireMessage = "Keep Hustling!" 
            else:
                RetireMessage = "So close!"
            
            Horoscope = generate_random_sentence()
            Name = f"{FirstName} {LastName}"
            BirthDateDsp = datetime.datetime.strftime(BirthDate, "%B %d, %Y")
            StartDateDsp = datetime.datetime.strftime(StartDate, "%B %d, %Y")
            
            # Display results

            print()
            print()
            print(f"              Employee Information List")
            print(f"---------------------------------------------------------")
            print()
            print(f"Name: {Name:<20s}   Phone Number: {PhoneNum:<}")
            print(f"Age: {Age}                      Birthday: {BirthDateDsp}")
            print()
            print(f"Employee ID: {EmployeeID}")
            print()
            print(f"Years until retirement: {Retire}")
            print(f"      \"{RetireMessage}\"")
            print()
            print(f"{Name} has worked with this company since:\n{StartDateDsp}.")
            print(f"Total years with the company: {Tenure}")
            print()
            print(f"{Name}'s zodiac sign is {Zodiac}.")
            print(f"\"{ZMessage}\"")
            print()
            print(f"{Name}'s horoscope for today is: ")
            print(f"\"{Horoscope}\"")
            print()
            print()
            
            while True:
                Continue = input("Would you like to continue with a new employee? (Y / N): ").upper()
                if Continue == "":
                    print("Data Entry Error - Continue cannot be blank")
                elif Continue != "Y" and Continue != "N":
                    print("Data Entry Error - Continue must be Y or N only.")
                else:
                    break

            if Continue == "N":
                break

        # Housekeeping
        print()
        print(f"Thank you for using our program! Have a great day!")
    
    elif MenuChoice == "4":
    #Description: Write the program based on the guidelines below. Note: I did not mention validations, loops, etc – add any features that we did in class to make this program amazing.XYZ Company is setting up a maintenance schedule for a major piece of equipment. Allow the user to enter the cost and the purchase date. They must perform basic cleaning in 10 days, tube and fluid checks in 3 weeks, and a major inspection in 6 months. Determine each date in the maintenance schedule. Determine the monthly amortization for the equipment based on a useful life of 15 years (180 months) and a salvage value based on 10% of the purchase cost. The formula to calculate the monthly amortization is amortization = (Cost – Salvage value) / Number of months. Display all input and calculated results in a well formatted output.

    #Author: Kyle Hollett

    #Date: 2024-02-19

        #Constants (units given in comments)
        SALVAGE_RATE = 0.10 #%
        CLEANING_DAYS_10 = 10
        TUBE_FLUID_CHECK_WEEKS_3 = 3
        INSPECT_MONTHS_6_IN_WEEKS = 26.07
        MONTHLY_AMORT_15YEAR = 180
        LIFETIME_WEEKS = 782
        NUMBER_CAP = 999999.99
        #functions

        def calc_amort_value(Cost):
            SalvageAmount = Cost * SALVAGE_RATE
            Amortization = (Cost - SalvageAmount) / MONTHLY_AMORT_15YEAR
            return SalvageAmount, Amortization

        def calc_maintenance_schedule(PurchaseDate):
            PurchaseDate =  datetime.datetime.strptime(PurchaseDate, '%Y-%m-%d')
            CleaningDate = PurchaseDate + datetime.timedelta(days=CLEANING_DAYS_10)
            TubeFluidCheck = PurchaseDate + datetime.timedelta(weeks=TUBE_FLUID_CHECK_WEEKS_3)
            Inspection = PurchaseDate + datetime.timedelta(weeks=INSPECT_MONTHS_6_IN_WEEKS)
            LifeTimeWarranty = PurchaseDate + datetime.timedelta(weeks=LIFETIME_WEEKS)
            return CleaningDate, TubeFluidCheck, Inspection, LifeTimeWarranty

        #User Inputs
            
        while True:
            if not Whoops("If you accidentally chose Option 4,\ntype END and press return to go back to the main menu.\nOtherwise, press return to continue: "):
                break
            
            while True:
                Cost = FloatTest("Enter cost of equipment: ")
                if Cost > NUMBER_CAP:
                    print("Cost cannot be greater than $9,999,999.99")
                    print("Try again")
                    print()
                    continue
                else:
                    print()
                    break
            
                
            while True:
                PurchaseDate = input("Enter purchase date of equipment (YYYY-MM-DD): ")
                try:
                    ValidatedPurchaseDate = datetime.datetime.strptime(PurchaseDate, '%Y-%m-%d')
                    if ValidatedPurchaseDate < datetime.datetime(1917, 1, 1):
                        print("Purchase date cannot be before 1917. Please enter a valid date.")
                        continue
                except ValueError:
                    print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
                else:
                    if ValidatedPurchaseDate > datetime.datetime.now():
                        print("Purchase date cannot be in the future. Please enter a valid date.")
                    else:
                        break
                
            #Calculations:
            SalvageAmount, Amortization = calc_amort_value(Cost)
            CleaningDate, TubeFluidCheck, Inspection, LifeTimeWarranty = calc_maintenance_schedule(PurchaseDate)

            #Format Displays
            ValidatedPurchaseDateDsp = ValidatedPurchaseDate.strftime('%Y-%m-%d')
            CostDsp = "${:,.2f}".format(Cost)
            SalvageAmountDsp = "${:,.2f}".format(SalvageAmount)
            AmortizationDsp = "${:,.2f}".format(Amortization)
            LifeTimeWarrantyDsp = LifeTimeWarranty.strftime('%Y-%m-%d')
            CleaningDateDsp = CleaningDate.strftime('%Y-%m-%d')
            TubeFluidCheckDsp = TubeFluidCheck.strftime('%Y-%m-%d')
            InspectionDsp = Inspection.strftime('%Y-%m-%d')
            #Output
            print("|--------------------------------------------------------------------------|")
            print("|                                                                          |")
            print("|               Cost, Salvage and Amortization for Equipment:              |")
            print("|                                                                          |")
            print("|--------------------------------------------------------------------------|")
            print("|   Equipment Cost:    |     Salvage Amount:    |   Monthly Amortization:  |")
            print(f"|  {CostDsp:>13s}       |    {SalvageAmountDsp:>12s}        |     {AmortizationDsp:>12s}         |")
            print("|--------------------------------------------------------------------------|")
            print("|                                                                          |")
            print("|                          Maintenance Schedule:                           |")
            print("|                                                                          |")
            print("|--------------------------------------------------------------------------|")
            print("|            Purchase Date:          |         Basic Cleaning on:          |")
            print(f"|              {ValidatedPurchaseDateDsp:>10s}            |             {CleaningDateDsp:>10s}              |")
            print("|--------------------------------------------------------------------------|")
            print("|      Tube and Fluid Checks on:     |         Major Inspection on:        |")
            print(f"|              {TubeFluidCheckDsp:>10s}            |             {InspectionDsp:>10s}              |")
            print("|--------------------------------------------------------------------------|")
            print("|                    Equipment Lifetime Valid Until:                       |")
            print(f"|                               {LifeTimeWarrantyDsp:<10s}                                 |")
            print("|--------------------------------------------------------------------------|")
            print()
            print("Would you like to continue the program?")
            Continue = input("Enter Y or N: ").upper()
            print()
            if Continue == "N":
                break
    
    elif MenuChoice == "5":
    #Midterm Sprint Question 5: Something Old, Something New
    #I created an interactive tutorial to introduce regular expressions. I chose regular expressions because not only are they useful in Python, they are commonplace in other programming languages. Regex is a powerful tool and I will illustrate that with an introduction and three examples.
    #By Bradley Ayers
    #February 17-18, 2024
        
        #Constants:
        EMAIL_REGEX = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
        UNAME_REGEX = re.compile(r"^([A-Za-z0-9._%+-]+)@")
        DATA_STRING = "Iola Ferguson, (285) 310-6326, enim.commodo.hendrerit@outlook.net, '6298 Quam, Rd.', 72577, Saarland, Belgium, 3, 'orci lacus vestibulum lorem, sit amet ultricies sem magna nec', 6, $19.47, JYZ98EEJ6DD Sheila Strickland, (627) 873-2052, semper@icloud.couk, 189-1527 Ultricies Road, 35367, Swiętokrzyskie, United States, 3, 'Aenean sed pede nec ante blandit viverra. Donec tempus, lorem', 6, $55.05, ZMD65DCH1BJ quis.massa.mauris@yahoo.ca, Pakistan, $38.86 magna.cras@aol.net, Mexico, $75.25 amet.orci@protonmail.edu, Brazil, $3.88 sociis@hotmail.net, Indonesia, $99.28 accumsan@google.ca, Colombia, $46.90 Burke Richard, 1-441-218 1074, volutpat.nunc.sit@hotmail.org, 992-6300 Nibh. Av., 1137, Leinster, Mexico, 13, vitae erat vel pede blandit congue. In scelerisque scelerisque dui., 9, $22.75, RNE32IWM8PC Armand Mccarthy, (507) 444-8334, facilisis.non@icloud.edu, 'P.O. Box 164, 662 Vulputate, Avenue', 8547, Styria, United Kingdom, 9, 'neque sed sem egestas blandit. Nam nulla magna, malesuada vel, ', 1, $60.20, UND33BCY0WR Gretchen Molina, 1-576-912-3003, duis.mi@icloud.ca, Ap #691-2811 Diam. St., 48453-64570, Kaliningrad Oblast, Russian Federation, 7, Nulla facilisi. Sed neque. Sed eget lacus. Mauris non dui, 1, $80.74, TVT63CLW8IT"

        print()
        print("Hello there! Since you chose Option 5, you get to learn about regular expressions in Python!")
        print()
        
        while True:
            if not Whoops("If you accidentally chose Option 5,\ntype END and press return to go back to the main menu.\nOtherwise, press return to continue: "):
                break
        
            #Brief introduction to regex 
            print("Regular expressions, or regex, are a powerful tool used to search for patterns in strings.")
            print()
            print("To use regex, we first need to import the module.")
            print("Do this by typing the following at the top of your script:")
            print()
            print("import re")
            print()
            AnyKey("Press any key to continue.\n ")
            print()
            
            print("Email addresses are used in all three examples.")
            print("They follow a specific format:")
            print("Uppercase or lowercase letters and/or numbers @ website name . suffix")
            print("Let's break down how this looks in regex:")
            print()
            print("r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\\b'")
            print()
            print("It may look complicated, but remember:")
            print("There's no need to memorize, only to understand.")
            print("Let's break this regex into smaller pieces.")
            print()
            AnyKey("Press any key to continue.\n ")
            print()
            
            print("Regex strings start with an r outside the quotation marks.")
            print()
            print("It's important to note that \\ is an escape character in Python,")
            print("meaning it has to be handled properly in code.")
            print("For every \\ displayed in the console, two have to be typed in the string.")
            print()
            AnyKey("Press any key to continue.\n ")
            print()
            
            print("\\b: Word boundary")
            print("[A-Za-z0-9._%+-]+: One or more alphanumeric characters or special characters")
            print("@: Literal @ symbol")
            print("[A-Za-z0-9.-]+: One or more alphanumeric characters or hyphens (for domain)")
            print("\\.: Literal period (escaped)")
            print("[A-Z|a-z]{2,}: Two or more letters (for the top-level domain)")
            print("\\b: Another word boundary")
            print()
            AnyKey("Remember: Practice makes perfect! Press any key to continue.\n ")
            print()
            
            #Example 1: Validating an email address
            print("We will look at three practical use cases for regular expressions.")
            print()
            print("One common use for regex is input validation.")
            print()
            print("You will be prompted to enter an email address below.")
            print("Please enter an incorrectly formatted email address on the first try,")
            print("then try entering a valid one.")
            print()
            
            while True:
                Email = input("Please enter an email address: ")
                print()
                if not EMAIL_REGEX.match(Email):
                    print ("Error: Invalid format for an email address.")
                    print()
                    continue
                else:
                    print("Thank you! Your email address is " + Email)
                    print()
                    break
            
            print("This input statement uses an if/else statement to validate")
            print("user input against the regex pattern for an email address.")
            print("It uses the re function match() to see if the input fits the format.")
            print()
            AnyKey("Press any key to move to the second example.\n ")
            print()
            
            #Example 2: Isolating a specific part of a string
            print("Let's suppose a site wants to automatically assign a user a username.")
            print("That username will simply be the first part of the email address,")
            print("before the @ symbol.")
            print()
            print("Take the email from the first example: " + Email)
            print("How to isolate the part before @?")
            print()
            AnyKey("Press any key to find out!\n ")
            print()
            
            print("Since we have already validated this email, we are going to")
            print("isolate a specific part of it. Our new regex pattern is:")
            print()
            print("r'^([A-Za-z0-9._%+-]+)@'")
            print()
            print("This pattern is similar to the one we used at first, but only goes to @.")
            print()
            AnyKey("Press any key to see how this works.\n ")
            print()
            
            print("Regex patterns are separated into groups based on parentheses.")
            print("The whole expression can be called group(0).")
            print("The user name we want to collect would be group(1),")
            print("the section enclosed in the first set of parentheses ([A-Za-z0-9._%+-]+)")
            print()
            
            Match = re.match(UNAME_REGEX, Email)
            UserName = Match.group(1)
            
            print("The match command is used again, and the username is assigned:")
            print("UserName = Match.group(1)")
            print()
            print("That leaves us with:")
            AnyKey("Drumroll... (press any key)")
            print()
            print("Email: " + Email)
            print("Username: " + UserName)
            print()
            AnyKey("Press any key to move to the final example.\n ")
            print()
            
            #Example 3: Extracting structured data from unstructured sources
            print(DATA_STRING)
            print()
            print("...")
            print()
            print("This is just a relatively small sample of garbled data,\nbut it's still enough to make me happy I can parse through it with regex.")
            print()
            AnyKey("Press any key to see how!\n ")
            print()
            
            print("We can use the same regex pattern we used in our first validation\nto ensure that we only select email addresses from the data.")
            print()
            print("Here we can use the regex function findall")
            print("The code looks like this:")
            print("EmailAdd = re.findall(EMAIL_REGEX, DATA_STRING)")
            print("This will create a list and we can do whatever we want with it!")
            print()
            print("for the purposes of this demo, we are going to use\na for loop to iterate and print one email address per line.")
            print()
            AnyKey("Press any key to see the magic happen.")
            print()
            
            EmailAdd = re.findall(EMAIL_REGEX, DATA_STRING)
            for i in EmailAdd:
                print(i)
            print()
            AnyKey("Ta-da! Press any key to move to the wrap-up.")
            print()
            
            #Conclusion:
            print("Thank you for checking out this tutorial on regular expressions.")
            print("Regex is a powerful tool and this was just a very brief introduction.")
            print("If you'd like to learn more, copy and paste this URL into your browser:")
            print()
            print("https://docs.python.org/3/library/re.html")
            print()
            AnyKey("Press any key to return to the main menu screen.")
            break
    
    elif MenuChoice == "6":
        print("Thank you for using Seal Team Six's Midterm Sprint Program!")
        print("Enjoy the rest of your day and see you next time ^_^")
        print()
        break
    
    elif MenuChoice == "7":
    #I wanted to learn something new (the animation) while reviewing the append function for lists.
    #Brad Ayers
    #February 21, 2024
        
        import time

        Emoji = "(づ｡◕‿‿◕｡)づ"
        Phrase = "Mo is Tiggety-Boo!"
        Frames = []
        Counter = 0
        PhraseCounter = 0

        while Counter < 3:
            Emoji = " " + Emoji
            Frames.append(Emoji)
            Counter += 1
        while 3 <= Counter <= (len(Phrase) + len(Emoji)):
            Frames.append(Phrase[0:PhraseCounter] + Emoji)
            Counter += 1
            PhraseCounter += 1

        for frame in Frames:
                    print("\r" + frame, end="")
                    time.sleep(0.1)
                
        continue
    
    else:
        print("Error: Value must be a number (1 - 6).")
        AnyKey("Press any key to return to the main menu screen.")
        continue