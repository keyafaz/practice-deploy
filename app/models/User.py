from system.core.model import Model
import re 

class User(Model):
  def __init__(self):
    super(User, self).__init__()
  
  def get_all_users(self):
    return self.db.query_db('SELECT * FROM users')
  
  # def get_all_reviews(self):
  #   query='SELECT * from (SELECT * FROM reviews ORDER BY created_at DESC limit 0,3) as alias left join users on alias.users_id = users.id ORDER BY created_at desc'
  #   return self.db.query_db(query)
  def create_poke(self, pokes):
    query='INSERT into pokes(users_id, poker_id)values (:users_id, :poker_id)'
    data={
    'users_id':pokes['users_id'],
    'poker_id':pokes['poker_id']}
    return self.db.query_db(query, data)

  def poke_history(self, user_id):
    query='SELECT users.*, COUNT(pokes.users_id) as poke_history FROM users LEFT JOIN pokes ON( users.id = pokes.users_id ) GROUP BY users.id'
    data={'id':user_id}
    return self.db.query_db(query, data)





  def get_user_by_id(self, user_id):
    query= 'SELECT * FROM users WHERE id= :user_id'
    data={'user_id':user_id}
    return self.db.query_db(query,data)

  
  # def get_pokes(self, id):
  #   query= 'SELECT users.name as poker, users.id as poker_id, users2.name as pokee, users2.id as pokee_id FROM users LEFT JOIN pokes ON users.id = pokes.poker_id LEFT JOIN users as users2 ON users2.id = pokes.users_id'
  #   data={'user_id':user_id}
  #   return self.db.query_db(query,data)
  def get_all_pokes(self):
    query='SELECT * FROM pokes'
    return self.db.query_db(query)

  def get_pokes(self, id):
    query= 'SELECT * FROM pokes WHERE id= :user_id'
    data={'user_id':user_id}
    return self.db.query_db(query,data)

  def register_user(self, info):
    EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
    errors=[]
    if not info['name']:
      errors.append('Name cannot be blank')
    if not info['alias']:
      errors.append('Alias cannot be blank')
    elif len(info['name'])<2:
      errors.append("Name must be at least 2 characters long.")
    if not info['birthday']:
      errors.append("Birthday cannot be blank")
    if not info['email']:
      errors.append("Email cannot be blank")
  
    elif not EMAIL_REGEX.match(info['email']):
      errors.append('Email format must be valid!')  
     
    if not info['password']:
      errors.append('Password cannot be blank')
    elif len(info['password'])<8:
      errors.append('Password must be at least 8 characters long')
  
    elif info['password'] != info['confirm_pw']:
      errors.append('Passwords must match!')
    
    
    query= "SELECT * FROM users WHERE email=:email limit 1"
    data={'email':info['email']}
    email_validation=self.db.query_db(query, data)
    if len(email_validation) >0:
      errors.append('Email is already registered.')
    if errors:
      return{'status':False, 'errors':errors}
    else:
      password=info['password']
      hashed_pw = self.bcrypt.generate_password_hash(password)
     

      create_query='INSERT INTO users (name, alias, email, pw_hash, birthday) VALUES (:name, :alias, :email, :pw_hash, NOW())'
      create_data = {
       'name':info['name'],
       'alias':info['alias'],
       'email':info['email'], 
       'pw_hash':hashed_pw}

      last_insert_id=self.db.query_db(create_query, create_data)
      
      create_data['id']=last_insert_id
      return{'status':True, 'user': create_data, 'last_insert_id':last_insert_id}

  def login_user(self,info):
    password= info['password']
    errors=[]
    user_query='SELECT * FROM users WHERE email = :email LIMIT 1'
    user_data={
    'email':info['email']
    }
    users = self.db.query_db(user_query, user_data)
    if not info['email']:
      errors.append("Email cannot be blank")
    elif len(users) == 0:
      errors.append("no email found")
    else:
      user=users[0]
      if self.bcrypt.check_password_hash(user['pw_hash'],password):
        return {'status':True, 'user':user}
      errors.append('Invalid email or password')
    return {'status': False, 'errors':errors}

  # def pokes(self, pokes)
  #   query='INSERT into pokes (users_id, poker_id) values (:users_id,:poker_id)'
  #   data={
  #   'users_id':pokes['users_id'],
  #   'poker_id':pokes['poker_id']
  #   }
  #   return self.db.query_db(query, data)



 


  #   query= 'INSERT INTO products (name, description, price) VALUES (:name, :description, :price)'
  #   data={
  #   'name':product['name'],
  #   'description':product['description'],
  #   'price':product['price']
  #   }
  #   return self.db.query_db(query, data)

  # def update_product(self, product):
  #   query='UPDATE products SET name= :name, description= :description, price= :price WHERE id= :product_id'
  #   data= {
  #   'name':product['name'],
  #   'description':product['description'],
  #   'price':product['price'],
  #   'product_id':product['id']
  #   }
  #   return self.db.query_db(query, data)

  # def delete_product(self, product_id):
  #   query='DELETE FROM products WHERE id= :product_id'
  #   data={'product_id': product_id}
  #   return self.db.query_db(query, data)

    







  # def create_user(self, info):
  #   EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
  #   errors=[]
  #   is_valid=False
  #   if not info['first_name']:
  #     errors.append('First name cannot be blank')
  #     is_valid=False
  #   elif len(info['first_name'])<2:
  #     errors.append("First name must be at least 2 characters long.")
  #     is_valid=False
  #   if not info['last_name']:
  #     errors.append("Last name cannot be blank")
  #     is_valid=False
  #   elif len(info['last_name'])<2:
  #     errors.append("Last name must be at least 2 characters long")
  #     is_valid=False
  #   if not info['email']:
  #     errors.append("Email cannot be blank")
  #     is_valid=False
  #   elif not EMAIL_REGEX.match(info['email']):
  #     errors.append('Email format must be valid!')  
  #     is_valid=False  
  #   if not info['password']:
  #     errors.append('Password cannot be blank')
  #   elif len(info['password'])<8:
  #     errors.append('Password must be at least 8 characters long')
  #     is_valid=False
  #   elif info['password'] != info['confirm_pw']:
  #     errors.append('Emails must match!')
  #     is_valid=False
    
  #   query= "SELECT * FROM user WHERE email=:email limit 1"
  #   data={'email':info['email']}
  #   email_validation=self.db.query_db(query, data)
  #   if len(email_validation) >0:
  #     errors.append('Email is already registered.')
  #     is_valid=False
  #   if errors:
  #     return{'status':False, 'errors':errors}
  #   else:
  #     password=info['password']
  #     hashed_pw = self.bcrypt.generate_password_hash(password)
  #     create_query='INSERT INTO user (first_name, last_name, email, pw_hash) VALUES (:first_name, :last_name, :email, :pw_hash)'
  #     create_data = {
  #     'first_name':info['first_name'],
  #      'last_name':info['last_name'],
  #      'email':info['email'], 
  #      'pw_hash':hashed_pw
  #      }
  #     self.db.query_db(create_query, create_data)

  #     get_user_query='SELECT * FROM user ORDER by id DESC LIMIT 1'
  #     users=self.db.query_db(get_user_query)
  #     return{'status':True, 'user':users[0]}

  # def login_user(self,info):
  #   password= info['password']
  #   errors=[]
  #   user_query='SELECT * FROM user WHERE email = :email LIMIT 1'
  #   user_data={
  #   'email':info['email']
  #   }
  #   users = self.db.query_db(user_query, user_data)
  #   if len(users) == 0:
  #     errors.append("no email found")
      
    
  #   else:
  #     user=users[0]
  #     if self.bcrypt.check_password_hash(user['pw_hash'],password):
  #       return {'status':True, 'user':user}
  #     errors.append('Invalid email or password')
  #   return {'status': False, 'errors':errors}




    # def get_all_courses(self):
    #     return self.db.query_db("SELECT * FROM courses")

    # def get_course_by_id(self, course_id):
    #     # pass data to the query like so
    #     query = "SELECT * FROM courses WHERE id = :course_id"
    #     data = { 'course_id': course_id}
    #     return self.db.query_db(query, data)

    # def add_course(self, course):
    #   # Build the query first and then the data that goes in the query
    #   query = "INSERT INTO courses (title, description, created_at) VALUES (:title, :description, NOW())"
    #   data = { 'title': course['title'], 'description': course['description'] }
    #   return self.db.query_db(query, data)

    # def update_course(self, course):
    #   # Building the query for the update
    #   query = "UPDATE courses SET title=:title, description=:description WHERE id = :course_id"
    #   # we need to pass the necessary data
    #   data = { 'title': course['title'], 'description': course['description'], 'course_id': course['id']}
    #   # run the update
    #   return self.db.query_db(query, data)

    # def delete_course(self, course_id):
    #   query = "DELETE FROM courses WHERE id = :course_id"
    #   data = { "course_id": course_id }
    #   return self.db.query_db(query, data)