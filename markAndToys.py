def maximumToys(prices, k):
    sorted_price=sorted(prices)
    sorted_list = [i for i in sorted_price  if i<k]
    print(sorted_list)
    num_toys=0
    sum_prices=0

    for i in range(len(sorted_list)):
        if sum_prices+sorted_price[i]<=k:
            sum_prices+=sorted_price[i]
            print(sum_prices)
            num_toys+=1
        else:
            return num_toys
    return num_toys

a=[1,12,5,111,200,1000,10]

print(maximumToys(a,50))