n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    burst = int(input(f"Enter the burst time of process {i+1}: "))
    priority = int(input(f"Enter the priority of process {i+1}: "))

    processes.append({
        'id': i+1,
        'burst': burst,
        'priority': priority
    })


processes.sort(key=lambda x: x['priority'])

total_time = 0
total_waiting = 0

for p in processes:
    total_time += p['burst']
    p['completion'] = total_time
    p['turnaround'] = p['completion']  # arrival time = 0
    p['waiting'] = p['turnaround'] - p['burst']
    total_waiting += p['waiting']

print("\nProcess ID  Waiting Time  Turnaround Time")
for p in sorted(processes, key=lambda x: x['id']):
    print(f"{p['id']:>10} {p['waiting']:>13} {p['turnaround']:>17}")

avg_waiting = total_waiting / n
print(f"\nAverage waiting time: {avg_waiting:.2f}")
