import pandas as pd
import os
import random

# Создаём папку data, если её нет
os.makedirs("data", exist_ok=True)

# Две категории, как в твоём исходнике
categories = [
    "Курсы программирования",
    "Английский язык"
]

# Даты — каждый месяц 2024–2025
dates = pd.date_range(start="2024-01-01", end="2025-12-01", freq="MS")

rows = []

for date in dates:
    # Курсы программирования
    income_prog = random.randint(45000, 60000)
    expense_prog = random.randint(18000, 26000)
    students_prog = random.randint(100, 160)

    rows.append({
        "Дата": date.strftime("%Y-%m-%d"),
        "Категория": "Курсы программирования",
        "Доходы": income_prog,
        "Расходы": expense_prog,
        "Студенты": students_prog,
        "Прибыль": income_prog - expense_prog
    })

    # Английский язык
    income_eng = random.randint(28000, 38000)
    expense_eng = random.randint(9000, 16000)
    students_eng = random.randint(70, 110)

    rows.append({
        "Дата": date.strftime("%Y-%m-%d"),
        "Категория": "Английский язык",
        "Доходы": income_eng,
        "Расходы": expense_eng,
        "Студенты": students_eng,
        "Прибыль": income_eng - expense_eng
    })

# Сохраняем CSV
output_path = "data/education_finance.csv"
df = pd.DataFrame(rows)
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"Файл создан: {output_path}")
print(f"Количество строк: {len(df)}")
