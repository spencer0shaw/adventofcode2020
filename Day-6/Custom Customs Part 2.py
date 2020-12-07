with open("data.txt") as infile:
    lines = [line.strip() for line in infile]
score = 0
single_answer = set()
new = True
for line in lines:
    if not line:
        score += len(single_answer)
        single_answer = set()
        new = True
        continue
    if not new:
        single_answer = set(line) & single_answer
    else:
        new = False
        single_answer = set(line)
if single_answer:
    score += len(single_answer)
print(score)
