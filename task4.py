import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

best = max(students, key=lambda x: x['grade'])

worst = min(students, key=lambda x: x['grade'])

total_grades = sum(s['grade'] for s in students)
average = round(total_grades / len(students), 1)

print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")
print(f"Eng past baho: {worst['name']} — {worst['grade']}")
print(f"O'rtacha baho: {average}")