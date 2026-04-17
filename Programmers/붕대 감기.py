# [PCCP 기출문제] 1번 / 붕대 감기
# 붕대를 감는 데 걸리는 시간과 초당 회복량, 추가 회복량이 담긴 배열 bandage, 초기 체력 health, 공격이 담긴 2차원 배열 attacks가 매개변수로 주어질 때, 공격이 모두 끝난 후의 체력을 return 하도록 solution 함수를 완성
# 단, 공격이 끝나기 전에 체력이 0 이하로 떨어지는 경우 -1을 return 한다.

# 몬스터 공격 시간과 time이 일치하는 경우 체력이 damage만큼 감소한다.
# 몬스터 공격 시간과 time이 일치하지 않는 경우 체력이 초당 회복량만큼 회복한다.
# 초당 회복량이 회복된 후, 붕대를 감는 데 걸리는 시간과 일치하는 경우 체력이 추가 회복량만큼 회복한다.

def solution(bandage, health, attacks):
    
    need_time = bandage[0]
    second_recover = bandage[1]
    plus_recover = bandage[2]
    max_health = health
    now_health = health
    
    
    n = attacks[len(attacks)-1][0]
    
    seq = 0
    idx = 0
    
    for time in range(1, n+1):
        attack_time = attacks[idx][0]
        damage = attacks[idx][1]
        
        
        if time == attack_time: # 공격이 일어나는 경우
            now_health -= damage
            idx += 1
            seq = 0
            if now_health <= 0:
                return -1
        else:  # 공격이 일어나지 않는 경우
            seq += 1
            now_health += second_recover
            
            if seq == need_time: # 붕대를 감는 데 걸리는 시간과 일치하는 경우
                seq = 0
                now_health += plus_recover
            
            now_health = min(now_health, max_health)
    
    return now_health
