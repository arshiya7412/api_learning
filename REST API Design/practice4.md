# Practice 4 — Filtering

## Books API

### 1. Filter books by genre
```http
GET /books?genre=science
```

### 2. Filter books by author
```http
GET /books?author=Tolkien
```

### 3. Filter by genre and year
```http
GET /books?genre=science&year=2025
```

### 4. Filter by genre with pagination
```http
GET /books?genre=science&page=2&limit=10
```

## Key concept

Filtering uses **query parameters** to narrow down the resources returned by an API.

Multiple query parameters can be combined using `&`.
