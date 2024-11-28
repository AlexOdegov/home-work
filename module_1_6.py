my_dict={'Aleksandr':1982 , 'Aleksandra':1986,'Sophia':2013,'Andrey':1992}
print('Годы рождения:', (my_dict))
print('Год рождения: ', my_dict['Sophia'])
print('Год рождения: ',my_dict.get('Sergey'))
my_dict.update({'Egor':1985,'Anton':2002})
print('Год рождения: ',my_dict.pop('Andrey'))
print('Годы рождения: ',my_dict)
my_set={1,2,3,3,4,5,5,2,1,'Egor',False,False}
print('Множество: ',my_set)
my_set.add('Andrey')
my_set.add(6)
my_set.remove(False)
print('Множество: ',my_set)