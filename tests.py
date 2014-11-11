from database import init_db, db_session
from models import *
import datetime
import unittest

class TestCase(unittest.TestCase):

    def setUp(self):
        init_db()
        
    def test_input_data(self):

        # Add users
        u1 = User(name="Paul", email="fake1@email.com", 
                    password="password")
        u2 = User(name="Joe", email="fake2@gmail.com", 
                    password="password")

        # Add beers
        b1 = Beer(name="Chaisoin", style = "Saison");
        b2 = Beer(name="Orca Porter", style = "Porter");

        # Add brewers to beers
        u1.brewers.append(b1)
        u2.brewers.append(b1)
        u1.brewers.append(b2)

        db_session.add_all([u1, u2, b1, b2])
        db_session.commit()
        print "****Data Has Been Commited to DB****"

    
    def test_query1(self):
	    #Pull a user
        user1 = db_session.query(User).filter_by(name='Paul').first()
        print "User Name: ", user1.name, "User Email: ", user1.email


    def test_query2(self):
	    #Pull a List of Brewers for a particular beer
        beer1 = db_session.query(User).filter_by(name="Orca Porter").first()
        brewers1 = db_session.query(brewers_table).all()
        for b in brewers1:
            print b.user_id


    def test_query3(self):
        #Pull results from a search
        """
        search1 = db_session.query(Alert).filter_by(name='guitars').first()
        results = db_session.query(Result).filter_by(alert=search1).all()
        for result in results:
            print "Result Title: ", result.title, "Result link: ", result.link
        """
        pass

    def tearDown(self):
        db_session.remove()

	
if __name__ == '__main__':
    unittest.main()	
