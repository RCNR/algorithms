# 기적의 매매법 20546
# 준현 : 주식 살 수 있으면 무조건 사기
# 성민 : 3일 연속 가격 상승 -> 전량 매도 <-> 3일 연속 가격 하락 -> 전량 매도
# 성민이의 조건이 쫌 까다롭다.
# 현재 날짜 기준 가격이 상승했는지, 하락했는지 확인 필요

num = int(input())
board = list(map(int, input().split()))

jun_money = num
jun_res = 0

sung_money = num
sung_res = 0

up = 0
down = 0

for i in range(len(board)):
    cost = board[i]
    if cost <= jun_money:
        jun_res += jun_money // cost
        jun_money = jun_money % cost
    
    if i > 0 and board[i] > board[i-1]: up+=1
    else: up = 0
    
    if i > 0 and board[i] < board[i-1]: down+=1
    else: down = 0

    if down == 3 and cost <= sung_money: # 전량 매수
        sung_res += sung_money // cost
        sung_money = sung_money % cost
        down = 0

    elif up == 3 and sung_res != 0: # 전량 판매
        sung_money += sung_res * cost
        sung_res = 0
        up = 0

jres = jun_money + board[13] * jun_res
sres = sung_money + board[13] * sung_res

if jres > sres:
    print("BNP")
elif jres < sres:
    print("TIMING")
else:
    print("SAMESAME")