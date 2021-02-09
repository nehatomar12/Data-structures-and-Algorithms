# Wacky Workouts
# https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/angry-neighbours/

'''
SAMPLE INPUT  SAMPLE OUTPUT 
2               3
3               5


'''
# store = []
# res = []
# def cal_workout_days(n, store):
    
#     if n in (1, 0):
#         res = 1
#     elif n == 2:
#         res = n
#     else:
#         res = cal_workout_days(n-1, store) + cal_workout_days( n-2, store)
    
#     store[n] = res
#     print(store)
#     return res

# print(cal_workout_days(3,store))

saved = [0,1]
def list_dp_fib(n):
    while len(saved) < n+1:
        saved.append(0)
    if n <= 1:
        return n

    if saved[n-1] == 0:
        saved[n-1] = list_dp_fib(n-1)
    if saved[n-2] == 0:
        saved[n-2] = list_dp_fib(n-2)
    
    saved[n] = saved[n-1] + saved[n-2]
    return saved[n]

print((list_dp_fib(4+2)))
#print(saved[2+2])