# Practice 5 — Sorting

## Books API

### 1. Sort books by title in ascending order
```http
GET /books?sort=title&order=asc
```

### 2. Sort books by year in descending order
```http
GET /books?sort=year&order=desc
```

### 3. Filter science books and sort by year descending
```http
GET /books?genre=science&sort=year&order=desc
```

### 4. Get page 2, 10 books per page, sorted by title ascending
```http
GET /books?sort=title&order=asc&page=2&limit=10
```

## Key concept

Sorting controls the order in which resources are returned.

- `sort=title` → sort using the title field
- `order=asc` → ascending order
- `order=desc` → descending order
