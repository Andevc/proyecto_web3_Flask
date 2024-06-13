from src.database.db_mysql import DataBase
from werkzeug.security import generate_password_hash, check_password_hash
class User:
 
    def __init__(self, user_id, username, password, email, fullname) -> None:
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.fullname = fullname

    @staticmethod
    def from_dict(data):
        print(str(data))
        return User(
            data['user_id'],
            data['username'],
            data['password'],
            data['email'],
            data['fullname']
        )

    @staticmethod
    def to_dict(user):
        return {
            'user_id' : user.user_id,
            'username' : user.username,
            'password' : user.password,
            'email' : user.email,
            'fullname' : user.username
        }
    
    @staticmethod
    def get_All():
        db = DataBase()
        query = 'SELECT * FROM `user`'
        db.execute(query)
        results = db.fetchall()
        db.close
        return [User.from_dict(result) for result in results]
    
    @staticmethod
    def get_by_Id(user_id):
        db = DataBase()
        query = 'SELECT * FROM `user` WHERE user_id = %s'
        db.execute(query, (user_id))
        res = db.fetchone()
        db.close()
        return User.from_dict(res) if res else None

    @staticmethod
    def Create(user):
        db = DataBase()
        #hashed_password = generate_password_hash(user.password, method='sha256')
        query = 'INSERT INTO `user`(`user_id`, `username`, `password`, `email`, `fullname`) VALUES (%s ,%s ,%s ,%s ,%s )'
        db.execute(query, (user.user_id, user.username, user.password, user.email, user.fullname))
        db.close()
    
    @staticmethod
    def Update(user):
        db = DataBase()
        query = 'UPDATE `user` SET `username`=%s, `password`=%s, `email`=%s, `fullname`=%s  WHERE `user_id`=%s '
        db.execute(query, (user.username, user.password, user.email, user.fullname, user.user_id))
        db.close()
        
    @staticmethod
    def Delete(user_id):
        db = DataBase()
        query = 'DELETE FROM `user` WHERE `user_id`=%s'
        db.execute(query, (user_id))
        db.close

    @staticmethod
    def get_by_username(username):
        db = DataBase()
        query = 'SELECT * FROM `user` WHERE username = %s'
        db.execute(query, (username,))
        res = db.fetchone()
        db.close()
        return User.from_dict(res) if res else None
    
    @staticmethod
    def get_by_email(email):
        db = DataBase()
        query = 'SELECT * FROM `user` WHERE email = %s'
        db.execute(query, (email,))
        res = db.fetchone()
        db.close()
        return User.from_dict(res) if res else None
    

    @staticmethod
    def check_password(stored_password, provided_password):
        return stored_password == provided_password