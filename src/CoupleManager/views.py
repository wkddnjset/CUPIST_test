from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView

from math import sin, cos, sqrt, atan2, radians
import collections

# Create your views here.
# 딕셔너리 형태로 한번에 replace하는 함수
def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

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
        male_age = Male.objects.all().filter(name__icontains=self._male).values('birthday')[0]['birthday'].strftime('%Y')
        female_age = Female.objects.all().filter(name__icontains=self._female).values('birthday')[0]['birthday'].strftime('%Y')
        if male_age > female_age:
            return self._female+"님의 나이가 "+self._male+"님의 나이보다"+str(int(male_age)-int(female_age))+"살 많습니다."
        if male_age == female_age:
            return self._male + "님의 나이와 " + self._female + "님의 나이가 같습니다."
        if male_age < female_age:
            return self._male+"님의 나이가 "+self._female+"님의 나이보다"+str(int(female_age)-int(male_age))+"살 많습니다."

    # 거리계산 알고리즘
    def distance(self):
        male_location = Male.objects.all().filter(name__icontains=self._male).values('location')[0]['location']
        female_location = Female.objects.all().filter(name__icontains=self._female).values('location')[0][
            'location']
        male_latlon = male_location.split(",")
        female_latlon = female_location.split(",")
        r = 6376.0
        lat1 = radians(float(male_latlon[0]))
        lat2 = radians(float(female_latlon[0]))
        lon1 = radians(float(male_latlon[1]))
        lon2 = radians(float(female_latlon[1]))
        dlat = abs(lat2-lat1)
        dlon = abs(lon2-lon1)
        a = sin(dlat / 2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = r * c
        if int(distance) > 5:
            return self._male+"님과 "+self._female+"님은 "+ str(int(distance))+"Km 정도 떨어져있습니다."
        else:
            return self._male+"님과 "+self._female+"님은 5Km 이내에 위치하고 있습니다."

    # 동일한 취미 찾기
    def same_hobby(self):
        male_hobbys = Male.objects.all().filter(name__icontains=self._male).values('hobbys')[0]['hobbys']
        female_hobbys = Female.objects.all().filter(name__icontains=self._female).values('hobbys')[0][
            'hobbys']
        rep = {'[':'', ']':'', "'":"", " ":""}
        male_hobbys_list = multiple_replace(male_hobbys, rep).split(",")
        female_hobbys_list = multiple_replace(female_hobbys, rep).split(",")
        same_hobbys = len(set(male_hobbys_list).intersection(set(female_hobbys_list)))
        return self._male + "님과 " + self._female + "님은 "+str(same_hobbys)+"개의 동일한 취미를 갖고 있습니다."

    def fulfilled(self):
        male_fulfill = Male.objects.all().filter(name__icontains=self._male).values('is_fulled')[0]['is_fulled']

        if male_fulfill == False:
            result = "미필"
        else:
            result = "군필"
        return self._male + "님은 " + result +"자 입니다."

class UserList(TemplateView):
    template_name = 'CoupleManager/list.html'

    def get_context_data(self, **kwargs):
        female = self.request.GET.get('female', '')
        male = self.request.GET.get('male', '')

        # # 새로운 데이터를 만들때 새로운 ID!
        context = super(UserList, self).get_context_data(**kwargs)
        print(male)
        print(female)
        context['males'] = Male.objects.all()
        context['females'] = Female.objects.all()
        if female and male:
            couple = CoupleManager()
            couple.male = str(male)
            couple.female = str(female)
            dict = {}
            dict['error'] = "False"
            dict['male'] = male
            dict['female'] = female
            dict['diff'] = couple.diff()
            dict['distance'] = couple.distance()
            dict['hobbys'] = couple.same_hobby()
            dict['fulfilled'] = couple.fulfilled()


        else:
            dict = {}
            dict['error'] = "True"
            dict['message'] = "데이터가 없습니다."

        context["results"] = dict
        print(dict)
        # print("결과 : " + c.diff(male, female)[0]['birthday'].strftime('%Y'))
        return context