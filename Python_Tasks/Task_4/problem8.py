# Problem 8: What's Your Name?
# HackerRank: https://www.hackerrank.com/challenges/whats-your-name/problem

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]
    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)