def solution(grid):
    answer = []
    
    row = len(grid)
    column = len(grid[0])
    
    # grid[r][c]의 4방향의 방문 여부를 담은 vec
    vec = [[[False for _ in range(4)] for _ in range(column)] for _ in range(row)]
    
    for r in range(row):
        for c in range(column):
            for k in range(4):
                # 해당 벡터가 이미 사용된 벡터면 패스
                if vec[r][c][k] == True:
                    continue
                
                count = 0
                
                now_r = r
                now_c = c
                now_k = k
                while(True):
                    if (vec[r][c][k] == False and k==0):
                        now_k=0
                    elif (vec[r][c][k] == False and k==1):
                        now_k=1
                    elif (vec[r][c][k] == False and k==2):
                        now_k=2
                    elif (vec[r][c][k] == False and k==3):
                        now_k=3
                    else:
                        if (now_k==0 and grid[now_r][now_c]=='S') or (now_k==2 and grid[now_r][now_c]=='R') or (now_k==3 and grid[now_r][now_c]=='L'):
                            now_k=0
                        elif (now_k==1 and grid[now_r][now_c]=='S') or (now_k==2 and grid[now_r][now_c]=='L') or (now_k==3 and grid[now_r][now_c]=='R'):
                            now_k=1
                        elif (now_k==2 and grid[now_r][now_c]=='S') or (now_k==0 and grid[now_r][now_c]=='L') or (now_k==1 and grid[now_r][now_c]=='R'):
                            now_k=2
                        else:
                            now_k=3

                    
                    if vec[r][c][k] == True:
                        if now_r==r and now_c==c and now_k==k:
                            break
                    if now_k==0:
                        # 위로
                        vec[now_r][now_c][0] = True
                        now_r -= 1
                        if now_r == -1:
                            now_r += row
                    elif now_k==1:
                        # 아래로
                        vec[now_r][now_c][1] = True
                        now_r += 1
                        if now_r == row:
                            now_r = 0
                    elif now_k==2:
                        # 왼쪽으로
                        vec[now_r][now_c][2] = True
                        now_c -= 1
                        if now_c == -1:
                            now_c += column
                    else:
                        # 오른쪽으로
                        vec[now_r][now_c][3] = True
                        now_c += 1
                        if now_c == column:
                            now_c = 0
                    count += 1
                
                answer.append(count)
                        
    return answer

print(solution(["SS"]))
