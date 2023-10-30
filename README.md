# UNI_lang
유니랭은 세계 최초로 [아야츠노 유니](https://www.youtube.com/@ayatsunoyuni) 님의 방송 요소를 이용해 만들어진 난해한 프로그래밍 언어입니다.
이 혼종의 정체가 뭐냐고요? 저도 모릅니다. 아루빠냥!

>이 언어는  [정한 Ryucont](https://github.com/rycont) 님의 [엄랭](https://github.com/rycont/umjunsik-lang) 의 소스 코드를 가져와 개조한 언어입니다.  
>이 프로젝트는 엄랭을 갖고 놀던 한 초보 개발자의 스쳐 지나가는 생각에서 시작 된 간단한 작업물 입니다.  
>현재 기준, 엄랭과 명령어 및 작동 방식이 완전히 같습니다.  
>심지어 README도 ~~베꼈~~ 양식이 같게 만들었습니다.  
>원하는 개선사항 및 버그 등은 [Issues](https://github.com/Hyang-Dian/UNI_lang/issues)에서 꼭 말해주세요!  

```
안녕하시지

4챨입니다
4챨4스윽특대유유
나니4스윽?
나니고레?
4스윽비질게디질게
4챨4스윽니
욘서유유유유유

디비자시지
```

# 구현체
현재 파이썬으로만 구현되어 있습니다.  
다른 언어 구현 가능하신 분들의 많은 참여 부탁드립니다 :)


# 문법
유니랭은 아야츠노 유니 님의 밈/어록을 기반으로 한 키워드들을 사용합니다.  
모든 프로그램은 "안녕하시지"로 시작하며, 항상 "디비자시지"로 끝나야 합니다.

# 자료형
정수: "유", "니", "특대"의 세 가지 키워드를 사용합니다.  
### 연산자

 - 1 증가 : `유`
 - 1 감소 : `니`
 - 곱하기 : `특대`
```
유유유 => 3
니니니 => -3
유니 => 0
유유특대유유 => 4
유특대니 => -1
```

# 변수
변수는 인덱싱(정수)를 통해 접근하고 대입할 수 있습니다.  
지정되지 않은 모든 변수의 초기값은 0입니다.
### 대입(챨)
`N챨`의  형태로 N 번째 변수에 대입합니다. (N = 정수)  
단, N는 4부터 시작합니다.
```
4챨 => 1번째 변수에 0 지정
5챨유 => 2번째 변수에 1 지정
4챨니 => 1번째 변수에 -1 지정
```
### 사용(스윽)
`N스윽`의 형태로 N번째 변수를 불러옵니다.
```
4스윽 => 1번째 변수
5스윽 => 2번째 변수
6스윽 => 3번째 변수
```
# 콘솔
### 입니다
콘솔에서 정수를 입력받습니다.
```
4챨입니다 => 콘솔에서 입력받아서 1번째 변수에 대입한다.
5챨입니다 => 콘솔에서 입력받아서 2번째 변수에 대입한다.
```
### 나니?
콘솔에 정수를 출력합니다.
```
나니유유? => 콘솔에 2 출력
나니4스윽? => 콘솔에 1번째 변수 출력
```
## 나니고레?
콘솔에 문자를 출력합니다.   
`나니고레`와 `?` 사이에 오는 정수를 유니코드 문자 ~~(그러고보니 여기도 유니네)~~ 로 변환하여 콘솔에 출력합니다.  
`나니고레`와 `?` 사이에 정수가 주어지지 않으면 개행합니다 (나니고레? => `\n`)
```
나니고레유유유유유유유유유유특대유유유유유유유유유유?
=> 콘솔에 d 출력
```
# 지시문
### 비질게
`{정수}비질게{실행할 명령}`의 형태로 작성합니다.  
정수가 0이라면 `실행할 명령`이 실행되며, 그렇지 않다면 다음 줄로 넘어갑니다.
### 비질게라고할뻔 (NEW 23.10.21)
`{정수}비질게라고할뻔{실행할 명령}`의 형태로 작성합니다.
정수가 0이 아니라면 `실행할 명령`이 실행되며, 그렇지 않다면 다음 줄로 넘어갑니다.
### 욘서
`욘서`뒤에 오는 정수번째 줄로 이동합니다.  
`욘서유유유 => 3번째 줄로 이동`   
원라인코드의 경우에는 `~`로 분리된 코드단위로 카운트하여 이동합니다.
### 디질게
프로그램을 즉시 종료합니다.   
(기존 엄랭에 있던 반환 기능은 현재 제거되어있습니다.)
# 주석
### \#
주석 처리는 줄의 맨 앞에 \#을 붙이며, 그 줄 전체를 주석 처리합니다.
현재 버전에서는 주석이 코드 뒤에 붙을 경우, 오류가 발생할 수 있습니다. 주의해주시길 바랍니다.
```
#이렇게 되면 주석 처리됩니다.

4챨유유유 #주석 <- 처럼 사용시 주석이 포함된 상태로 프로그램이 기동하여 오류가 발생할 수 있습니다.
```

# 기타
 - 확장자는 `.uniuni`입니다.
 - One-line 작성은 `\n`을 `~`로 치환합니다.
# To-Do
 - [x] 유니랭 구현
 - [ ] 추가 기능 구현 (~ing)
 - [ ] python 외의 프로그래밍 언어 환경 구현
# History
 - 2023.10.19 : 유니랭 v1 공개
 - 2023.10.21 : v1 1차 문법 정리 및 개선 , `비질게라고할뻔`추가
 - 2023.10.24 : 함수 호출 오류 수정, 각주처리 추가, [예제1(도트아트)](https://github.com/Hyang-Dian/UNI_lang/tree/03b855e90bd680cf896dd1db49de43c2dd641a47/%EC%98%88%EC%A0%9C/1%20-%20%EC%9C%A0%EB%8B%88%20%EB%8F%84%ED%8A%B8%EC%95%84%ED%8A%B8)추가.

# Thanks 
> 원작 프로젝트 기획자 [정한 Ryucont](https://github.com/rycont) 님 및,  
> 원작 프로젝트에 참여하신 많은 [능력자 분들](https://github.com/rycont/umjunsik-lang/blob/master/README.md#contributors-)

# Contact
> Discord : hyang_dian
> X : @Hyang_Dian
