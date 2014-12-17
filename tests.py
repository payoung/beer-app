from database import init_db, db_session
from models import User, Beer, Brewer, Recipe, Malt, Hop
from datetime import date
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
        brewer1 = Brewer(user=u1, beer=b1)
        brewer2 = Brewer(user=u2, beer=b1)
        brewer3 = Brewer(user=u1, beer=b2)

        # Add a Recipe to a beer
        recipe1 = Recipe(steep_time=60, boil_time=60, brew_date=date(2014, 10, 31),
                         beer=b1)
        malt1 = Malt(variety="Pale Malt LME", weight=5, recipe=recipe1)
        malt2 = Malt(variety="Great Western 2-row", weight=4.5, recipe=recipe1)
        hop1 = Hop(variety="Magnum", addition_time=60, weight=1, recipe=recipe1)
        hop2 = Hop(variety="Cascade", addition_time=0, weight=1, recipe=recipe1)

        db_session.add_all([u1, u2, b1, b2, brewer1, brewer2, brewer3])
        db_session.add_all([recipe1, malt1, malt2, hop1, hop2])
        db_session.commit()
        print "****Data Has Been Commited to DB****"

    
    def test_query1(self):
	    #Pull a user
        user1 = db_session.query(User).filter_by(name='Paul').first()
        print "User Name: ", user1.name, "User Email: ", user1.email


    def test_query2(sxelf):
	    #Pull a List of Breers for a particular User
        user1 = db_session.query(User).filter_by(name='Paul').first()
        for b in user1.beers:
            print b.name


    def test_query3(self):
        #Pull a List of Brewers for a particular beer
        beer1 = db_session.query(Beer).filter_by(name="Chaisoin").first()
        print "Beer Name: ", beer1.name
        for u in beer1.brewers:
            print u.name

    def test_query4(self):
        #Pull a recipe
        beer1 = db_session.query(Beer).filter_by(name="Chaisoin").first()
        recipe1 = db_session.query(Recipe).filter_by(beer=beer1).first()
        r1_malts = db_session.query(Malt).filter_by(recipe=recipe1).all()
        r1_hops = db_session.query(Hop).filter_by(recipe=recipe1).all()
        print beer1.name, " Recipe - Brewd On: ", recipe1.brew_date
        print "Steep Time: ", recipe1.steep_time, " Boil Time: ", recipe1.boil_time
        print "Malts:"
        for malt in r1_malts:
            print "    Variety: ", malt.variety, "Amount: ", malt.weight
        print "Hops:"
        for hop in r1_hops:
            print "    Variety: ", hop.variety, "Amount: ", hop.weight
            

    def tearDown(self):
        db_session.remove()

	
if __name__ == '__main__':
    unittest.main()	
