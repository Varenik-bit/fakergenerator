from faker import Faker
# импортируем библиотеки

faker = Faker('RU') # задаём язык

print('Здравствуйте! Выберите сколько людей вы хотите сгенерировать!') # приветствуем
user_people = int(input()) # принимаем ввод количества сгенерированных людей

for i in range(user_people): # задаем цикл для получения большого списка людей

    name = faker.name() # генерируем имя
    address = faker.address() # генерируем адрес
    email = faker.email() # генерируем email
    job = faker.job() # генерируем работу

    print(f'{name}\n{address}\n{email}\n{job}\n') # выводим информацию о человеке
