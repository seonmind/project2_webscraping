# 정규식 regular expression
import re


p=re.compile("ca.e") # 정규식을 컴파일해서 p에다 저장하는것


# ca.e :문자 하나가 .에 들어감     cade case cafe careless
# ^ca  :로 시작                   cat camera
# se&  :로 끝남                   base 

# m=p.match("case") match: 주어진 문자열의 처음부터일치하는지 확인(뒷부분은 무관하게 일치 가능)

# print(m.group())

# if문으로 에러가 발생안하게 하기
def print_match(m):
    if m:
        print(m.group()) # group은 정규식과 일치하면 문자열 반환 아니면 에러
        print(m.string)  #입력받은 문자열
        print(m.start()) #일치하는 문자열의 시작 index
        print(m.end())   #일치하는 문자열의 끝 index
        print(m.span())  #일치하는 문자열의 시작과 끝 index
    else:
        print("error")

m=p.search("careful") # search: 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

lst=p.findall("good care cafe") #findall: 일치하는 모든 것을 리스트로 반환