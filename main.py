from csv import reader
from random import randrange


#1
print('Task 1')
count = 0
with open('books-en.csv', 'r') as booktable:
    table = reader(booktable, delimiter=';')
    for row in list(table)[1:]:
        if len(row[1]) > 30:
            count += 1
    print(count)


#2
print('Task 2')
flag = 0
avtor = input('Введите автора книги: ')
with open('books-en.csv', 'r') as booktable:
    table = reader(booktable, delimiter=';')
    for row in list(table)[1:]:
        if row[2] == avtor:
            if row[3] == '2015' or row[3] == '2018':
                flag = 1
                print(row[1], row[2], row[3])
    if flag == 0:
        print('Книг данного автора  не найдено')


#3
bookid = [randrange(0, 9400) for x in range(20)]
with open('books-en.csv', 'r') as booktable:
    table = reader(booktable, delimiter=';')
    row = [x for x in list(table)[1:]]
with open('randombooks.txt', 'w') as randombooks:
    for i in range(20):
        randombooks.write(f'{i+1}. {bookid[i]} {row[bookid[i]][2]} {row[bookid[i]][1]}-{row[bookid[i]][3]}\n')