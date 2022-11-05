books = [
("почему.", 200),
("так",  250),
("сложно",  500),
("а, не легко", 190)
]
file = open("out.bin", "wb")
import pickle
pickle.dump(books, file)
file = open("out.bin", "rb")
bs = pickle.load(file)
print( bs )
import pickle

book1 = ["почему", 200]
book2 = ["так", 250]
book3 = ["сложно.", 500]
book4 = ["а, не легко", 190]

try:
    file = open("out.bin", "wb")

    try:
        pickle.dump(book1, file)
        pickle.dump(book2, file)
        pickle.dump(book3, file)
        pickle.dump(book4, file)

    finally:
        file.close()

except FileNotFoundError:
    print("Невозможно открыть файл")
    file = open("out.bin", "rb")
    b1 = pickle.load(file)
    b2 = pickle.load(file)
    b3 = pickle.load(file)
    b4 = pickle.load(file)



    print(b1, b2, b3, b4, sep="\n")



