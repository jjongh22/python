# statement와 expression 정의 및 차이_202235975_서정희

#varialbe = expression (statement)

# statement(문장): entire line of code. 한 줄의 코드에 있는 문장을 말한다. 문장은 파이썬 코드에서 실행가능한 최소한의 단위이다. 문장은 어떤 작업을 수행하거나 어떤 동작을 나타낸다. statement에는 하나 이상의 expression과 varialble로 구성되어져 있다. 모든 expression은 statement이지만, 모든 statement가 expression은 아니다.

# expression(표현식): 계산식을 말한다. 즉, 값을 반환하는 코드이다. varialble에 의해 할당된 value라고 볼 수 있으며, 계산되어진 값이다. 즉, 하나의 value로 reduce 된다.

# statement(문장), expression(표현식)의 차이: expression은 하나의 value로 reduce 되지만, statement는 그렇지 않다. statement는 값이 아닌 문장을 생각하면 되고, expression은 하나의 값을 생각하면 된다. 요약하면, expression은 값을 계산하는데 사용되고, statement는 어떤 작업을 수행하는데 사용되는 것(각각의 문장)이다.

# statement, expression example code
# ex1
x=5 #statement, expression
y=x+5 #statement, expression
print(y) #statement
# ex2
x=3 #statement(할당문), expression
if x>0: #statement(조건문)
    print('P') #statement(함수 호출)
# ex3
a=5 #expression, statement
b=a**2*3 #expression, statement
# ex4
def func(x):
    return x*2 #return value가 있는 function call도 expression이다.
# ex5 
def introduce(name,number):
    print('Hello,',name)
    print('Your code number is',number)
introduce('jh',1234) #statement

#할당문, 조건문, 정의문, 함수 등은 statement이고, 어떠한 value를 나타내거나 계산을 나타내는 것, 예를 들면 'x=3', 'y=x-1'은 expression이다. 다만 모든 expression은 statement이기 때문에 계산식은 expression이면서 statement이다.

