import json

# Открываем файл
with open('companies.txt', 'r') as fp:
    raw_list = fp.readlines()

# Создаём список с чистыми данными
companies_list = [company.strip().split() for company in raw_list]

# Считаем прибыль для каждой компании и добавляем в конец списка
for company in companies_list:
    profit = int(company[2]) - int(company[3])
    company.append(profit)

profits_dict = {company[0]: company[4] for company in companies_list if company[4] >= 0}
losses_dict = {company[0]: company[4] for company in companies_list if company[4] < 0}
    
# Рассчитываем среднюю прибыль
companies_with_profit = [company for company in companies_list if company[4] > 0]
total_profit = 0
for company in companies_with_profit:
    total_profit += company[4]

avg_profit_dict = {'average_profit': total_profit / len(companies_with_profit)}

# Формируем финальный список и сохраняем его в json
final_list = [profits_dict, avg_profit_dict, losses_dict]

with open('exercise7.json', 'w') as fp:
    json.dump(final_list, fp)





    
