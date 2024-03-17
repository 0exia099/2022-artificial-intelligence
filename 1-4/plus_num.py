#파일에 10개의 정수 난수 추가
import random

file = open("numbers.txt", "w")

for _ in range(10):
    file.write(str(random.randint(1,100)) + "\n")
    #print(random.randint(1,100), file=file) #같다

file.close()