def RoundRobin(processes, burst_time, time_quantum):
    
    n = len(processes) # 프로세스의 수
    remaining_time = list(burst_time) # 각 프로세스의 남은 실행 시간
    turnaround_time = [0] * n # 각 프로세스의 완료 시간
    waiting_time = [0] * n # 각 프로세스의 대기 시간

    time = 0 # 현재 시간
    queue = [] # 라운드 로빈 스케줄링에 사용되는 대기 큐

    while True:
        all_completed = True # 모든 프로세스 종료 시 반복문 종료를 위한 플래그

        # 각 프로세스에 대해 순회하며 실행
        for i in range(n):
            if remaining_time[i] > 0: # 아직 실행할 남은 시간이 있는 경우
                all_completed = False # 모든 프로세스가 종료되지 않았음을 표시

                if remaining_time[i] > time_quantum: # 시간 할당량보다 남은 시간이 더 많은 경우
                    time += time_quantum # 현재 시간을 시간 할당량만큼 증가
                    remaining_time[i] -= time_quantum # 프로세스의 남은 실행 시간에서 시간 할당량을 감소
                    queue.append(i) # 대기 큐에 프로세스 추가
                else:
                    time += remaining_time[i] # 현재 시간을 남은 실행시간만큼 증가
                    turnaround_time[i] = time # 프로세스의 종료시간 기록
                    remaining_time[i] = 0 # 프로세스의 남은 실행시간을 0으로 설정(종료)
                    waiting_time[i] = turnaround_time[i] - burst_time[i] # 대기시간 계산

        if all_completed:
            break # 모든 프로세스가 종료되었을 경우 반복문 종료
    
    # 결과 출력
    print('process\tTurnaround Time\tWaiting Time')
    for i in range(n):
        print(f'p{i+1}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}')

# 함수 호출해 기능 확인하기
process = [1, 2, 3]
burst_time = [10, 5, 8]
time_slice = 2

RoundRobin(process, burst_time, time_slice)
