import sqlite3
from datetime import datetime
def get_connection():
    conn = sqlite3.connect('database_file.db')
    return conn
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS notes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT,
                    created_at TEXT NOT NULL
                )
                """)
    conn.commit()
    conn.close()
def add_note(title , content):
    conn = get_connection()
    cursor = conn.cursor()
    
    created_at = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    cursor.execute("""
                   INSERT INTO notes (title , content, created_at)
                   VALUES(?,?,?)
                   """,(title , content ,created_at ))
    conn.commit()
    conn.close()
    return True
def get_all_notes():
    conn = get_connection()
    cursor = conn.cursor()
    diction = []
    cursor.execute("""
                   SELECT * FROM notes
                   """)
    notes = cursor.fetchall()
    conn.close()
    if notes:
        for note in notes:
            diction.append({
                'id' : note[0],
                'title' : note[1],
                'content' : note[2],
                'created_at' : note[3]
            })
        return diction
    return False
def get_note_by_id(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT * FROM notes WHERE id = ?
                   """,(note_id,))
    note = cursor.fetchone()
    conn.close()
    if note:
        return{
            'id' : note[0],
            'title' : note[1],
            'content' : note[2],
            'created_at' : note[3]
        }
    return False
def update_note(note_id, title=None, content=None):
    conn = get_connection()
    cursor = conn.cursor()
    fields = []
    params = []
    if title is not None:
        fields.append('title = ?')
        params.append(title)
    if content is not None:
        fields.append('content = ?')
        params.append(content)
    if not fields:
        return False
        
    sql = f"UPDATE notes SET {','.join(fields)} WHERE id = ?"
    params.append(note_id)
    cursor.execute(sql , params)
    update = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return update
def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   DELETE FROM notes WHERE id = ?
                   """,(note_id,))
    update = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return update




