from src.database.db_mysql import DataBase
from werkzeug.security import generate_password_hash, check_password_hash
from src.utils.generate_id import generate_id
class User:
 
    def __init__(self, user_id,username, password, email, fullname) -> None:
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.fullname = fullname

    # Operaciones CRUD

    @staticmethod
    def Create(user):
        db = DataBase()
        gen_id = str(generate_id())
        hashed_password = generate_password_hash(user.password)
        query = 'INSERT INTO `user`(`user_id`, `username`, `password`, `email`, `fullname`) VALUES (%s ,%s ,%s ,%s ,%s )'
        db.execute(query, (gen_id, user.username, hashed_password, user.email, user.fullname))
        db.close()
    
    @staticmethod
    def Update(user):
        db = DataBase()
        query = 'UPDATE `user` SET `username`=%s, `password`=%s, `email`=%s, `fullname`=%s  WHERE `user_id`=%s '
        hashed_password = generate_password_hash(user.password)
        db.execute(query, (user.username, hashed_password, user.email, user.fullname, user.user_id))
        db.close()
        
    @staticmethod
    def Delete(user_id):
        db = DataBase()
        query = 'DELETE FROM `user` WHERE `user_id`=%s'
        db.execute(query, (user_id))
        db.close

    # Otros Metodos 

    @staticmethod
    def from_dict(data):
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
    def check_password(hash_passwors, password):
        return check_password_hash(hash_passwors, password)

    