# recursive function to generate all possible configurations
def generate_configurations(size, red, black, temp):
    # when all cards are drawn, we add configuration to list     
    if red == 0 and black == 0:
        options.append(temp)
        return
    if red > 0:
        generate_configurations(size, red - 1, black, temp + ['R'] )
    if black > 0:
        generate_configurations(size, red , black - 1, temp + ['B'] )

# function to evaluate maximum possible payoff for any given configuration 
def generate_maxpay(temp):
    cur_max = 0
    cur = 0
    for i in temp:
        # for every R draw, player gets +1, for every black draw, player gets -1         
        if i == 'R':
            cur = cur + 1
        else :
            cur = cur - 1
        # always selecting maximum payoff since user plays optimally         
        cur_max = max(cur, cur_max)
    return cur_max

# function to calculate expected payoff for possible configurations
def calculate_expected_payoff(freq_payoff, total):
    # using concept that E(x) = summation of xi * P(xi) 
    expected_ans = 0.0
    for i in range(0, len(freq_payoff)):
        expected_ans = expected_ans + (i * freq_payoff[i] / total)
    return expected_ans
    
#the main function for calling required functions   
if __name__ =='__main__':
    n = 4
    red = n
    black = n
    count = 0
    temp = []
    options = []
    freq_payoff = [0]* (n + 1)
    generate_configurations(2*n, red, black, temp)
    
    #number of possible configurations is the size of list of configurations
    count = len(options)
    print ("Total cards =", n, "with", n , "red", "and", n , "black cards.")
    print ()
    print ("Total number of configurations : ", count)
    
    for temp in options:
        cur_pay = generate_maxpay(temp)
        #printing configuration along with its respective maxmimum payoff         
        print (temp, " -> ", cur_pay)
        #frequency of each possible payoff is maintained in freq array
        freq_payoff[cur_pay] += 1
    expected_payoff = calculate_expected_payoff(freq_payoff, count)
    print ()
    print ("The expected payoff for possible stated configurations =", expected_payoff)