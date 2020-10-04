def prefix(s: str):
    result = [0] * len(s)
    prefix_length = 0

    for i in range(1, len(s)):

        while prefix_length > 0 and s[prefix_length] != s[i]:
            prefix_length = result[prefix_length - 1]

        if s[prefix_length] == s[i]:
            prefix_length += 1

        result[i] = prefix_length
    return result


def kmp(needle: str, haystack: str) -> int:
    index = -1
    pi = prefix(needle)
    coincidence = 0
    for i in range(len(haystack)):
        while coincidence > 0 and needle[coincidence] != haystack[i]:
            coincidence = pi[coincidence-1]

        if needle[coincidence] == haystack[i]:
            coincidence = coincidence + 1

        if coincidence == len(needle):
            index = i - len(needle) + 1
            break
    return index


def check(haystack: str, needle: str) -> bool:
    if len(haystack) != len(needle) or needle < '':
        print("Finita la commedia")
        return False

    haystack += haystack

    if (kmp(needle, haystack)) != -1:
        print("Cycle")
        return True
    else:
        print("Not cycle")
        return False


def demo():
    print("Start demo")
    while True:
        haystack = input("Enter string:")
        needle = input("Enter a string to check:")

        if haystack == '!':
            break
        if needle == '!':
            break

        print(check(haystack, needle))

    print('End of demo')


if __name__ == '__main__':
    demo()
