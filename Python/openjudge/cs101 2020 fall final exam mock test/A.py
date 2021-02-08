foot = int(input())
if foot % 4 == 0:
    outmax = int(foot / 2) if int(foot / 2) > int(foot / 4) else 0
    outmin = int(foot / 4) if int(foot / 2) > int(foot / 4) else 0
else:
    outmax = int(foot / 2) if int(foot / 2) > foot // 4 + 1 else 0
    outmin = foot // 4 + 1 if int(foot / 2) > foot // 4 + 1 else 0
print(outmin, end = " ")
print(outmax)