"""
#11654
알파벳, 소문자, 대문자, 숫자 0-9 중 하나가 주어졌을 때 주어진 글자의 아스키 코드값을 출력하는 프로그램 작성
"""

print(ord(input())) #ord : 문자열 -> 아스키
print(chr(input())) #chr : 아스키 -> 문자열

#11720
"""
N개의 숫자가 공백 없이 쓰여있다. 
이 숫자를 모두 합해서 출력하는 프로그램을 작성
"""

N = int(input())
num_list = sum(map(int, input()))

print(num_list)