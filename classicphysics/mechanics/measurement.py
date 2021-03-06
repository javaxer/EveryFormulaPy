#coding:utf-8

'''
길이의 단위와 그 전환에 대한 정의
내용은 모두 Serway물리 교과서 내용에서 발췌했음
처음에는 파일명을 Length라고 했으나 곰곰히 생각해 본 결과 정의(Standard)라고 정의하는 쪽이 더 정확할 것으로 보여
파일 명을 수정함.
'''

#물리학 교과서 1장에 나오는 물리학 측정(Physics and measurement)

import math

#기준에 대한 원시 클래스
class Standard:
    #생성자 정의(number는 양, unit은 단위)
    #모든 물리학 값에는 단위가 있어야 한다는 배움을 기억하는가?
    def __init__(self, number=0.0, unit='unit'):
        self.standard = number
        self.unit = unit

    #기준에 대한 정의 출력(예: '길이에 대한 정의', '무게에 대한 정의' 등등)
    def get_definition(self):
        print("기준에 대한 원시 클래스")

    #양을 지정하는 메소드
    def set(self,number):
        self.standard=number

    #양을 얻는 메소드
    def get(self):
        return self.standard

    #단위를 설정하는 메소드
    def set_unit(self,unit):
        self.unit=unit

    #단위를 얻는 메소드
    def get_unit(self):
        return self.unit

    #단위가 서로 일치 하지 않을 경우에 대한 예외 처리
    class UnitException(Exception):
        print("단위가 서로 불일치 합니다.")
        pass

    #합성에 대한 정의 __add__
    def __add__(self, other):
        if self.get_unit() != other.get_unit():
            raise UnitException()
        else add_result = self.get()+other.get()

        return self.add_result

    #기본 출력 형태는 양+단위 형태이다.
    def __str__(self):
        return "{} {}".format(self.standard,self.unit)

#단위를 비교하는 함수
def compare_unit(stand1,stand2):
    stand1_unit = stand1.get_unit()
    print(stand1_unit)
    stand2_unit = stand2.get_unit()
    print(stand2_unit)
    if stand1_unit == stand2_unit:
        return True
    else:
        return False

#SI단위계 표준 단위인 미터에 대한 정의
class Length(Standard):

    speed_of_light = 299792458              #광속(299,792,458 m/s)

    #길이에 대한 생성자, 기본 데이타는 0.0 m
    def __init__(self,length=0.0,unit='m'):
        self.standard=length
        self.unit=unit

    # 1m에 대한 물리적인 정의
    def get_definition(self):
        print("1미터(m)는 진공 속에서 빛이 1/",self.speed_of_light,"초 동안 진행한 거리이다.")
    def set_length(self,length):
        self.set(length)
    def get_lenght(self):
        return self.get()
    def get_speed_of_light(self):
        return self.speed_of_light

#아래의 클래스는 위 길이에 대한 클래스의 한글 클래스이다.
class 길이(Length):
    def 정의(self):
        self.get_definition()
    def 설정(self,number):
        self.set(number)
    def 획득(self):
        self.get()


class Mass(Standard):
    def __init__(self,mass,unit='kg'):
        self.standard=mass
        self.unit=unit

    #1kg에 대한 물리적인 정의
    def get_definition(self):
        print("1킬로그램(kg)은 프랑스 국제 도량형국에 보관되어 있는 특정한 백금-이리듐합금 실린더로 정의된다.")

#아래의 클래스는 위 질량에 대한 클래스의 한글 클래스이다.
class 질량(Mass):
    def 정의(self):
        self.get_definition()
    def 설정(self,number):
        self.set(number)
    def 획득(self):
        self.get()


class Time(Standard):
    #1sec에 대한 물리적인 정의
    def get_definition(self):
            print("1초(sec)는 세슘 원자로 부터 방축되는 복사 진동주기의 9,1,92,631,770배이다")

#아래의 클래스는 위 시간에 대한 클래스의 한글 클래스이다.
class 길이(Time):
    def 정의(self):
        self.get_definition()
    def 설정(self,number):
        self.set(number)
    def 획득(self):
        self.get()


#부피에 대한 정의, 기초적인 산수 영역이나 아래의 밀도에 대한 정의를 위해 추가한다.
class Volume(Standard):

#정육면체의 부피에 대한 공식
def set_square_volume(length_x,unit):
    square_volume = Volume(math.pow(length_x.get(),3),unit)
    return square_volume

# 직육면체에 부피에 대한 공식
def set_rectengular_volume(length_x, length_y, length_z,unit):
    rectengular_volume = Volume(length_x*length_y*length_z,unit)
    return rectengular_volume

class 부피(Volume):
    def 설정(self,number):
        self.set(number)
    def 획득(self,number):
        self.get(number)
    def 직육면체부피(self,length):
        self.get()

#밀도를 저장하기 위한 개체 클래스
class Density(Standard):

def get_density(self, mass, volume,unit):
    density = mass.get()/volume.get()
    return Density(density,unit)

class 밀도(Density):

class DimensionalAnalysis:
    #차원 분석에 대한 클래스, 현시점에서는 검증용 외에는 별다른 용도가 없으므로 일단 통과하자
    pass

#각도에 대한 개체
class Angle(Standard):
    def __init__(self,degree=0,unit='deg'):
        self.standard = degree
        self.unit = unit

    def get_definition(self):
        print("1도란 1회전의 360등분이다. 혹은 pi/180 라디안이다.")

def conversion_units():
    #단위 환산에 대한 내용, 일단 이 부분도 패스(SI단위만 사용할 거니까)
    pass
