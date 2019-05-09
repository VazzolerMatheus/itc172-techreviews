from django.test import TestCase
from .models import TechType, Product, Review
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.


#TEST FOR MODELS
class TechTypeTest(TestCase):

    def test_str(self):
        #we are saying that the techtype name is laptop
        #to make sure it's right, it has to return "laptop"


        #this is creating an instance of the TechType, putting the 'laptop' on the techtypename variable
        type=TechType(techtypename='laptop')
        self.assertEqual(str(type), type.techtypename)


    def test_table(self):

        self.assertEqual(str(TechType._meta.db_table), 'techtype')


class ProductTest(TestCase):

    def setUp(self):
        self.type=TechType(techtypename='tablet')


        self.prod=Product(productname='Ipad', techtype=self.type, productprice=800.00)

    def test_str(self):
        self.assertEqual(str(self.prod), self.prod.productname)

    def test_type(self):
        self.assertEqual(str(self.prod.techtype), 'tablet')

    def test_discount(self):
        self.assertEqual(self.prod.memberDiscount(), 40.00)




#TEST FOR VIEWS
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):

                        #check this later
                        #inverse imported from django.urls
        response = self.client.get(reverse('index'))

                #200 means everything is good!
        self.assertEqual(response.status_code, 200)


class GetProductsTest(TestCase):
    def setUp(self):
        self.u = User(username='myUser')
                    #you can write it like this (just the name of the class)
        self.type = TechType(techtypename = 'laptop')
                    #or like this, (with .object.create)
        self.prod = Product.objects.create(productname = 'product1', techtype=self.type, user=self.u, productprice=500.00, productentrydate='2019-04-02', productdescription='lalalalala lalalaal')

    def test_product_detail_success(self):
        response=self.client.get(reverse('product', args=(self.prod.id,)))
        self.assertEqual(response.status_code, 200)