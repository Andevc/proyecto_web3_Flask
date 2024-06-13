from src.database.db_mysql import DataBase
from src.models.ProductModel import Product

class Collection:
 
    def __init__(self, user_id, product_id ) -> None:
        self.user_id = user_id
        self.product_id = product_id

    @staticmethod
    def from_dict(data):
        return Collection( data['user_id'], data['product_id'] )
        
            
    @staticmethod
    def add_product_to_user_collection(user_id, product_id):
        db = DataBase()
        query = 'INSERT INTO `collection`(`user_id`, `product_id`) VALUES (%s, %s)'
        db.execute(query, (user_id, product_id))
        db.close()

    @staticmethod
    def delete_from_collection(user_id, product_id):
        db = DataBase()
        query = 'DELETE FROM collection WHERE user_id = %s AND product_id = %s '
        db.execute(query, (user_id, product_id))
        db.close()

    @staticmethod
    def get_by_user_and_product_id(user_id, product_id):
        db = DataBase()
        query = 'SELECT * FROM collection WHERE user_id = %s AND product_id = %s'
        db.execute(query, (user_id, product_id))
        res = db.fetchone()
        db.close()
        return Collection.from_dict(res) if res else None
    
    @staticmethod
    def get_products_by_user_id(user_id):
        db = DataBase()
        query = """
                SELECT * FROM product 
                JOIN collection ON collection.product_id = product.product_id 
                JOIN user ON collection.user_id = user.user_id 
                WHERE user.user_id = %s;
                """
        db.execute(query, (user_id))
        results = db.fetchall()
        db.close
        return [Product.from_dict(res) for res in results]
        
    @staticmethod
    def count_products_from_user(user_id):
        db = DataBase()
        query = 'SELECT COUNT(*) AS count FROM collection WHERE user_id = %s'
        db.execute(query, (user_id))
        res = db.fetchone()
        db.close()
        return res['count']
    
    # @staticmethod
    # def update_user_by_product_id(user_id, product_id):
    #     db = DataBase()
    #     query = 'UPDATE `collection` SET `user_id`= %s WHERE product_id = %s'
    #     db.execute(query, (user_id, product_id))
    #     db.close()
        
        
    