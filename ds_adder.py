# ds_adder.py

import sys #실행할 때 커맨드 라인에서 전달된 인자들을 읽어오기 위해 sys모듈을 import함

#커맨드 라인에서 전달된 인자들을 정수로 바꿔줌
num0=int(sys.argv[1])
num1=int(sys.argv[2])

#계산 및 출력
print('몫:',(num0//num1))
print('나머지:',(num0%num1))
