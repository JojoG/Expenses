"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime
from django.contrib.auth.models import User
from expenses.models import Person, Household, Multiplier, Transaction

from tests_setup import FollowTestCase



class SimpleTest(FollowTestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)



class CreatePersonTest(FollowTestCase):

    @classmethod
    def jackUser(cls):
        return cls.userWithUN('jackdreilly')


    @classmethod
    def userWithUN(cls, un):
        jack = User(first_name = 'Jack',last_name = 'Reilly',username=un,password='jack1234',email='jackdreilly@gmail.com')
        return jack

    @classmethod
    def person(cls,user):
        return Person(user=user, name = "jackie jackie")

    @classmethod
    def personUN(cls,un):
        jackuser = cls.userWithUN(un)
        jackuser.save()
        return cls.person(jackuser)

    @classmethod
    def jackperson(cls):
        return cls.person(cls.jackUser())



    
    def test_make_user(self):
        jack = self.jackUser()
        jack.save()
        self.assertEqual(jack.first_name, 'Jack', msg='user has first name')
        self.assertGreater(User.objects.filter(first_name = "Jack").count() ,0, msg='user with first name save in db')


    def test_make_person(self):
        jack = self.jackUser()
        jack.save()
        jackperson = self.person(jack)
        jackperson.save()
        self.assertEqual(jackperson.name,"Jack Reilly", msg='name constructed from user info')
        self.assertEqual(jackperson.user,jack, msg='user correctly stored in person')
        self.assertGreater(Person.objects.filter(name = "Jack Reilly").count() ,0,msg='person stored in db')


class CreateHouseholdTest(FollowTestCase):

    @classmethod
    def createHousehold(cls):
        hh =  Household(name="sick household")
        hh.save()
        hh.persons = Person.objects.all()
        return hh

    @classmethod
    def jackHousehold(cls):
        user = CreatePersonTest.jackperson()
        user.save()
        household = cls.createHousehold()
        household.save()
        return household

    def test_create_household(self):
        household = self.jackHousehold()
        self.assertEqual(household.name, "sick household", msg='household name success')
        self.assertEqual(household.persons.count(), 1,msg='people in household')
        self.assertLess(household.creation_date , datetime.now(),msg='creation date bootstrap than now? that\'s good')
        self.assertGreater(Household.objects.filter(name="sick household").count(), 0,msg='db stored hh with name')


class CreateTransactionTest(FollowTestCase):

    @classmethod
    def createTransaction(cls):
        household = CreateHouseholdTest.jackHousehold()
        transactor = household.persons.all()[0]
        return Transaction(household = household, transactor = transactor,cost=302., tax = .008 )

    def test_create_transaction(self):
        trans = self.createTransaction()
        trans.save()
        self.assertIsNotNone(trans.transactor,msg='transactor stored w trans')
        self.assertEqual(trans.cost, 302.,msg='cost correct in trans')
        self.assertEqual(trans.tax, .008,msg='tax correct in trans')
        hh = trans.household
        self.assertGreater(hh.transaction_set.count(), 0,msg='hh has reference to transaction')
        n_people_hh = hh.persons.count()
        mults = Multiplier.objects.filter(transaction=trans)
        n_mults = mults.count()
        self.assertEqual(n_people_hh, n_mults,msg='same num of hh members as mults w trans reference')
        single_mult_value = mults[0].multiplier
        mult_values = [mult.multiplier for mult in mults]
        self.assertAlmostEqual(sum(mult_values), 1, places=5, msg='sum of mults equals 1')
        self.assertTrue(all([val == single_mult_value for val in mult_values]),msg='all mults have same init value')


class CreateInviteTest(FollowTestCase):

    @classmethod
    def createInvite(cls):
        u1 = CreatePersonTest.personUN('jackie')
        u2 = CreatePersonTest.personUN('jill')
        u1.save()
        u2.save()
        