from main import app, db

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    db.create_all()
