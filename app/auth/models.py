from datetime import datetime
from flask_login.mixins import UserMixin
from app import db, bcrypt
from app import login_manager


class User(db.Model, UserMixin):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25))
    user_email = db.Column(db.String(100), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registartion_date = db.Column(db.DateTime, default=datetime.now)


    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)
    

    @classmethod
    def create_user(cls, user, email, password):
        
        user = cls(user_name=user, 
                   user_email=email,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8')
                   )
        
        db.session.add(user)
        db.session.commit()
        return user
    
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))