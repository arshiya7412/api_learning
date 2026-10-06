# Practice 3 — Pagination

## Books/Products API

### 1. Get page 1 with 10 results
```http
GET /products?page=1&limit=10
```

### 2. Get page 2 with 10 results
```http
GET /products?page=2&limit=10
```

## Key concept

Pagination splits a large collection into smaller pages.

- `page=1` → first page
- `page=2` → second page
- `limit=10` → maximum 10 results per page

> The `/products` endpoint is used here to demonstrate API URL design; JSONPlaceholder does not provide a real products resource.
