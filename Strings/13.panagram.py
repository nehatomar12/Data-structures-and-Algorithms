
# Panagram: if sentence contain all 26 aplhabets
# Lipogram: if any letter is missing...etc
# Pangrammatic Lipogram: if it contain all letter except one letter

check_panagram = "The quick brown fox jumps over the lazy dog"
check_panagram = "The quick brown fox jumps over the  dog"


def panagram_check(check_panagram):
    alphabets = [0] * 26
    for i in check_panagram:
        if i != " ":
            i = i.lower()
            index = ord(i)-ord('a')
            alphabets[index] += 1

    if 0 not in alphabets:
        print("given sentence is panagram")
    else:
        cnt = 0
        for i in range(len(alphabets)):
            if alphabets[i] == 0:
                cnt += 1
                missing_letter = chr(ord('a') + i)
                print(("Missing elements: ",missing_letter))
        print(cnt)
        if cnt == 1:
            print("Sentence is Pangrammatic Lipogram")
        else:
            print("Sentence is not Pangrammatic Lipogram")


panagram_check(check_panagram)