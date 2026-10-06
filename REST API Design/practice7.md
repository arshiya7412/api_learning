# Practice 7 — API Versioning

## Student API

### 1. Version 1 — get all students
```http
GET /api/v1/students
```

### 2. Version 1 — get student 25
```http
GET /api/v1/students/25
```

### 3. Version 2 — get all students
```http
GET /api/v2/students
```

### 4. Version 2 — get student 25's assignments
```http
GET /api/v2/students/25/assignments
```

### 5. Version 2 — search and sort students
Correct REST-style URL:
```http
GET /api/v2/students?search=Arshiya&sort=name&order=asc
```

## Key concept

API versioning allows different API versions to coexist.

For example:

- `/api/v1/students` → version 1
- `/api/v2/students` → version 2

Older clients can continue using v1 while newer clients use v2.

> The original answer for #5 used `/students/search=Arshiya/sort=name/order=asc`. Those values are query parameters, so they should follow `?` and be separated with `&`.
