#친구 네트워크 
"""
문제
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

n: 테스트 케이스 개수 
f: 친구 관계 수 

for 테스트 개수 만큼(n):
    for 친구관계수 만큼(f):
        친구 이름 두개 받아서 대표노드 업데이트(유니온)

0 1 2 3 4    
0 1 2 3 1
0 1 2 2 1
0 1 1 1 1  
1 1 1 1 1 

#find연산할때 처음 찾아들어갈때(재귀)는 관계수+2 다음의 연결에서는 +1 
#사이클 허용하면안될거같음 -> 노드 수=관계수+1
#새로운 테스트 케이스를 받을때 parent, 이름 딕셔너리, 관계수 초기화 

"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())


def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        if a>b:
            parent[a] = b
        else:
            parent[b] = a 

for _ in range(n):
    #init 
    f = int(input())
    parent = [i for i in range(f+1)]
    dict = {} #이름 -> 숫자 매핑(0~f)
    for _ in range(f):
        a,b = input().split() 
        #딕셔너리로 변환 NameToNum(a,b)
        #union(a,b)


def NameToNum(f1,f2):
    #딕셔너리에 있는 놈이면 패스 아닌놈은 추가하고 인덱스 증가 
    if f1 not in dict:
        