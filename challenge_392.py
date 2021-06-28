"""
Challenge 392: Pancake sort
Completed: 6/28/21
Link: https://www.reddit.com/r/dailyprogrammer/comments/np3sio/20210531_challenge_392_intermediate_pancake_sort/
"""
def flipfront(ints, num):
    front = 0
    back = num - 1
    while (front <= back):
        temp = ints[front]
        ints[front] = ints[back]
        ints[back] = temp
        front += 1
        back -= 1
    return
    # Could possible be more efficient

def pancake_sort(ints, length):
    flag = True

    #Checks if list is sorted
    for i in range(length - 1):
        if ints[i] > ints[i + 1]:
            flag = False
    if flag:
        print("done")
        return

    #Moves first index to the back
    if ints.index(max(ints[0:length])) == 0:
        flipfront(ints, length)
        pancake_sort(ints, length - 1)

    #Moves highest number to front of list
    else:
        flipfront(ints, ints.index(max(ints[0:length])) + 1)
        pancake_sort(ints, length)

def main():
    ar = [3,6,4,2,3,8,4,56,78,4,2,1]
    pancake_sort(ar, len(ar))
    print(ar)

if __name__ == "__main__":
    main()
