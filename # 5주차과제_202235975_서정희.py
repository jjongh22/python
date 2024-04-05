# 5주차과제_202235975_서정희

def my_for(input_nm):  #for문을 사용하는 함수 정의
    result=[]          #빈 list 생성
    for i in input_nm: #각 요소 반복 과제를 수행하기 위한 준비
        result.append(i**3) #result list에 각 요소의 세제곱값을 추가함
    return result #my_for함수는 호출시 result list반환

def my_while(input_nm): #while문을 사용하는 함수 정의
    result=[]           #빈 list 생성
    idx=0               #list index 0부터 시작
    while idx<len(input_nm): #idx가 input_nm의 길이 미만일 때 까지 실행
        result.append(input_nm[idx]**3) #input_nm 각 요소 세제곱한 것을 result list에 입력
        idx+=1 #idx에 1을 더하여 다시 수행
    return result #result list 반환

def my_lambda(input_nm): #lambda문을 사용하는 함수 정의 
    return list(map(lambda x:x**3,input_nm)) #input_nm의 각 요소를 세제곱한 후 list로 만들어준다.
        
## 또 다른 map, lambda 이용
# my_lambda=input('숫자를 입력하시오(빈칸으로 구분).:').split() ##입력받은 숫자를 my_lambda list로 만듦
# my_lambda=map(int, my_lambda) ##만들어진 list의 str로 되어있는 각 요소들을 계산해주기 위해서 int로 변환. int(my_lambda)는  my_lambda가 이미 위 수행과정에서 list가 되었는데 list는 int로 변환해줄 수 없기 때문에 반복연산자인 map을 사용하여 각 요소를 int로 변경해주었다. 
# ml=map(lambda x: x**3, my_lambda) ##list의 각 요소들을 세제곱해주기 위해서 반복연산자인 map사용
# print(list(ml)) ##위의 각 요소들을 list로 묶어 출력함

def result(input_nm): #result 함수생성
    print('input:',input_nm) # input_nm출력
    print('input(my_for):',my_for(input_nm)) #my_for함수 호출
    print('input(my_while):',my_while(input_nm)) #my_while함수 호출
    print('input(my_lambda):',my_lambda(input_nm)) #my_lambda함수 호출
    
def main(): #main함수 정의
    input_nm=list(range(5,16)) #input_nm list 생성
    result(input_nm) #result함수 호출

if __name__=="__main__": #모듈로 가져와서 import하여 사용하지 못하게함.
    main() #main 함수 호출
    
    
