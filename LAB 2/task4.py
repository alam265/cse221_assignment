data = open('input4.txt', 'r')
result = open('output4.txt', 'w')
n, w = data.readline().split()
n = int(n)
w = int(w)
wlist = [0]*w



start_time = []
end_time = []



for _ in range(n):
    startTime, endTime = data.readline().split(' ')
    start_time.append(int(startTime))
    end_time.append(int(endTime))

for i in range(len(start_time)):
    min_loc = i
    for j in range(i+1,len(start_time)):
        if end_time[j] < end_time[min_loc]:
            min_loc = j 
    end_time[i],end_time[min_loc] = end_time[min_loc],end_time[i]
    start_time[i],start_time[min_loc] = start_time[min_loc],start_time[i]




count = 1
wlist[0] = end_time[0]

for i in range(1,len(end_time)) :
    if int(start_time[i]) >= wlist[0] and int(start_time[i]) >= wlist[1] :
        if int(start_time[i]) - wlist[0] < int(start_time[i]) - wlist[1]:
            wlist[0] = int(end_time[i])
            count += 1

        else :
            wlist[1] = int(end_time[i])
            count += 1

    elif int(start_time[i]) >= wlist[0]:
        wlist[0] = int(end_time[i])
        count += 1

    elif int(start_time[i]) >= wlist[1] :
        wlist[1] = int(end_time[i])
        count += 1

    elif w > 2 and int(start_time[i]) >= wlist[2]:
        wlist[2] = int(end_time[i])
        count += 1



print(count)

result.write(f"{count}")

