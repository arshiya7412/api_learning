# Practice 1 — Resource-Based URLs

## Student API

### 1. Get all students
```http
GET /students
```

### 2. Get student with ID 25
```http
GET /students/25
```

### 3. Create a student
```http
POST /students
```

### 4. Delete student with ID 25
```http
DELETE /students/25
```

### 5. Get assignments belonging to student 25
```http
GET /students/25/assignments
```

### 6. Get assignment 8 belonging to student 25
```http
GET /students/25/assignments/8
```

## Key concept

The URL identifies the **resource**, while the HTTP method determines the **operation**.

- `/students` → student collection
- `/students/25` → specific student
- `/students/25/assignments` → assignments belonging to student 25
- `/students/25/assignments/8` → specific assignment
