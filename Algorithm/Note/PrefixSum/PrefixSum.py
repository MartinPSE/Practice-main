from _lsprof import profiler_entry

n = 5
data = [10, 20, 30, 40, 50]

summary = 0
prefix_sum = [0]

for i in data:
    summary += i
    prefix_sum.append(summary)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
