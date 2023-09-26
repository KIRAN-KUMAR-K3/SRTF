def srtf(processes, n):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x[1])
    
    # Initialize variables
    total_time = 0
    completed = 0
    current_time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    while completed != n:
        shortest = -1
        min_remaining_time = float('inf')
        
        for i in range(n):
            if processes[i][1] <= current_time and processes[i][2] < min_remaining_time and processes[i][2] > 0:
                shortest = i
                min_remaining_time = processes[i][2]
        
        if shortest == -1:
            current_time += 1
        else:
            processes[shortest][2] -= 1
            current_time += 1
            
            if processes[shortest][2] == 0:
                completed += 1
                end_time = current_time
                waiting_time[shortest] = end_time - processes[shortest][1] - processes[shortest][0]
                turnaround_time[shortest] = end_time - processes[shortest][1]
    
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    
    print("Process\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{i+1}\t\t{processes[i][0]}\t\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    print(f"\nTotal Waiting Time: {total_waiting_time}")
    print(f"Total Turnaround Time: {total_turnaround_time}")
    print(f"Average Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    processes = []
    for i in range(n):
        burst_time = int(input(f"Enter burst time for process P{i+1}: "))
        arrival_time = int(input(f"Enter arrival time for process P{i+1}: "))
        processes.append([burst_time, arrival_time, burst_time])
    
    srtf(processes, n)
