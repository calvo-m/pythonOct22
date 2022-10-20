books = {'Dostoievsky':('Book B', 'Book A', 'Book C'), 'Kafka':('Book 1', 'Book 2')}

user_author = input("Choose an author: ")
for author, book_collection in books.items():
    if user_author == author:
        print(sorted(book_collection))