from django.test import TestCase
from .models import *

# Create your tests here.
# Create your views here.
class CoupleManager:
    def __init__(self):
        self._male = ""
        self._female = ""

    @property
    def male(self):
        return self._male

    @male.setter
    def male(self, value):
        self._male = value

    @property
    def female(self):
        return self._female

    @female.setter
    def female(self, value):
        self._female = value

    def diff(self):
        male_age = Male.objects.all().filter(name__icontains=self._male)
        print(male_age)

if __name__=='__main__':
    c = CoupleManager()
    c.male = "장원"
    c.female="재연"
    print(c.diff)
    print(c.male)
    print(c.female)