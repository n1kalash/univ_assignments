# АЛГОРИТМИ ТА СКЛАДНІСТЬ. 1 СЕМЕСТР. ЗАДАЧІ
 
1. Реалізуйте багатофазне сортування злиттям.

2. Нехай є n болтів різного розміру та n відповідних гайок. Припустимо, можна  порівнювати, чи підходять гайка і болт одне до одного, або гайка більша (чи менша). Порівняти між собою дві гайки чи два болти неможливо. Розробіть і реалізуйте алгоритм розбивки всіх гайок і болтів на відповідні пари за час ?(n log n).

3. d-арні піраміди схожі на бінарні, лише їх вузли, відмінні від листя, мають не по 2, а по d дочірніх елементів. Представте d-арну піраміду у вигляді масиву (якою буде її висота для n елементів?). Розробіть ефективні реалізації процедур Extract_Max, Insert та Increase_Key, призначених для роботи з d-арною незростаючою пірамідою. Проаналізуйте час роботи цих процедур і виразіть їх в термінах n та d.

4. Нехай маємо масив, що містить n записів з даними для сортування, і що ключ кожного запису приймає значення 0 або 1. Алгоритм для сортування такого набору записів повинен мати деякі з трьох наступних характеристик: 1) час роботи алгоритму О(n); 2) алгоритм має бути стійким; 3) сортування проводиться на місці, тобто крім вихідного масиву використовується додаткова пам’ять, що не перевищує деякої постійної величини. Розробіть і реалізуйте алгоритм, що задовольняє a) критеріям 1 і 2. b) критеріям 1 і 3. c) критеріям 2 і 3 (бажано з найкращим часом). (кожен пункт 2 бали)

5. Реалізуйте алгоритм Штрассена для множення матриць. На практиці алгоритм починає застосовуватися для матриць такого розміру, коли з'являється виграш порівняно з класичним способом на основі означення, який використовується для матриць меншого розміру. Спробуйте експериментально визначити цю "точку перетину" для свого комп'ютера.

6. Розробіть алгоритм, який за лінійний час визначав би, чи є текстовий рядок Т циклічним зсувом іншого рядка Т* (наприклад, abc та cab).

7. Узагальніть метод Рабіна-Карпа пошуку зразка в текстовому рядку так, щоб він дозволив розв’язати задачу пошуку заданого зразка розміром m на m у символьному масиві розміром n на n. Зразок можна рухати по горизонталі та вертикалі, але не обертати.

8. Реалізуйте алгоритми пошуку зразка в текстовому рядку: наївний, Хорспула, Боєра-Мура, КПМ та Рабіна-Карпа і порівняйте їх ефективність. Виконайте пошук зразків різної довжини: випадкового бінарного зразка у випадковому бінарному тексті та випадкового слова у природному тексті на цій мові.
