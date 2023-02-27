def sya_abouMe():
    print("I am Abu Al Shahriar Rifat");
sya_abouMe();
def myProfile():
    print('I am working as a software Engineer');
myProfile();

def greedingFunction():
    print("Hi I am a full stack web application developer");
greedingFunction();

def mynameIs(name):
    print(f'Hey my Name is {name}');
mynameIs('Abu Al Shahriar Rifat');

##Default arguments
def myFullName(name="Abu Al Shahriar Rifat"):
    print(f'My Name is {name}');
myFullName("Rifat")

##names arguments

'''
Takes 2 integers,returs their sum
'''
def sum(a,b):return a+b;
def add(a,b):return a+b;
different=sum(100,20)-add(100,3);


def calculateFoodTotal(foodAmount,tip_parcentage):
    tipamount=foodAmount*(tip_parcentage/100)
    print(tipamount)
    TotalAmount=foodAmount+tipamount
    return TotalAmount;
print(calculateFoodTotal(foodAmount=200,tip_parcentage=10))

def WeotherToEmoji(wather:str):
    if wather=="rainy":
        print("Today is raiing");
    elif wather=='cloudy':
        print('Today is cloudy');
    elif wather =='thunderstom':
        print("I have seen thunderstom in my own eyes");
    else:
        print("Today is Sunny day");
WeotherToEmoji('rainy');


def mysum(a:int,b:int):return a+b;
print(mysum(20,30));

def maximum(a,b):
    if a>b:
        return a;
    else:
        return b;

##Lamda function
def sum(a,b):return a+b;
sum_2=lambda a,b:a+b;
print(sum_2(10,20))
sum_3=lambda a,b:a/b;
print(sum_3(20,2))


def textSum():
    assert sum(1,2)==3
    assert sum(-20,30)==40
    assert sum(560,780)==1340
    print("I am a full stack developement");














