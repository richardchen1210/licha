import numpy as np
def row_op(arr):
    n = arr.shape[0]
    for i in range(n):
        if arr[i][i] !=0:
            arr = redu(arr,i)
            # print("arr",i+1,":\n",arr)
    for i in range(n):
        rgcd = np.gcd.reduce(arr[i])
        # print("rgcd",i+1,"is",rgcd)
        if arr[i][i] !=0 and rgcd != 1:
            arr[i] = arr[i]/rgcd
        if arr[i][i] <0:
            arr[i] = -arr[i]
    return arr

def redu(arr,i):
    n = arr.shape[0]
    # mult1 = arr[(i+1)%3][i]/arr[i][i]
    # print("mult1",mult1)
    # mult2 = arr[(i+2)%3][i]/arr[i][i]
    # print("mult2",mult2)
    for j in range(n-1):
        if arr[(i+1+j)%n][i] != 0:
            arr[(i+1+j)%n] = arr[(i+1+j)%n]*arr[i][i]-arr[i]*arr[(i+1+j)%n][i]
    return arr

def show_ans(arr):
    n = arr.shape[0]
    sol = []
    arr = row_op(arr)
    for i in range(n):
        sol.append(arr[i][-1]/arr[i][i])
    return sol


# data = np.array([[1,1,1,3],[1,2,4,7],[1,1,2,4]])
# data = np.array([[1,-4,2,0],[-3,8,4,2],[-2,8,-4,1]])
# data = np.array([[1,2,-2,-3],[3,-1,4,14],[2,3,-1,2]])
# data = np.array([[1,1,2,2],[2,1,1,2],[1,2,5,4]])
# data = np.array([[1,-2,3,5],[2,-3,5,9],[3,-1,3,8]])
data = np.array([[1,2,5],[2,1,4]])
# data = np.array([[1,2,1,8],[1,-3,-3,1],[3,1,-1,2]])
# data = np.array([[2,3,7],[1,-1,1]])
# data = np.array([[2,3,-4,1,15],[1,-2,3,-2,-3],[3,5,1,-1,20],[4,1,-1,1,5]])
# data = np.array([[1,1,1,1],[1,-1,2,1],[2,-1,2,1]])
# data = np.array([[1,1,1,26],[1,-1,0,1],[2,-1,1,18]])
# print(data)
# print(row_op(data))
print(show_ans(data))