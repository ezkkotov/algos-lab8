"""
### Задача 1: Средние расходы по семестрам  
Джон записал свои ежемесячные расходы за прошлый год:  
```python
monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
```  
Напишите программу, которая с помощью цикла `for` вычисляет средние расходы Джона за первый семестр (январь–июнь) и второй семестр (июль–декабрь).  

monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
first_sum = 0
second_sum = 0
for month in range(12):
    if month < 6:
        first_sum += monthly_spending [month]

else: second_sum += monthly_spending [month]

first_sum_average = first_sum / 6
second_sum_average = second_sum / 6

print(f"РАСХОДЫ ЗА ПЕРВЫЙ СЕМЕСТР:{first_sum:.2f}")
print(f"РАСХОДЫ ЗА ВТОРОЙ СЕМЕСТР:{second_sum:.2f}")


### Задача 2: Кто тратил больше? 
У Джона есть друг Сэм, который также записал свои ежемесячные расходы за прошлый год:  
```python
john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]  
sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]
```  
Напишите программу, которая сравнивает расходы Джона и Сэма по месяцам и подсчитывает количество месяцев, в которых Джон тратил больше.  

john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]  
sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]
total_spending_john = sum(john_monthly_spending)
total_spending_sam = sum(sam_monthly_spending)

if total_spending_john > total_spending_sam:
    print(f"Джон потратил больше: {total_spending_john:.2f} против {total_spending_sam:.2f}")
elif total_spending_john < total_spending_sam:
    print(f"Сэм потратил больше: {total_spending_sam:.2f} против {total_spending_john:.2f}")
else:
    print(f"джон и сэм потратили одинакова: {total_spending_john:.2f}")


### Задача 3: Список друзей  
У Пола и Тины есть списки друзей:  
```python
paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
tina_friends = ["Tim", "Susan", "Mary", "Josh"]
```  
Объедините оба списка в один, исключив дублирующиеся имена.  

paul_friends = ["Mary", "Tim", "Mike", "Henry"]
tina_friends = ["Tim", "Susan", "Mary", "Josh"]

combined_friends = list(set(paul_friends) | set(tina_friends))
print(combined_friends)



### Задача 4: Общие друзья  
Используя те же списки друзей Пола и Тины, напишите программу, которая с помощью цикла находит их общих друзей.  

paul_friends = ["Mary", "Tim", "Mike", "Henry"]
tina_friends = ["Tim", "Susan", "Mary", "Josh"]
common_friends = []

for friend in paul_friends:
    if friend in tina_friends:
        common_friends.append(friend)

print("общие друзьяшки:", common_friends)



### Задача 5: Игроки в баскетбол  
В спортивном клубе зарегистрированы игроки:  
```python
football_players = {"Eve", "Tom", "Richard", "Peter"}  
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}  
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}
```  
Напишите программу, которая определяет игроков, зарегистрированных только в баскетболе (не в футболе и не в волейболе).  

football_players = {"Eve", "Tom", "Richard", "Peter"}  
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}  
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}


### Задача 6: Подсчёт голосов  
Результаты опроса о любимом языке программирования:  
```python
poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]
```  
Используя словарь, подсчитайте количество голосов за каждый язык.  
poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]

vote_count = {}
for language in poll_results:
    if language in vote_count:
        vote_count[language] += 1
    else:
        vote_count [language]  = 1

print (vote_count)

### Задача 7: Подсчёт очков  
Три друга играют в игру, где каждый игрок зарабатывает очки в трёх раундах. Их результаты:  
```python
scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('Tom', 8), ('Tom', 9), ('Tom', 8)]
```  
Создайте словарь, где ключами будут имена игроков, а значениями — их суммарные очки.  
scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('Tom', 8), ('Tom', 9), ('Tom', 8)]
total_scores = {}

for name, score in scores:

    if name in total_scores:
        total_scores[name] += score
    else:
        total_scores[name] = score

print(total_scores)

---


### Задача 8: Статистика списка  
Дан список чисел:  
```python
numbers = [10, 3, 5, 9, 18, 3, 0, 7]
```  
Напишите функцию, которая возвращает максимальное значение, сумму и среднее арифметическое чисел в списке.  
numbers = [10, 3, 5, 9, 18, 3, 0, 7]
max_value = max(numbers)
total_sum = sum(numbers)
average = total_sum / len(numbers)
print(f"максимальное значение: {max_value}")
print(f"сумма: {total_sum}")
print(f"среднее арифмитическое: {average}")

---

### Задача 9: Длинные и короткие слова  
Дан список слов:  
```python
word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]
```  
Напишите программу, которая определяет самое длинное и самое короткое слово в списке.  
word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]
longest_word = max(word_list, key=len)
shorted_word = min(word_list, key=len)
print(f"самое длинное слово: {longest_word}")
print(f"самое короткое слово: {shorted_word}")
---

### Задача 10: Фильтрация по частоте  
Дан список чисел:  
```python
number_list = [5, 8, 2, 7, 3, 5, 6, 9, 2, 4, 8, 7, 1, 5, 3]
```  
Создайте новый список, содержащий только числа, которые встречаются в оригинальном списке не менее трёх раз.  
from collections import Counter
number_list = [5, 8, 2, 7, 3, 5, 6, 9, 2, 4, 8, 7, 1, 5, 3]
counter = Counter(number_list)
fitlerd_list = [num for num, count in counter.items() if count >= 3]
print(fitlerd_list)
---
### Задача 11: Второй лучший результат  
Дан список результатов экзамена:  
```python
exam_results = [23, 78, 96, 32, 53, 67, 23, 98, 33, 38, 45, 39, 86, 12, 43, 45]
```  
Напишите программу, которая определяет второй по величине результат в списке.  
exam_results = [23, 78, 96, 32, 53, 67, 23, 98, 33, 38, 45, 39, 86, 12, 43, 45]
exam_results.sort()
print("второй по величине=", exam_results[-2])
