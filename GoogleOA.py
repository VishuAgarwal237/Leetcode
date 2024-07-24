
def sol(clients):

    N = len(clients)
    arr = [None] * N 
    last_added = -1
    for i in range(N):
        if clients[i] not in arr:
            for j in range(len(arr)):
                if arr[j] == None:
                    arr[j] = clients[i]
                    last_added = j + 1
                    break
        else:
            for j in range(len(arr)):
                if arr[j] == clients[i]:
                    arr[j] = None
                    break
    return last_added


def sol1(A, B):

    max_diff = 0
    currMax = A[0]
    currMin = A[0]
    current = B[0]
    for i in range(1, len(B)):
        if B[i] == current:
            currMin = min(currMin, A[i])
            currMax = max(currMax, A[i])
            max_diff = max(max_diff, currMax - currMin)
        else:
            current = B[i]
            currMin = A[i]
            currMax = A[i]
        print(currMax)
    print(max_diff)




if __name__ == "__main__":
    print(sol(["Alice", "Eve", "Bob", "Eve", "Carl", "Alice"]))
    print(sol(["Alice", "Bob", "Bobby"]))

    sol1([60, 100, 90, 80], ["Low", "High", "High", "High"])