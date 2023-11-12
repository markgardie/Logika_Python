from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/about_me')
def about_me():
    return "My name is Marks"


my_shelf = dict()

while True:
    author = input('Введіть автора (q - завершити):')
    if author == 'q':
        break
    books = list()    
    while True:
        book = input('Введіть книгу (s - стоп):')
        if book == 's':
            break
        books.append(book)
    my_shelf[author] = books
 
for author in my_shelf:
   print(author, '-', my_shelf[author])



