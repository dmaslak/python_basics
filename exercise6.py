# Упражнение 6


# Объявляем нужные переменные
first_day_result = int(input('Сколько километров пробежал спорстмен в первый день?'))
desired_result = int(input('Какой желаемый результат в километрах?'))
number_of_days = 1

print(f'В 1 день спортсмен пробежал {first_day_result} километра')

# Сам цикл
while first_day_result < desired_result:
    number_of_days +=1
    first_day_result = round(first_day_result * 1.1, 2)
    print(f'В {number_of_days} день спортсмен пробежал {first_day_result} километра')
    
    
print(f'Ответ: спортсмен достиг желаемого результата в {desired_result} км на {number_of_days} день.')


