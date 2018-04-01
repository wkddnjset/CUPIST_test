from django.db import models

# 키 필드에서 최대, 최소값을 정해주기 위한 함수
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save, pre_save
import re

from django.forms import ValidationError
# Create your models here.


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('경도, 위도 좌표 포맷이 아닙니다.')

def name_validator(value):
    if re.match('[^가-힣]+', value):
        raise ValidationError('한글 포맷으로 입력해야 합니다.')
    if not (len(value) == 2) or (len(value) == 3):
        raise ValidationError('2글자 혹은 3글자로 적어주세요.')

def job_validator(value):
    if re.match('[^가-힣a-zA-Z]+', value):
        raise ValidationError('한글, 영문 대소문자만 입력 가능합니다.')
    if not (len(value) <= 10):
        raise ValidationError('10글자 이내로 작성해야합니다.')

########################################################################################################
###################################               Male               ###################################
########################################################################################################

# Male 테이블
class Male(models.Model):
    name     = models.CharField(max_length=5, validators = [name_validator])
    birthday   = models.DateField()
    height = models.IntegerField(validators=[MinValueValidator(160), MaxValueValidator(200)])
    job = models.CharField(max_length=10, validators = [job_validator])
    # 함수를 넘겨서 위도, 경도에 대한 유효성 검사 실행
    location = models.CharField(max_length=50, validators = [lnglat_validator])
    hobbys = models.CharField(max_length=250, null=True, blank=True)
    is_fulled = models.BooleanField()

    def __str__(self):
        return str(self.name)

########################################################################################################
###################################              Female              ###################################
########################################################################################################

# Male 테이블
class Female(models.Model):
    name     = models.CharField(max_length=5, validators = [name_validator])
    birthday   = models.DateField()
    height = models.IntegerField(validators=[MinValueValidator(150), MaxValueValidator(190)])
    job = models.CharField(max_length=10, validators = [job_validator])
    # 함수를 넘겨서 위도, 경도에 대한 유효성 검사 실행
    location = models.CharField(max_length=50, validators = [lnglat_validator])
    hobbys = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)


# 딕셔너리 형태로 한번에 replace하는 함수
def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

# save 되기 전에 입력된 취미 데이터를 읽어 리스트로 다시 저장한다.
def hobby_pre_save(sender, instance, *args, **kwargs):
    rep =  {"[": "", "]": "", "'": "", " ": ""}
    instance.hobbys = multiple_replace(instance.hobbys, rep)
    instance.hobbys = instance.hobbys.split(",")

def male_post_save(sender, instance, *args, **kwargs):
    json_data = "{"
    json_data += '\n "name" : "' + instance.name
    json_data += '"\n "birthday" : "' + instance.birthday.strftime('%Y-%m-%d')
    json_data += '"\n "height" : "' + str(instance.height)
    json_data += '"\n "job" : "' + instance.job
    json_data += '"\n "location" : "' + instance.location
    json_data += '"\n "hobbys" : "' + str(instance.hobbys)
    json_data += '"\n "is_fulled" : "' + str(instance.is_fulled) + '"\n'
    json_data += "}"
    print(json_data)

def female_post_save(sender, instance, *args, **kwargs):
    json_data = "{"
    json_data += '"\n "name" : "' + instance.name
    json_data += '"\n "birthday" : "' + instance.birthday.strftime('%Y-%m-%d')
    json_data += '"\n "height" : "' + str(instance.height)
    json_data += '"\n "job" : "' + instance.job
    json_data += '"\n "location" : "' + instance.location
    json_data += '"\n "hobbys" : "' + str(instance.hobbys) + '"\n'
    json_data += "}"
    print(json_data)

pre_save.connect(hobby_pre_save, sender=Male)
post_save.connect(male_post_save, sender=Male)
pre_save.connect(hobby_pre_save, sender=Female)
post_save.connect(female_post_save, sender=Female)

