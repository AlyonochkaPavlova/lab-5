N = int(input("Введите количество слов: "))
words = []

for i in range(N):
    word = input(f"Введите слово #{i + 1}: ")
    words.append(word)
result_string = " ".join(words)

print("Итоговая строка:", result_string)
