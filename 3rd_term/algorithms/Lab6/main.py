###   haystack початковий рядок
###   needle рядок для перевірки циклічного зсуву

# Формуємо таблицю префікс-функції
# повертає сформований массив префікс-функції
def prefix(s: str):
    result = [0] * len(s)  # массив в який записується префікс-таблиця
    prefix_length = 0  # індекс для суфікса

    for i in range(1, len(s)):

        while prefix_length > 0 and s[prefix_length] != s[i]:  # якщо символи на відповідних індексах не зберігаються
            prefix_length = result[prefix_length - 1]  # то ми робимо відступ

        if s[prefix_length] == s[i]:  # якщо символи на відповіхних індексах збігаються то ми збільшуємо prefix_length
            prefix_length += 1  #

        result[i] = prefix_length  # заповнення таблиці відповідними індексами
    return result



"Алгоритм Кнута-Морріса-Пратта"
# Функція повертає позицію на якій відбувається повний збіг, якщо
# збігу не відбувається, то повертає -1, приймає на вхід порівнюванні рядки.
def kmp(needle: str, haystack: str) -> int:
    index = -1
    pi = prefix(needle)  #  побудова префукс-функції
    coincidence = 0

    for i in range(len(haystack)):

        #. Поки coincidence > 0 і needle[coincidence] != haystack[i], записуємо coincidence = pi[coincidence - 1]
        while coincidence > 0 and needle[coincidence] != haystack[i]:
            coincidence = pi[coincidence - 1]

        # Порівняти символи needle[coincidence] і haystack[i]. Якщо символи рівні, збільшити coincidence на 1
        if needle[coincidence] == haystack[i]:
            coincidence = coincidence + 1

        #  входження зразка needle в рядок haystack знайдено
        if coincidence == len(needle):
            index = i - len(needle) + 1  # запис шуканої позиції(індексу)
            break
    return index


#
def check(haystack: str, needle: str) -> bool:
    # якщо рядки різної довжини - повертає False
    if len(haystack) != len(needle):
        return False
    # якщо строки "пусті" - повертає True
    if len(haystack) == len(needle) == 0:
        return True

    # подвоєння строки для використання використання алгоритму КМП "на пряму"
    haystack += haystack

    # якщо функція kmp повертає запис шуканої позиції, то зсув є повертає True, інакше False
    if (kmp(needle, haystack)) != -1:
        return True
    else:
        return False

"Функція demo створення для демонстрації можливостей програми"
def demo():
    print("Start demo")
    while True:
        haystack = input("Enter string:")  # початковий рядок
        needle = input("Enter a string to check:")  # рядок для перевірки циклічного зсуву
        "вихід з demo"
        if haystack == '!':
            break
        if needle == '!':
            break

        print(check(haystack, needle))  # вивід для перевірки циклічного зсуву

    print('End of demo')


if __name__ == '__main__':
    demo()
