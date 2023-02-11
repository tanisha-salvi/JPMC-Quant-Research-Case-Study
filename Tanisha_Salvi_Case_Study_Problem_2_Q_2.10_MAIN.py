# function to find the expected payoff using the probabilities calculated
# P(payoff = k) 0 <= k <= 26
def find_expected_payoff(prob, n):
    expected_payoff = 0.0
    #expected payoff is the summation of (probability that payoff = k) * k
    for i in range(0, n + 1):
        expected_payoff += i * prob[i]
    return expected_payoff

if __name__ =='__main__':
#  Total number of cards = 2 * n = 52
    n = 26
    f = [0] * (n + 1)
    prob = [0] * (n + 1)
    
#  fk -> probability that max_payoff >= k
#  fk / fk-1 = (n-k+1) / (n+k)
    f[0] = 1
    for k in range(1, n + 1):
        f[k] = (n - k + 1)/(n + k) * f[k-1]
    
#  prob(max_payoff = k) = prob(max_payoff >= k) - prob(max_payoff >= k+1)
    for i in range(0, n):
        prob[i] = f[i] - f[i+1]
        
#  prob(max_payoff > n) = 0
    prob[n] = f[n] - 0

    expected_payoff = find_expected_payoff(prob, n)
    print("The expected payoff =", expected_payoff)