# 시간 조심

def check_time(t):
    k = t % 100
    if k >= 50 and k <= 59:
        return t + 50
    return t + 10

def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        wanted_time = check_time(schedules[i])
        is_late = False
        day = startday
        
        for j in range(7):
            if day != 6 and day != 7:
                if timelogs[i][j] > wanted_time:
                    is_late = True
                    break
            day += 1
            if day == 8: day = 1
        
        if is_late == False:
            answer += 1
    
    return answer
        