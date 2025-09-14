import sys
import os

# Add the backend_app folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend_app')))

from app.models.user import User, db
from app import create_app


app = create_app()

with app.app_context():
    # Check if user already exists
    if not User.query.filter_by(email='testuser@sds.org').first():
        user = User(email='testuser@sds.org')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        print("✅ Test user created")
    else:
        print("ℹ️ Test user already exists")