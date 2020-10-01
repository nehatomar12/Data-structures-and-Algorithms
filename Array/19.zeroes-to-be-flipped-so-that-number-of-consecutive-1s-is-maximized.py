"""
Input:   arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
         m = 2
Output:  5 7

Steps:
    Maintain variables to check currentwindow and bestwindow(bestWindow, bestL, wL, wR)
    1. create a window which have k zeros(expand wR)
    2. once window is formed update bestwindow and bestL
    3. Now slide the window to right, updating wL
"""

arr = [0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0]
k = 60

wL = wR = 0
bestWindow = bestL = 0
currentZeros = 0

while wR < len(arr):
    # Step1
    if currentZeros <= k:
        if arr[wR] == 0:
            currentZeros += 1
        wR += 1
    # step3
    elif currentZeros > k:
        if arr[wL] == 0:
            currentZeros -= 1
        wL += 1

    # step2
    if (wR-wL) > bestWindow and currentZeros <= k:
        bestWindow = wR - wL
        bestL = wL

total_ones = 0
for i in range(bestL, bestWindow):
    if arr[i] == 0:
        print(i, end=" ")
print("Total ones: ", bestWindow)
