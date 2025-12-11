from flask import Flask , request, jsonify
import database as db
app = Flask(__name__)
db.create_table()


@app.route('/api/notes/' , methods = ['POST'])
def add_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    result = db.add_note(title , content)
    if not result:
        return jsonify({'error' : 'could not add the note!'}) , 404
    return jsonify({'message' : 'note added successfully'}) , 201


@app.route('/api/notes/' , methods = ['GET'])
def get_all_notes():
    result = db.get_all_notes()
    if not result:
        return jsonify({"error" : "No notes were found"}) , 404
    return jsonify(result) , 200

@app.route('/api/notes/<int:note_id>' , methods = ['GET'])
def get_single_note(note_id):
    result = db.get_note_by_id(note_id)
    if not result:
        return jsonify({'error' : f"your note_id {note_id} could not be found"}) , 404
    return jsonify(result) , 200

@app.route('/api/notes/<int:note_id>' , methods = ['PUT'])
def update_note(note_id):    
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    if db.update_note(note_id, title, content):
        return jsonify({"message" : f"note_id {note_id} was updated successfully"}) , 200
    return jsonify({"error" : f"note_id {note_id} could not be updated"}) , 404
  
@app.route('/api/notes/<int:note_id>' , methods = ['DELETE']) 
def delete_note(note_id):
    
    if db.delete_note(note_id):
        return jsonify({"message" : f"note_id {note_id} was deleted successfully"}) , 200
    return jsonify({"error" : f"note_id {note_id} could not be deleted"}) , 404 
  
    
if __name__ == "__main__":
    app.run(debug=True)