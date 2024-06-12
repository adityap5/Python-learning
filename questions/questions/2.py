#1 print natural numbers upto n

n = int(input("enter a number : "))

# for i in range(1,n+1):
#     print(i)

#2. reverse for loop from n to 1
# for i in range(n,0,-1):
#     print(i)

#3 take a number and print its table

# for i in range(1,11) :
#     print(n*i)
    
    
#4. factorial
# sum = 1
# for i in range(1,n+1,1):
#     sum = sum * i
# print(sum)    

#5. factors

# for i  in range(1,n+1):
#     if n%i == 0: 
#         print(i)
 
#6. Strong Number
# sum = 0
# for i  in range(1,n+1):
#     if n%i == 0 and  i !=n:
#         sum = sum + i
# if sum == n:
#     print(f"{n} is a strong number")
# else: print(f"{n} is not a strong number")   


#7. Prime Number
# count =0
# for i in range(1,n+1):
#     if n%i == 0 :
#         count = count + 1
# if count == 2:
#     print(f"{n} is a prime number")
# else: print(f"{n} is not a prime number")            

#8. Seprate each digit of a number and print it on the new line

# while n >0 :
#     print(n%10)
#     n =n//10

#9. Accept a number and check if it is a pallindromic number 
# copy = n
# reverse = 0
# while n > 0:
#     check =n%10
#     reverse = reverse *10 + check
#     n = n//10
# if reverse == copy:
#     print(f"{copy} is pallindromic number")
# else : print(f"{copy} is not a pallindromic number")   

#10. Right Triangle star

for i in range(n+1 ):
    for j in range(i):
        print("*",end=" " )
    print(" ") 
