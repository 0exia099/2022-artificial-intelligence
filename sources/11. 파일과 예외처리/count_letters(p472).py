##
#	이 프로그램은 파일 안의 문자들을 알바벳순으로 출력 : sorted.
#

filename = input("파일명을 입력하세요: ").strip() #공백 제거
infile = open(filename, "r") # 파일을 연다.

freqs = {} #딕셔너리로 저장하는게 좋다

# 파일의 각 줄에 대하여 문자를 추출한다. 각 문자를 사전에 추가한다. 
for line in infile:
    for word in line.split():		# 양쪽 끝의 공백 문자를 제거한다. strip -> split되면 
        if word in freqs:		# 문자열 안의 각 문자에 대하여 
            freqs[word] += 1		# 딕셔너리의 횟수를 증가한다. 
        else:				# 처음 나온 문자이면
            freqs[word] = 1		# 딕셔너리의 횟수를 1로 초기화한다. 

print(sorted(freqs.items()))
infile.close()