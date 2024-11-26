immutatable_var=1,2,3,'man',False
print(immutatable_var)
#immutatable_var[0]=9  #Объекты типа 'tuple не поддерживают изменение
mutable_list=['a','b','c',34,25,'Code'] #Создаем список
mutable_list[5]='decode' #Изменяем элемент списка
print(mutable_list) #Выводим на экран измененный список
