# 1. Python 예약어

Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하시오.

- False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

# 2. 실수 비교

python은 부동소수점 방식을 이용하여 실수(float)를 표현하는 과정에서, 나타내고자 하는 값과의 오차가 발생하여 원하는대로 연산 또는 비교가 되지 않을 때가 있다. 이를 참고하여, 아래와 같은 두 실수 값을 올바르게 비교하기 위한 코드를 작성하시오.



```python
num1 = 0.1 * 3
num2 = 0.3
math.isclose(num1, num2)

#아래도 가능
abs(num1-num2) <= 1e-10
```





# 3. 이스케이프 시퀀스

1) 줄바꿈: \\n

2) 탭: \\t

3) 백슬래시: \\\



# 4. String Ineterpolation

'안녕, 철수야'를 string interpolation을 사용하여 출력하시오.

```python
name = '철수'

print(f'안녕, {name}야')

#fstring이 항상 제일 좋음
```



# 5. 형 변환

다음 중, 실행 시 오류가 발생하는 코드를 고르시오.

```python
int('3.5')
```



# 6. 네모 출력

두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 *문자를 이용하여 출력하시오. 단 반복문은 사용할 수 없다.

```python 
n = 5 #가로
m = 9 #세로
rec = (('*'*5)+'\n')*m
print(rec)
```

# 7. 이스케이프 시퀀스 응용

print() 함수를 한 번만 사용하여 다음 문장을 출력하시오.

```python
print(\"파일은 c:\\Windows\\users\\내문서\\Python에 저장이 되었습니다.\")
```



# 8. 근의 공식

다음은 이차방정식의 근을 찾는 수식이다. 이를 파이썬 코드로 작성하시오.

```python
a = int(input())
b = int(input())
c = int(input())
roots=[0,0]
roots[0]=(-b+pow((pow(b,2)-4*a*c),0.5))/(2*a)
roots[1]=(-b-pow((pow(b,2)-4*a*c),0.5))/(2*a)
print(roots)
if roots[0]==roots[1]:
    print("중근입니다.")
```