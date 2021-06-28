"""
Challenge 393: Making Change
Completed: 6/21/21
link: https://www.reddit.com/r/dailyprogrammer/comments/nucsik/20210607_challenge_393_easy_making_change/
"""

def change(num):
    coins = 0
    count = num
    denoms = [500, 100, 25, 10, 5, 1]
    for denom in denoms:
        if count / denom >= 1:
            coins += count // denom
            count = count % denom
    return coins

def main():
    print("Enter a number (Enter -1 to stop):")
    coins = change(int(input()))
    print("You will recieve " + str(coins) + " coins.")

if __name__ == "__main__":
    main()
