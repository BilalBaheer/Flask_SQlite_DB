from flask import Flask, request, jsonify
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
import flask
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
from  sqlalchemy import event



#app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY__TRACK_MODIFICATIONS"] = 0



#confiure sqlite3 to enforce foreighn key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connecton, connection_record):
    if isinstance(dbapi_connecton, SQLite3Connection):
        cursor = dbapi_connecton.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()
#models 
db = SQLAlchemy(app)
app.app_context().push()
now = datetime.now()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))  # Corrected data type
    email = db.Column(db.String(50))  # Corrected data type
    address = db.Column(db.String(200))  # Corrected data type
    phone = db.Column(db.String(50))  # Corrected data type
    posts = db.relationship("BlogPost")

class BlogPost(db.Model):
    __tablename__ = "blogpost"  # Corrected attribute name
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))  # Corrected data type
    body = db.Column(db.String(200))  # Corrected data type
    date = db.Column(db.Date)  # Corrected attribute name
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)  # Corrected attribute name


def init_db():
    with app.app_context():
        db.create_all()

# Define a route or a function to trigger the database initialization
@app.route('/initialize-db', methods=['GET'])
def initialize_db():
    init_db()
    return 'Database initialized'

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/user", methods=["POST"])
def create_user():
    # Parse request as JSON 
    data = request.get_json()
    new_user = User(
        name=data["name"],
        email=data["email"],
        address=data["address"],
        phone=data["phone"],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 200

@app.route("/user/<int:user_id>", methods=["GET"])
def get_one_user(user_id):
    return jsonify({"message": "Placeholder for get_one_user"}), 200

@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return jsonify({"message": "Placeholder for delete_user"}), 200

@app.route("/blog_post/<int:blog_post_id>", methods=["GET"])
def get_one_blog_post(blog_post_id):
    return jsonify({"message": "Placeholder for get_one_blog_post"}), 200

@app.route("/blog_post/<int:blog_post_id>", methods=["DELETE"])
def delete_blog_post(blog_post_id):
    return jsonify({"message": "Placeholder for delete_blog_post"}), 200


if __name__ == "__main__":
    app.run(debug=True)

