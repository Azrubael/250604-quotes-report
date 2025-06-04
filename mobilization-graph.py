import openpyxl
import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

# Функція для очищення і отримання повного імені
def clean_name(full_name):
    result = ''
    try:
        result = ' '.join(full_name.split()).strip()
    except Exception as e:
        print(f"Помилка при очищенні імені: {e}")
    return result


prefix_path = '/home/az/Documents/'
shpk = '250513-ШПК.xlsx'
shpk_file = prefix_path + shpk

try:
    shpk_wb = openpyxl.load_workbook(shpk_file)
    shpk_ws = shpk_wb.active
except Exception as e:
    print(f"Помилка відкриття {shpk_file}: {e}")
    exit(1)

# Створити словник для зберігання даних з shpk_file
shpk_data = {}
mobilized_count = defaultdict(int)

for row in shpk_ws.iter_rows(min_row=5, values_only=True):  # Пропустити заголовки ШПК
    if row[6]:
        department = row[0]                 # Стовпчик A - підрозділ
        position = row[2]                   # Стовпчик C - посада
        rank = row[5]                       # Стовпчик F - звання
        full_name = clean_name(row[6])      # Стовпчик G - повне ім'я
        mobiliz_date = row[7]               # Стовпчик H - дата мобілізації

        # Перетворити дату мобілізації на місяць і рік
        if isinstance(mobiliz_date, datetime):
            month_year = mobiliz_date.strftime("%Y-%m")
            mobilized_count[month_year] += 1

        shpk_data[full_name] = {
            'department': department,
            'rank': rank,
            'position': position,
            'mobiliz_date': month_year
        }


pretty_json = json.dumps(shpk_data, indent=2, ensure_ascii=False)
print(pretty_json)

# Підготовка даних для графіка
months = sorted(mobilized_count.keys())
counts = [mobilized_count[month] for month in months]

# Створення стовпчастого графіка
plt.figure(figsize=(10, 6))
plt.bar(months, counts, color='skyblue')
plt.xlabel('Місяць')
plt.ylabel('Кількість мобілізованих')
plt.title('Кількість мобілізованих по місяцях')
plt.xticks(rotation=45)
plt.tight_layout()

# Збереження графіка у файл
graph_file = 'pics/mobilization_chart.png'
plt.savefig(graph_file)
plt.close()
print(f'Графік збережено в файл {graph_file}')