#print welcome messege
print ("Welcome in our Programme 😊 👋")
print ("----Age in Days Calculator-----")
 
 #Ask User to input his\her ----Age
askAge=input("Enter your age in years: ")
askAge=int (askAge)
oper = askAge * 365
 
 #print the operation 
print (f'You have lived for  {oper}  Days' )
print ("--------------------------------------")
print ("--------------------------------------")
#the second Programme
print("WELCOME IN GUESSING GAME YAAhooo")
# while loop ------ new variablle to count the numbers of tries
count=0
while True :
    
    #Gussing number between 0 and 10
    guess= input ('Guessing number between 0 and 10 : ')
    guess= int(guess)
    count += 1
    
#if input between 0 and 5 too lower
    if guess<=4 :
        print ('   Too Low 😒 🤦!  Try again. ')
        continue
    
    elif guess>4 and guess<8 :
        print ("   Good but not correct 😓 🙃")
        continue
    
    elif guess>=10 : 
        print ("   OPPS!🤦 🤦 It's Too High")
        continue
    
    else :
        print ('   congratulations!👌 ❤️ You guessed the number correctly')
# get out of the loop
        break 

print ("THE SUM OF TRIES : " , count)

print("--------------------------------------")
print("------------------------------------------")
print ("--------------------------------------------")

#the third Programme
# list
adds=[]

# the welcome messege 
print ('Welcome to The TO- DO List App')

#while loop
while True :
   print ("choose an option from : ")
   print ("    1. Add new Task.") #to add new Task
   print ("    2. View Tasks. ")  # to wiew the tasks 
   print ('    3. Delet Task. ')  #to delete  certain task
   print ("    4. EXIT ")         # to getout from programme

#  the user inputs his / her choose
   UserCHoose= int(input ("Enter the number of  your choose (1:4)  :  "))
   
# if --- else  conditions 

   if UserCHoose==1 :
       add= input ("add your task :  ")  # inorder to user input his task
       adds.extend(add)   # to add more Tasks
       print ("    successful addtion ")
       continue 
    
   elif UserCHoose==2 :
       if not adds :
           print("    not found any task🤷️ !Do you want to add your task ?\nClick on num 1! ")
       else :   
           print ('your Tasks :' )
           i=1
           for add in adds :
             print (   i ,    add)
             i+=1
       continue 
    
   elif UserCHoose==4 :
       print ("    Good Bye 👋 ")
       break 
   
   else :
      if not adds :
          print ("    no tasks to delete")
      else :
          i=1
          for add in adds :
            print (i ,adds)
            i+=1
            add_num=input("enter the value of the task that you want to delete it : ")
            
            j=0
            while j<=len(adds):
               if add_num == adds[j] :
              
                  del(adds[j] ) #delete this task
                  print ("the deletion operation is ended successfully.")
                  break
              
               elif add_num!= adds[j] :
                  j+=1
                  
               else :
                   print (" Ohhh, Nooo!This Letter isnot founded.")
                   break
              
            break
print ("--------------------------------------")   
print ("---------------------------------------")   
print ("----------------------------------------")   
print ("------------------------------------------")   
#pro num 4
#this pro for check if this num (input ) is even or odd!
# welcome message
print("This programme to check the number that you entered is even or odd?!")
loop=0
while True :
    user_input=input("enter a num:  ")
    user_input=int (user_input)
    if user_input % 2 == 0 :
        print ("this num is EVEN ")
    else :
        print ('this num is ODD !')
    break
loop+=1
print (loop)
print ("--------------------------------------")   
print ("----------------------------------------")   
print ("------------------------------------------")   
print ("--------------------------------------------")   
print ("----------------------------------------------")   
print ("------------------------------------------------")   
#pro num 5
#this pro is about entering 3 nums and choose the largest among them
# a welcome message 
print ("welcome in our app that check the largest NUM")
#user input  
num1=int (input (" enter the first num : "))
num2=int (input ("enter the second num :  "))
num3=int (input ("enter the third  num :  "))
 
 # if statment for check the largest num between of them
 
if num1<num2 and num2>num3 :
    print ("the largest num is : " , num2)
    
elif num1>num2 and num1>num3 :
    print ("the largest num is : " , num1)
    
else :
    print ("the largest num is :  " , num3)