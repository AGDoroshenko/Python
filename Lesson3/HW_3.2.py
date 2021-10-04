def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Doroshenko', name='Artem', year='1993', city='Saratov', email='a.g.doroshenko@mail.ru',
              telephone='8-927-110-75-77'))