file = open("scores.txt", "r+", encoding="utf-8")
#r+ -> write만하면 파일 맨처음에 몇바이트를 덮어씀. read하고 write하면 파일 맨뒤에 write한다.(왜인지 모름)
sum = 0
count = 0
for line in file:
    sum += float(line)
    count += 1
    
print(f"평균값 = {sum/count}", file=file)
file.close()