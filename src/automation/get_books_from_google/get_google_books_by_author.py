import requests
import json

# List of categories to fetch books for
categories = [
    'Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery',
    'Thriller', 'Romance', 'Biography', 'History', 'Science',
    'Self-Help', 'Children\'s Books', 'Young Adult', 'Poetry',
    'Art', 'Travel', 'Religion', 'Philosophy', 'Cooking', 'Health and Fitness'
]

# List of authors to fetch books for
authors = [
    'Tony Robbins', 'William Shakespeare', 'Fyodor Dostoyevsky',
    'Neal Shusterman', 'Lisa Manifold', 'Albert Camus', 'Lisa Zunshine'
]

# Base URL for Google Books API
base_url = 'https://www.googleapis.com/books/v1/volumes'


def fetch_books(query, is_author=False, max_results=5):
    """
    Fetches books from Google Books API for a given query (category or author).
    Returns a list of dictionaries representing books.
    """
    url = f'{base_url}?q={"inauthor" if is_author else "subject"}:{query}&maxResults={max_results}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('items', [])
        books = []
        for item in data:
            volume_info = item.get('volumeInfo', {})
            book = {
                "title": volume_info.get('title', 'Unknown'),
                "author": volume_info.get('authors', ['Unknown'])[0],
                "isbn": volume_info.get('industryIdentifiers', [{'identifier': 'Unknown'}])[0]['identifier'],
                "category": query if not is_author else volume_info.get('categories', ['Unknown'])[0],
                "publishedYear": int(volume_info.get('publishedDate', '0000').split('-')[0]),
                "thumbnail": volume_info.get('imageLinks', {}).get('thumbnail', 'Unknown'),
                "description": volume_info.get('description', 'No description available'),
                "count": 0,
                "damaged": 0
            }
            books.append(book)
        return books
    else:
        print(f'Failed to fetch books for {query}: {response.status_code}')
        return []


# Fetch books for each category and author, then collect them in a list
all_books = []

# Fetch books for each category
for category in categories:
    books = fetch_books(category, is_author=False, max_results=5)
    all_books.extend(books)

# Fetch books for each author
for author in authors:
    books = fetch_books(author, is_author=True, max_results=6)
    all_books.extend(books)

# Write the collected books data to a JSON file
output_file = 'books_by_author.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_books, f, ensure_ascii=False, indent=2)

print(f'Books data exported to {output_file}')
