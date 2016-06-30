from system.core.model import Model
import re 

class Book(Model):
	def __init__(self):
		super(Book, self).__init__()
	


	def create_book(self,book):
		query='INSERT INTO books (title, author) VALUES (:title, :author)'
		data={
		'title': book['title'],
		'author':book['author']
		}
		last_inserted_id = self.db.query_db(query, data)
		return last_inserted_id
		# bood if will be =last_insert id which is from querty of review =lst insert
	
	def get_book_by_id(self, book_id):
		query= 'SELECT * FROM books WHERE id= :book_id'
		data={'book_id':book_id}
		return self.db.query_db(query,data)
	def get_all_authors(self):
		query='SELECT books.author FROM books'
		# data={'author':author['author']} 
	
		return self.db.query_db(query)