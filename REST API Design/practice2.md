# Practice 2 — CRUD Operations

## Books API

### 1. Create a new book
```http
POST /books
```

### 2. Get all books
```http
GET /books
```

### 3. Get book 42
```http
GET /books/42
```

### 4. Completely replace book 42
```http
PUT /books/42
```

### 5. Change only the title of book 42
```http
PATCH /books/42
```

Example request body:
```json
{
  "title": "New Title"
}
```

> Note: `PATCH /books/42/title` was initially used, but the conventional REST design is to PATCH the book resource and send the changed field in the request body.

### 6. Delete book 42
```http
DELETE /books/42
```

## Key concept

- **URL** = what resource is being targeted
- **HTTP method** = what operation is being performed
- **Request body** = what data is being created or changed
