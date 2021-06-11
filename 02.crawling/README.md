# Java_Study

- <절차지향과 객체지향>
  - 절차지향 : 프로그램의 실행 절차에 중점을 둔 프로그래밍의 일종
    - 장점 : 컴퓨터의 처리구조와 유사해 실행속도가 빠름
    - 단점 : 1. 코드의 수정이 어려움
             2. 유지보수가 어려움
    - 언어) C언어
  - 객체지향 : 프로그램에서 다수의 "객체"를 만들고, 이들이 서로 상호작용을 통해 만들어지는 방식이다.
    - 장점 : 1.상속을 통해 프로그래밍시 코드의 재사용을 높일 수 있음
             2.프로그램 수정시 추가, 수정을 하더라도 캡슐화를 통해 주변 영향이 적기때문에 유지보수가 쉬움
    - 단점 : 캡슐화와 격리구조에 때문에 실행속도가 느리다.
    - 언어) Java, JavaScript, Python, C#

<br>

- <Value Type / Reference Type>
  - Value Type : 자신이 직접 데이터를 저장해서 보관
    - ex) int x  = 10; // int, char, double...
  - Reference Type : 데이터가 있는 위치만 자신이 가지고 있다가 필요할때 그 데이터가 있는 곳으로 가서 데이터를 가져옴
    - ex) Member mem = new Member(); // Class, Array, Interface..

<br>

- hashcode()
  - 객체의 주소값을 변환하여 생성한 객체의 고유한 정수값
    - ex) String str1 = new String("안녕"); <br>
          String str2 = new String("안녕");  
          String str3 = new String("안녕");  
          str1과 str2는 객체는 달라도 hashcode는 동일 / str3은 다름

<br>

- <오버로딩 & 오버라이딩>
  - Overloading(오버로딩)
    - 같은 이름의 메소드 여러개 정의
    - 매개변수의 타입이나 개수가 다름
  - Overriding
    - 부모클래스의 메소드를 자식클래스에서 재정의

<br>

- Generics(제네릭)
  - 클래스나 메소드에서 사용할 내부 데이터 타입을 일반화하는것
  - ex) MyArray<Integer> myArr = new MyArray<Integer>();
    - 타입의 안정성 향상
    - 타입체크와 형변환을 생략할 수 있으므로 코드가 간결

<br>

- 문자형 배열의 오름차순 & 내림차순
  - 오름차순 : Arrays.sort(배열변수명);
  - 내림차순 : Arrays.sort(배열변수명, Collections.reverseOrder());
  - 출력 : Arrays.toString(배열변수명)

  
======= 2021년 06월 08일 ========
