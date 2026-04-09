import random
import sys

class Cookie:
    pass

a = Cookie()
b = Cookie()

a.pp = 4
b.pp = 3

class Fourcal: # self는 객체 지정일 뿐 파라미터 X
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
a = Fourcal(4, 2)
print(a.mul())

a.setdata(100, 200)
print(a.add())

class SafeFourcal(Fourcal):
    def div(self): # 예외처리
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
def gugu(n):
    return [n * i for i in range(1, 10)]

print(gugu(10))

result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)

def get_total_page(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(25, 10))
print(get_total_page(30, 10))

nums = random.sample(range(1, 10), 3)
count = 0

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt','r')
    memo = f.read()
    f.close()
    print(memo)

# fn1 = sys.argv[1]
# fn2 = sys.argv[2]

# file1 = open(fn1, "r")
# file2 = open(fn2, "w")

# a.file1.read()
# file1.close()

# a = a.replace("\t","_")

# file2.write(a)
# file2.close()

while True:
    question = input("3자리 숫자를 입력하세요: ")
    guess = list(map(int, question))
    count += 1

    strike = 0
    ball = 0

    for i in range(3):
        if guess[i] == nums[i]:
            strike += 1
        elif guess[i] in nums:
            ball += 1

    if strike == 3:
        print(f"정답! {count}번 만에 맞혔습니다.")
        break

    print(f"{strike}스트라이크 {ball}볼")

def caesar(word, key):
    result = ""
    for char in word:
        num = ord(char) - ord('A')
        shifted = (num + key) % 26
        result += chr(shifted + ord('A'))
    return result

word = input("문자열을 입력하세요: ")
key = int(input("밀 칸 수를 입력하세요: "))

print(f"암호화: {caesar(word, key)}")    