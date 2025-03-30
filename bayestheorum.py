#20% - has strep throat -- 85% positive, 15% false negatives
#80% - not have strep throat -- 90% negative, 2% false positives
def find_prob(a,b):
    if a == 1:
        prob_a = 0.2
        if b == 1:
            prob_p = 0.85
        else:
            prob_p = 0.15
        prob_a_and_b = prob_a * prob_p
        print("probability of both events occuring is: ", prob_a_and_b)   
   
    if a == 2:
        prob_b = 0.8
        if b == 1:
            prob_p = 0.2
        else:
            prob_p = 0.98            
        prob_a_and_b = prob_b * prob_p
        print("probability of both events occuring is: ", prob_a_and_b) 


print("Person has strep throat? \n 1.Yes \n 2. No")
a = int(input("Enter 1 or 2: "))        

print("Person has tested positive for strep throat? \n 1.Yes \n 2. No")
b = int(input("Enter 1 or 2: "))

print("Probability of a and b occuring is:")
find_prob(a,b)