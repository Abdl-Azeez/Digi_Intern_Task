# First Task in Section 2
def Task1():
    for i in range (1,100):  #range 1 to 100 is used in order to make the loop start from 1 and not 0
        if ((i%5==0) or (i%3==0)): 
            print (i)
        


# Second Task in Section 2
def findHCF(num, arr):
    #Find the HCF using the Euclidean Algorithm
    x=arr[0]  
    y=arr[1]
    
    def GCD(x, y): #Function is created to set the value x to y if y is not equals to zero
        while (y!=0): 
            x,y = y, x%y
        return x

    gcd = GCD(x,y) #Calling the function to change the values
    y= len(arr)

    for i in range(2,y):
        gcd= GCD(gcd,arr[i])
    
    # Check for the positive numbers, if it correspond with the positive given by the user
    positiveNumb=0
    for i in range (len(arr)):
        if arr[i]>=0:
            positiveNumb+=1
    if (positiveNumb == num):
        return ("The HCF is  ",gcd)
    else:
        return ("\nCheck the sum of positive numbers given")



# Third Task in Section 2
def Task3():
    StrToCheck= str(input("Enter the string to check :  "))
    
    ReverseStr=(StrToCheck[::-1])
    
    if (ReverseStr.lower()==StrToCheck.lower()):
        return True, StrToCheck , " is Palindrome to", ReverseStr
    else:
        return ReverseStr,"  is not Palindrome to ",  StrToCheck 
    

#Print the value between 1-100 that are multiple of 3 and 5 respectively
Task1()

#Print the HCF of numbers
print (findHCF(5, [2, 4, 6, 8, 10]))
    
#Check for Palindrome
print (Task3())
    



