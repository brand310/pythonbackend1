from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'          
app.config['SQLALCHEMY_TRACK_MODIFICTAIONS'] = False

db = SQLAlchemy(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db)



@app.route('/', methods = ['GET'])
def get_articles():
    return jsonify({'hello':'world'})


if __name__ == "__main__":
    app.run(debug=True)