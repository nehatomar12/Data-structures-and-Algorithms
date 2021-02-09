"""
Given arrival and departure times of all trains that reach a railway station,
the task is to find the minimum number of platforms required for the
railway station so that no train waits.

Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
Explantion: There are at-most three trains at a time (time between 11:00 to 11:20)


"""

def approach_1(arrive, depart):
    result = 1
    for i in range(len(arrive)):
        min_plat = 1
        for j in range(i+1, len(arrive)):
            # cond1: arrive = [950, 940] depart = [1130, 1120]
            # cond2: arrive = [940, 950] depart = [1120, 1130]
            if (arrive[i] >= arrive[j] and arrive[i] <= depart[j]) or (
                    arrive[j] >= arrive[i] and arrive[j] <= depart[i]):
                min_plat += 1
        result = max(result, min_plat)

    print(result)


def approach_2(arrl, exit):
    arrl.sort()
    exit.sort()

    guests_in = 1
    max_guests = 1
    time = arrl[0]
    i = 1
    j = 0
    n = len(arrl)

    while (i < n and j < n):
        if (arrl[i] <= exit[j]):
            guests_in = guests_in + 1
            if(guests_in > max_guests):
                max_guests = guests_in
                time = arrl[i]
            i = i + 1
        else:
            guests_in = guests_in - 1
            j = j + 1

    print("Maximum Number of Guests =",
          max_guests, "at time", time)



    # Time complexity O(nlogn)

if __name__ == "__main__":
    arrive = [900, 940, 950, 1100, 1500, 1800]
    depart = [910, 1120, 1130, 1200, 1900, 2000]
    arrl = [1, 2, 10, 5, 5]
    exit = [4, 5, 12, 9, 12]
    approach_2(arrl,exit)
    approach_1(arrl,exit)


"""
# while i < len(arrive) and j < len(arrive):
    #     # cond1: arrive = [950, 940] depart = [1130, 1120]
    #     if arrive[j] <= depart[i]:
    #         # Train still at platform. need more platform
    #         need_platform += 1
    #         j += 1
    #     # cond2: arrive = [940, 1020] depart = [950, 1120]
    #     #elif arrive[j] >= depart[i]:
    #     else:
    #         # Train left before arrival of next train platform is empty
    #         need_platform -= 1
    #         i += 1
    #     result = max(result, need_platform)
    #     print(result, r)


"""
