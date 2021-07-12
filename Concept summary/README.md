
<div align="center" id="top">
<img height="270px" width="270px" src="./logo.png"><br>
  <h1>📃개념 및 궁금증 정리</h1>
</div>

***


<div align="center" id="top">
  <h1> 📖파이썬</h1>
</div>

### 내장함수 (built-in function)
   파이썬 내장 함수들은 외부 모듈과는 달리 import를 필요로 하지 않는다.
  
### str()
- 문자열 형태로 객체를 반환하여 리턴하는 함수이다.
```
>>> str(3)
'3'
>>> str('hi')
'hi'
>>> str('hi'.upper())
'HI'
```

### 포함 연산
포함 연산은 해당 값이 iterable한 두 번째 인수에 포함되는지의 여부를 반환한다. not in 연산자는 반대의 논리를 수행한다. 포함 연산의 결과는 bool 타입이다.
- in
- not in

### is와 ==의 차이
- is는 비교하는 대상이 같은 객체일 경우에 True를 반환
- ==는 비교하는 대상의 값이 같은 경우에 True를 반환
- 즉 is가 더 좁은 비교이다
