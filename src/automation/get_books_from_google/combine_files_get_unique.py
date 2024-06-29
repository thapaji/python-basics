import json

# List of input files
input_files = ['1.json', '2.json', '3.json', 'books.json']

# Dictionary to keep track of unique ISBNs
unique_books = {}

# Read and combine data from all input files
for file_name in input_files:
    with open(file_name, 'r', encoding='utf-8') as file:
        books = json.load(file)
        for book in books:
            isbn = book.get('isbn')
            if isbn and isbn not in unique_books:
                unique_books[isbn] = book

# Get the combined list of books
combined_books = list(unique_books.values())

# Write the combined data to new.json
output_file = 'new.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(combined_books, file, ensure_ascii=False, indent=2)

print(f'Combined data exported to {output_file}')
