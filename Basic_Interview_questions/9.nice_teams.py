def maxPairs(skillLevel, minDiff):
    #print(skillLevel, minDiff)
    # Write your code here
    print(skillLevel)
    arr = list(set(skillLevel))
    print(arr)

    if len(arr) == 1:
        return 0
    i = 0
    answer =0
    while arr[i]+minDiff <= arr[-1]:
        print("in...")
        if (arr[i] + minDiff) in arr:
            answer += 1
            arr.remove((arr[i] + minDiff))
        i += 1

    return answer


skillLevel=[1,2,3,4,5,6]
minDiff=4

skillLevel= [709552565, 473251358, 803612259, 579542802, 183012194, 689345248, 151290765, 123232501, 994391793, 25107191, 862726097]
minDiff = 440987423
skillLevel = [690726610, 893005429, 771998092, 23203911, 732048773, 609897342, 605163057, 492930001, 830083522, 952945114]
minDiff =763949691

print(skillLevel)
skillLevel.sort()
print(skillLevel)
#print(maxPairs(skillLevel, minDiff))
for i in skillLevel:
    if (i+minDiff) in skillLevel:
        print(i)