
nobc = 0 #this is the number of bags checked
vob = 0 #this is the value of the bag
x = 2
y = 1
for i in range(1,9):


   
    vob = 0
    counter1 = input ("enter the first counters name ")
    cointype1 = input ("please enter the type of coin  ")       
    weight1 = int(input("please enter the correct weight of bag ")) 
            
    if cointype1 == "£2":
                if weight1 < 120:
                    print("You have entered the incorrect weight.") 
                    print(120-int(weight1),"grams needed.")
                    #12 gram per £2 coin  
                elif weight1 > 120: 
                    print("You have entered the incorrect weight.") 
                    print(int(weight1) - 120,"grams needed.")
                    #12 gram per £2 coin  
                else:
                    print("You have entered the correct bag weight.")
                accuracy = weight1 / 120
                if accuracy > 1:
                    accuracy = accuracy - 1
                    accuracy = 1-accuracy
                accuracy = accuracy * 100
                nobc = nobc + 1
                vob = vob + 120       
                            


    if cointype1 == "£1":
                        if weight1 < 174:
                            print("You have entered the incorrect weight.") 
                            print(174-int(weight1),"grams needed.")
                        #8.75 gram per £1 coin  
                        elif weight1 > 174: 
                            print("You have entered the incorrect weight.") 
                            print(int(weight1) - 174,"grams needed.")
                        #8.75 gram per £1 coin  
                        else:
                            print("You have entered the correct bag weight.")      
                        accuracy = weight1 / 175
                        if accuracy > 1:
                            accuracy = accuracy - 1
                            accuracy = 1-accuracy
                        accuracy = accuracy * 100
                        nobc = nobc + 1
                        vob = vob + 175

    if cointype1 == "50p":
                        if weight1 < 160:
                            print("You have entered the incorrect weight.") 
                            print(160-int(weight1),"grams needed.")
                        #8 gram per 50p coin  
                        elif weight1 > 160: 
                            print("You have entered the incorrect weight.") 
                            print(int(weight1) - 160,"grams needed.")
                        #8 gram per 50p coin  
                        else:
                            print("You have entered the correct bag weight.")     
                        accuracy = weight1 / 160
                        if accuracy > 1:
                            accuracy = accuracy - 1
                            accuracy = 1-accuracy
                        accuracy = accuracy * 100
                        nobc = nobc + 1
                        vob = vob + 160

    if cointype1 == "20p":
                        if weight1 < 250:
                            print("You have entered the incorrect weight.") 
                            print(250-int(weight1),"grams needed.")
                    #5 gram per 20p coin  
                        elif weight1 > 250: 
                            print("You have entered the incorrect weight.") 
                            print(int(weight1) - 250,"grams needed.")
                    #5 gram per 20p coin  
                        else:
                            print("You have entered the correct bag weight.")     
                        accuracy = weight1 / 250
                        if accuracy > 1:
                            accuracy = accuracy - 1
                            accuracy = 1-accuracy
                        accuracy = accuracy * 100
                        nobc = nobc + 1
                        vob = vob + 250

    if cointype1 == "10p":
                        if weight1 < 325:
                            print("You have entered the incorrect weight.") 
                            print(325 - int(weight1),"grams needed.")
                    #2.35 gram per 5p coin  
                        elif weight1 >325: 
                            print("You have entered the incorrect weight.") 
                            print(int(weight1) - 325,"grams needed.")
                    #2.35 gram per 5p coin  
                        else:
                            print("You have entered the correct bag weight.")              
                        accuracy = weight1 / 325
                        if accuracy > 1:
                            accuracy = accuracy - 1
                            accuracy = 1-accuracy
                        accuracy = accuracy * 100
                        vob = vob + 325
                        nobc = nobc + 1

    if cointype1 == "5p":
                        if weight1 < 235:
                            print("You have entered the incorrect weight.") 
                            print(235 - nt(weight1),"grams needed.")
                    #356 gram per 1p coin  
                        elif weight1 >235: 
                            print("You have entered the incorrect weight.") 
                            print(int(weight1) - 235,"grams needed.")
                    #356 gram per 1p coin  
                        else:
                            print("You have entered the correct bag weight.") 
                        accuracy = weight1 / 235
                        if accuracy > 1:
                            accuracy = accuracy - 1
                            accuracy = 1-accuracy
                        accuracy = accuracy * 100
                        nobc = nobc + 1
                        vob = vob + 235

    if cointype1 == "2p":
                        if weight1 < 356:
                            print("You have entered the incorrect weight.") 
                            print(356-int(weight1),"grams needed.")
                    #2.35 gram per 5p coin  
                        elif weight1 >356: 
                            print("You have entered the incorrect weight.") 
                            print(int(weight1) - 356 ,"grams needed.")
                    #2.35 gram per 5p coin  
                        else:
                            print("You have entered the correct bag weight.")               
                        accuracy = weight1 / 356
                        if accuracy > 1:
                            accuracy = accuracy - 1
                            accuracy = 1-accuracy
                        accuracy = accuracy * 100
                        nobc = nobc + 1
                        vob = vob + 356

    if cointype1 == "1p":
                        if weight1 < 356:
                            print("You have entered the incorrect weight.") 
                            print(356-int(weight1),"grams needed.")
                    #356 gram per 1p coin  
                        elif weight1 >356: 
                            print("You have entered the incorrect weight.") 
                            print(int(weight1) - 356,"grams needed.")
                    #356 gram per 1p coin  
                        else:
                            print("You have entered the correct bag weight.") 
                        accuracy = weight1 / 356
                        if accuracy > 1:
                            accuracy = accuracy - 1
                            accuracy = 1-accuracy
                        accuracy = accuracy * 100
                        nobc = nobc + 1
                        vob = vob + 356
                        
print("the accuracy was " + str(accuracy) + "%" "\n")
print("You've checked" , i, "bags")
print("The amount of weight overall is " , weight1, )

print("You have finished Congratulations!")