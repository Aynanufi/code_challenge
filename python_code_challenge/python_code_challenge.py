#Budget Plan for Tayo and Sola
#1. Finding out how much Tayo makes monthly

print("How much do you make monthly, Tayo?") #Asks Tayo how much he makes monthly
x=input('Salary: ') #Tayo will write how much he makes monthly

print(x + ' is a good plan') 

#a. Take whatever Tayo has put in and determine how much he has saved for 5 years

tayoSalary= float(x) #taking the input Tayo made and assigning it to Salary
tayosMonthlySavings= float(0.25) #rounded this to a decimal point
tayosTime= 60 #the number of months in 5 years

tayoSavings = tayoSalary * tayosMonthlySavings * tayosTime #saving the whole of salary, monthlysavings, and time into savings 


print('You saved ' + str( tayoSavings ) + ' over 5 years')


#Sola's plan
#2. Finding out how much Sola charges per project

print("How much do you charge per project, Sola?")
y=input('Salary: ') #Sola will write how much she charges per project

#a Take whatever sola has input in and determine how much she has saved for 2 years

solaSalary= float(y) #taking the input Sola made and assigning it to solaSalary
solaMonthlySavings= float(0.35) #rounded this to a decimal point
solasTime= 24 #the number of months in 2 years

#saving the whole of salary, monthlysavings, and time into savings
solaSavings = solaSalary * solaMonthlySavings * solasTime  

print('You saved ' + str( solaSavings ) + ' over 2 years')

#3Finding the total budget of the couple
# Where total budget is the sum of the savings of the couple

totalBudget= solaSavings+tayoSavings 

print('Your total budget is ' + str(totalBudget) + ' ')

#4.Calculating the budget for the wedding if rent = 2000000 and couple wants 20% of current savings left
rent= float(2000000)
newSavings= float(0.2)

if rent==2000000:
    budgetForWedding = newSavings*totalBudget - rent
    print (str (budgetForWedding) + ' is the budget for your wedding if you are having 20% of your current savings left')

    
#5 checking if budget will cover mummy Sola's list using an if statement

list= 7150000
if budgetForWedding > list:
    print('Your budget can cover the extraneous expenses')

elif budgetForWedding < list:
    print('Your budget cannot cover your mother\'s list, Sola.')


#6 Reading the file from the invite list 
guest = '\\Users\\IFUNANAYA-PC\\Downloads\\invite_list.txt' 
file = open(guest, 'r')
guestVipList=file.read()
print(guestVipList) #this will print out the guest list for the couple to see

#count the number of words of the invite list by passing the file name to the program and scanning the file to print out the count
word_count = 0  
with open('\\Users\\IFUNANAYA-PC\\Downloads\\invite_list.txt','r') as file:
    for line in file: #using a for loop
        word_count += len(line.split()) #using a split method to return a list of the words and get the count of all words by using the len method
    print ('The number of people on the invite list that are getting aso ebi are: ', word_count)
    print(word_count)

    #using the count method to count the number of times Ajayi and Thomas occured in the file
    #subtract others from ajayi and thomas and get the rest of the people on the invite list
    #do the calculations by multiplying the cost of asoebi for each house
    #print
    #close opened txt file
ajayi=guestVipList.count('Ajayi') 
thomas=guestVipList.count('Thomas') 
others = word_count - ajayi - thomas
whiteAsoebi = 50000 * ajayi
blueAsoebi = 45000 * thomas
greenAsoebi = 40000 * others
print('The Ajayis are ' + str(ajayi) + ', their color of asoebi is white, and the cost of asoebi is ' + str(whiteAsoebi))
print ('The Thomases are ' + str(thomas) + ', their color of asoebi is blue, and the cost of asoebi is ' + str(blueAsoebi))
print ('The rest', others , 'VIPS who are not family members will be getting the green asoebi, and the cost of asoebi is', greenAsoebi )

file.close()
