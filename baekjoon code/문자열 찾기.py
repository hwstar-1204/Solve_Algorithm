#문자열 찾기 
"""
node 클래스 생성:
    isEnd(마지막 문자열 여부)
    childnode(자식노드)

trie 클래스 생성:
    parent(부모 노드 저장 변수)
    문자 삽입 함수:
        for 문자열 탐색:
            if 자식노드에 없는 문자면:
                신규 생성 
            자식 노드 문자로 이동 
            if 이번 문자열의 마지막 문자면:
                마지막 문자 표시 

    문자 찾기 함수:
        for 문자열 탐색:
            문자 탐색시 존재하지 않으면 false 리턴 
            마지막 문자까지 모두 존재하고 마지막 문자에 isEnd가 true인 경우 true 리턴 


n: 집합 S의 문자열 개수 , m: 검사할 문자열 개수 
trie 생성 

for n:
    문자열 삽입 함수 수행 

for n:
    문자열 찾기 함수 수행 
    if 단어를 찾았으면 정답값 1 증가 

정답 출력 
"""

from sys import stdin
input = stdin.readline

class Node(object):
    def __init__(self,isEnd):
        self.isEnd = isEnd 
        self.childNode = {}

class Trie(object):
    def __init__(self):
        self.parent = Node(None)

    def insert(self,string):
        nowNode = self.parent
        temp_length = 0
        for char in string:
            if char not in nowNode.childNode:
                nowNode.childNode[char] = Node(char)
            nowNode = nowNode.childNode[char]
            temp_length += 1
            if temp_length == len(string):
                nowNode.isEnd = True

    def search(self, string):
        nowNode = self.parent
        temp_length = 0
        for char in string:
            if char in nowNode.childNode:
                nowNode = nowNode.childNode[char]
                temp_length += 1
                if temp_length == len(string) and nowNode.isEnd:
                    return True
                else:
                    return False
        return False

n,m = map(int,input().split())
myTrie = Trie()

for _ in range(n):
    word = input().strip()
    myTrie.insert(word)

result = 0
for _ in range(m):
    word = input().strip()
    if myTrie.search(word):
        result += 1

print(result)

