if __name__ =='__main__':
    n = 52
    f = [0] * (n//2 + 1)
    prob = [0] * (n//2 + 1)
    
# fk -> probability that max_payoff >= k
# fk / fk-1 = (n-k+1) / (n+k)
    f[0] = 1
    for i in range(1, n//2 + 1):
        f[i] = (n - i + 1)/(n + i) * f[i-1]
    
# prob(max_payoff == k) = prob(max_payoff >= k) - prob(max_payoff >= k+1)
    for i in range(0, n//2):
        prob[i] = f[i] - f[i+1]
        print('P ( payoff =',i,') = %.15f'%prob[i])
        
    prob[n//2] = f[n//2] - 0
    print('P ( payoff =',n//2,') = %.15f'%prob[n//2])