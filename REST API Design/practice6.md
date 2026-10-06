# Practice 6 — Searching

## Books API

### 1. Search for books matching "python"
```http
GET /books?search=python
```

### 2. Search for "harry" and sort by title ascending
```http
GET /books?search=harry&sort=title&order=asc
```

### 3. Search for "science", page 2, 10 results per page
```http
GET /books?search=science&page=2&limit=10
```

### 4. Search for "AI", filter by technology, and sort by year descending
```http
GET /books?search=AI&genre=technology&sort=year&order=desc
```

## Key concept

Searching uses a query parameter such as `search=` to find resources matching a search term.

Searching can be combined with filtering, sorting, and pagination.
