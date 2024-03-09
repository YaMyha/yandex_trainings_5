def b():
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    prices_len = len(prices)

    if prices_len == 1:
        print(0)
    else:
        max_diff = prices[1] - prices[0]
        for i in range(prices_len-1):
            purchase_price = prices[i]
            if i < prices_len-k:
                for j in range(i+1, i+k+1):
                    curr_diff = prices[j] - purchase_price
                    if curr_diff > max_diff and j-i <= k:
                        max_diff = curr_diff
            else:
                for j in range(i, prices_len):
                    curr_diff = prices[j] - purchase_price
                    if curr_diff > max_diff and j-i <= k:
                        max_diff = curr_diff

        if max_diff <= 0:
            print(0)
        else:
            print(max_diff)


if __name__ == "__main__":
    b()