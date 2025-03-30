#20% - has strep throat -- 85% positive, 15% false negatives
#80% - not have strep throat -- 90% negative, 2% false positives
def find_prob(a,b):
    if a == 1:
        prob_a = 0.2
        if b == 1:
            prob_p = 0.85
        else:
            prob_p = 0.15
    if b == 1:
        prob_b = 0.8
        if b == 1:
            prob_p = 0.2
        else:
            prob_p = 0.98            
