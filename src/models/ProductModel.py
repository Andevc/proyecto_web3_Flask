from src.database.db_mysql import DataBase

class Product:

    def __init__(self, product_id, product_name, description, price, image_url) -> None:
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.image_url = image_url
  
    @staticmethod
    def from_dict(data):
        return Product(
            data['product_id'],
            data['product_name'],
            data['description'],
            data['price'],
            data['image_url']
        )

    @staticmethod
    def to_dict(product):
        return {
            'product_id' : product.product_id,
            'product_name' : product.product_name,
            'description' : product.description,
            'price' : product.price,
            'image_url' : product.image_url
        }

    @staticmethod 
    def get_All():
        db = DataBase()
        query = 'SELECT * FROM `product`'
        db.execute(query)
        result = db.fetchall()
        db.close()
        return [Product.from_dict(result) for result in result]
    
    @staticmethod
    def get_by_Id(product_id):
        db = DataBase()
        query = 'SELECT * FROM `product` WHERE product_id = %s'
        db.execute(query, (product_id))
        res = db.fetchone()
        db.close()
        return Product.from_dict(res) if res else None
    
    @staticmethod
    def Create(product):
        db = DataBase()
        query = 'INSERT INTO `product`(`product_id`, `product_name`, `description`, `price`, `image_url`) VALUES (%s, %s, %s, %s, %s)'
        db.execute(query, (product.product_id, product.product_name, product.description,product.price, product.image_url))
        db.close()

    @staticmethod
    def Update(product):
        db = DataBase()
        query = 'UPDATE `product` SET `product_name`=%s, `description`=%s, `price`=%s, `image_url`=%s  WHERE `product_id`=%s'
        db.execute(query, (product.product_name, product.description, product.price, product.image_url, product.product_id))
        db.close()
        
    @staticmethod
    def Delete(product_id):
        db = DataBase()
        query = 'DELETE FROM `product` WHERE `product_id` = %s'
        db.execute(query, (product_id))
        db.close()