from system.core.controller import *
class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        # Note that we have to load the model before using it
        self.load_model('User')
        self.load_model('Review')
        self.load_model('Book')

    def index(self):
        return self.load_view('index.html')

    

    def register_user(self):
        user_info={
        'name':request.form['name'],
        'alias':request.form['alias'],
        'email': request.form['email'],
        'password':request.form['password'],
        'confirm_pw':request.form['confirm_pw'], 
        'birthday':request.form['birthday']
        }
        create_status=self.models['User'].register_user(user_info)
        
        if create_status['status']== True:
            session['name']=create_status['user']['name']
            session['id']= create_status['user']['id']
            session['logged_in_as']= create_status['user']['id']
            flash('You are successfully registered')
            return redirect('/users/poke')
        else:
            for message in create_status['errors']:
                flash(message,'regis_errors')
            return redirect('/')
    
    def login_user(self):
        user_info={
        'email': request.form['email'],
        'password':request.form['password']
        }
        login_status=self.models['User'].login_user(user_info)
        if login_status['status'] == True:
            session['logged_in_as']=login_status['user']['id'] 
            flash('Successfully logged in!')
            return redirect('/users/poke')
        if login_status['status']==False:
            for message in login_status['errors']:
                flash(message, 'login_errors')
            return redirect('/')


  

    def logged_in_home_page(self):
        if 'logged_in_as' not in session:
            flash("You need to be logged in to view this page. Please log in to continue",'logouts')
            return redirect("/")
        
        poke_history_details={
        'user_id':session['logged_in_as']}
        pokees= self.models['User'].poke_history(poke_history_details)
        return self.load_view('poke.html', all_users=pokees)


    def poke_user(self):
        if 'logged_in_as' not in session:
            flash("You need to be logged in to view this page. Please log in to continue",'logouts')
            return redirect("/")
        user_id_details={
        'users_id':request.form['pokee_id'],
        'poker_id':session['logged_in_as']
        }
        print user_id_details
        self.models['User'].create_poke(user_id_details)

        return redirect('/users/poke')

    # def poke_history(self, user_id):
    #     poke_history_details={
    #     'user_id':session['logged_in_as']}
    #     all_users= self.models['User'].poke_history(poke_history_details)
    #     return redirect('/users/poke')

    def logout(self):
        session.pop("logged_in_as", None)
        return redirect('/')

    

    # def add_page(self):
    #     if 'logged_in_as' not in session:
    #         return redirect("/")
       
    #     author= self.models['Book'].get_all_authors() 
    #     return self.load_view('add_book.html', authors=author)
        
    # def create(self):
    #     if 'logged_in_as' not in session:
    #         return redirect("/")
        
    #     book_details={
    #     'title':request.form['title'],
    #     'author':request.form['author']
    #     }
    #     book_id=self.models['Book'].create_book(book_details)
        
       
    #     review_details = {
    #     'review': request.form['review'],
    #     'rating':request.form['rating'],
    #     'user_id':session['logged_in_as'],
    #     'book_id':book_id
    #     }
    #     self.models['Review'].create_review(review_details)
    #     return self.load_view('review_book.html')


    # def review_book(self,id):
    #     self.models['Review'].get_review_by_id(id)
    #     # book= self.models['Book'].get_book_by_id(id)
    #     return self.load_view('review_book.html',review=review, book=book[0])

 








    # def show(self, id):
    #     product= self.models['Product'].get_product_by_id(id)
    #     return self.load_view('show.html.html', product=product[0])

    # def new(self):
    #     return self.load_view('new_product.html')
    
    # def create(self):
    #     product_details = {
    #     'name': request.form['name'],
    #     'description':request.form['description'],
    #     'price':request.form['price']
    #     }
    #     self.models['Product'].create_product(product_details)
    #     return redirect('/')



    # def edit(self, id):
    #     product= self.models['Product'].get_product_by_id(id)
        
    #     return self.load_view('edit_product.html',product=product[0])

    # def update(self, product_id):
    #     product_details={
    #     'id': product_id,
    #     'name':request.form['name'],
    #     'description':request.form['description'],
    #     'price':request.form['price']
    #     }
    #     self.models['Product'].update_product(product_details)
    #     return redirect('/')

    # def remove(self, product_id):
    #     self.models['Product'].delete_product(product_id)
    #     return redirect('/')

    # def logged_in_page(self):
    #     return self.load_view('success.html')

    # def register(self):
    #     user_info={
    #     'first_name': request.form['first_name'],
    #     'last_name': request.form['last_name'],
    #     'email': request.form['email'],
    #     'password':request.form['password'],
    #     'confirm_pw':request.form['confirm_pw']
    #     }
    #     create_status=self.models['User'].create_user(user_info)
    #     if create_status['status'] == True:
    #         session['first_name']=create_status['user']['first_name']
    #         session['id'] = create_status['user']['id']
    #         flash("You are successfully registered ")
    #         return redirect ('/users/success')
    #     else:
    #         for message in create_status['errors']:
    #             flash(message,'regis_errors')  
    #         return redirect('/')
    
    # def login(self):
    #     user_info={
    #     'email':request.form['email'],
    #     'password':request.form['password']
    #     }
    #     login_status=self.models['User'].login_user(user_info)
    #     if login_status['status'] ==True:
    #         session['logged_in_as'] = login_status['user']['id']
    #         flash("You are successfully logged in")
    #         return redirect('/users/success')    
    #     if login_status['status']==False:
    #         for message in login_status['errors']:
    #             flash(message, 'login_errors')
    #     return redirect('/')


    # # This is how a method with a route parameter that provides the id would work
    # # We would set up a GET route for this method
    # def show(self, id):
    #     # Note how we access the model using self.models
    #     course = self.models['Course'].get_course_by_id(id)
    #     return self.load_view('show.html', course=course[0])

    # # This is how a method used to add a course would look
    # # We would set up a POST route for this method
    # def add(self):
    #     # in actuality, data for the new course would come 
    #     # from a form on our client
    #     course_details = {
    #         'title': request.form['title'],
    #         'description': request.form['description']
    #     }
    #     self.models['Course'].add_course(course_details)
    #     return redirect('/')

    # # This is how a method used to update a course would look
    # # We would set up a POST route for this method
    # def update(self, course_id):
    #     # in actuality, data for updating the course would come 
    #     # from a form on our client
    #     course_details = {
    #         'id': course_id,
    #         'title': request.form['title'],
    #         'description': request.form['description']
    #     }
    #     self.models['Course'].update_course(course_details)
    #     return redirect('/')

    #  # This is how a method used to delete a course would look
    #  # We would set up a POST route for this method
    # def delete(self, course_id):
    #     self.models['Course'].delete_course(course_id)
    #     return redirect('/')