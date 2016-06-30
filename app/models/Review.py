from system.core.model import Model
import re 

class Review(Model):
	def __init__(self):
		super(Review, self).__init__()
	def get_all_reviews(self):
		query='SELECT * from (SELECT * FROM reviews ORDER BY created_at DESC limit 0,3) as alias left join users on alias.users_id = users.id ORDER BY created_at desc'
		return self.db.query_db(query)
	def create_review(self,review): 
		query='INSERT INTO reviews (review, rating, users_id, books_id, created_at) VALUES (:review, :rating, :user_id, :books_id, NOW())'
		data={
		'review': review['review'],
		'rating':review['rating'],
		'user_id':review['user_id'],
		'books_id':review['book_id']
		}
		return self.db.query_db(query, data)
		# return last_inserted_id
	

	def get_review_by_id(self, review_id):
		query= 'SELECT * FROM review WHERE id= :review_id'
		data={'review_id':review_id}
		reviews=self.db.query_db(query,data)
		return reviews[0]

	