'''
과제 1. 별찍기 (4월 20일까지)
- 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요
**********
*********
********
*******
*****
****
***
**
*
'''

n=0
while True:
    n+=1
    if n>9 : break
    i=10-n
    print('*'* i)
'''
과제 2. 구구단 (4월 20일까지)
- 구구단 2단을 출력해보세요!
'''

for i in range(1,10):
    print(2*i, end=" ")
    

#과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 20일까지)

result=0
for n in range(1,1000):
    if n%3==0:
        result+=n
print(n)


#과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)

mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
for score in mutsa_scores:
    result+=score
print(result/8)

#과제 5. input.py 문제 2개 풀기 (4월 20일까지)




