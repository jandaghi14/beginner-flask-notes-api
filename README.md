# Flask Notes API

A simple and clean REST API for note-taking built with Flask and SQLite. Features full CRUD operations with a minimal, easy-to-understand codebase.

## Features

- **Create Notes**: Add new notes with title and content
- **Read Notes**: Retrieve all notes or a specific note by ID
- **Update Notes**: Modify existing note titles and content
- **Delete Notes**: Remove notes permanently
- **SQLite Database**: Lightweight persistent storage
- **RESTful Design**: Standard HTTP methods and status codes
- **Automatic Timestamps**: Created date tracked for each note

## Technologies Used

- Python 3
- Flask (Web Framework)
- SQLite3 (Database)

## Database Schema

### Notes Table
```sql
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT,
    created_at TEXT NOT NULL
)
```

## API Endpoints

### Get All Notes
```
GET /api/notes/
```
**Response:** Array of all notes with id, title, content, and timestamp

**Example Response:**
```json
[
  {
    "id": 1,
    "title": "First Note",
    "content": "This is my first note",
    "created_at": "11/12/2025, 18:35:37"
  }
]
```

---

### Get Single Note
```
GET /api/notes/<id>
```
**Response:** Single note object or 404 error if not found

---

### Create New Note
```
POST /api/notes/
Content-Type: application/json

{
  "title": "Note title",
  "content": "Note content"
}
```
**Response:** 201 Created with success message

---

### Update Note
```
PUT /api/notes/<id>
Content-Type: application/json

{
  "title": "Updated title",
  "content": "Updated content"
}
```
**Response:** 200 OK with success message or 404 if not found

**Note:** Both fields are optional - send only the fields you want to update

---

### Delete Note
```
DELETE /api/notes/<id>
```
**Response:** 200 OK with success message or 404 if not found

---

## Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/jandaghi14/beginner-flask-notes-api.git
cd beginner-flask-notes-api
```

2. **Install Flask:**
```bash
pip install flask
```

3. **Run the application:**
```bash
python app.py
```

4. **Server runs on:** `http://127.0.0.1:5000`

## Testing with curl

### Create a note
```bash
curl -X POST http://127.0.0.1:5000/api/notes/ -H "Content-Type: application/json" -d "{\"title\": \"My first note\", \"content\": \"This is the content\"}"
```

### Get all notes
```bash
curl http://127.0.0.1:5000/api/notes/
```

### Get single note
```bash
curl http://127.0.0.1:5000/api/notes/1
```

### Update note
```bash
curl -X PUT http://127.0.0.1:5000/api/notes/1 -H "Content-Type: application/json" -d "{\"title\": \"Updated title\"}"
```

### Delete note
```bash
curl -X DELETE http://127.0.0.1:5000/api/notes/2
```

## Project Structure
```
beginner-flask-notes-api/
│
├── app.py              # Flask application and API routes
├── database.py         # Database operations and schema
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## Key Features

### Clean Architecture
- Separation of concerns (routes vs database logic)
- Modular code organization
- Easy to understand and maintain

### Error Handling
- Proper HTTP status codes (200, 201, 404)
- Descriptive error messages
- Validation for missing notes

### Database Design
- Automatic ID generation
- Timestamp tracking
- Optional content field
- Parameterized queries for security

## What I Learned

- Building REST APIs with Flask
- SQLite database operations
- HTTP methods and status codes
- JSON request/response handling
- API testing with curl
- Error handling in web applications
- Code organization and modularity

## Future Improvements

- Add user authentication
- Implement search functionality
- Add tags/categories for notes
- Pagination for large note collections
- Input validation and sanitization
- Deploy to cloud platform
- Add unit tests

## License

This project is open source and available for educational purposes.

## Author

Built as part of a Python learning journey - practicing Flask and SQLite integration.