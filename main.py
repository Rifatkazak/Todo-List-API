from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from user_auth import user_auth_bp
from todo_list import todo_list_bp

app = Flask(__name__)

# Veritabanı yapılandırması
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Blueprint'leri kaydetme
app.register_blueprint(user_auth_bp, url_prefix='/auth')
app.register_blueprint(todo_list_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
