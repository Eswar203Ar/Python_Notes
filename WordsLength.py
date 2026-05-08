## Display words from list whose length is minimum 5 using filter()
words = ["java", "python", "html", "css", "javascript", "sql"]
result = list(filter(lambda word: len(word) >= 5, words))
print(result)