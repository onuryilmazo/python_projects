from textblob import TextBlob
words = ["Data Scence", "Mahine Learnin", "fıck"]
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")
print("\nja ich liebe dich")