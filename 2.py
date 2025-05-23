words = []

while True:
    word = input("Введите слово (или stop для завершения): ")
    if word.lower() == 'stop':
        break
    words.append(word)
result_string = " ".join(words)

print("Итоговая строка:", result_string)
