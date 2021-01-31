import json
import datetime
from operator import itemgetter

empDict= {'employees': []}
listBirth = []

# Search max date of birth
with open('datafile.py','r') as reader:
    list = reader.read().splitlines()
    reader.close()
    for i in list:
        # Work with the date of birth
        nonFormatDate =  i.split('"')[1].split('-')  #transforming date to list ['YYYY', 'MM', 'DD']
        formatDate = datetime.date(int(nonFormatDate[0]), int(nonFormatDate[1]), int(nonFormatDate[2]))
        listBirth.append(formatDate)
maxAge = max(listBirth)
#print(maxAge)

#Считаем количество полных лет на момент рождения самого младшего сотрудника
def get_age(birthday):
    age = maxAge.year - birthday.year
    if maxAge.month > birthday.month:
        age -= 1
    elif maxAge.month == birthday.month and maxAge.day > birthday.day:
        age -= 1
    return age

#Формируем JSON
with open('datafile.py','r') as reader:
    list = reader.read().splitlines()
    reader.close()
    for i in list:

        # Work with the date of birth
        nonFormatDate =  i.split('"')[1] #date from row
        nonFormatDate = nonFormatDate.split('-')  #transforming date to list ['YYYY', 'MM', 'DD']
        #print(f'nonFormatDate= {nonFormatDate}')
        formatDate = datetime.date(int(nonFormatDate[0]), int(nonFormatDate[1]), int(nonFormatDate[2]))
        #print(f'formatDate= {formatDate}')
        numberOfDays = datetime.date.today() - formatDate
        numberOfDays = str(numberOfDays).split() [0] #only days # Got the number of days from birth to the current date = numberOfDays

        empDict['employees'].append({
            "name": i.split(' =')[0].replace('_', ' '),
            "daysFromBirthday": numberOfDays,
            "fullAge": get_age(formatDate)
        })

# Sorting JSON by value of fullAge by descending
empDict['employees'] = sorted(empDict['employees'], key=itemgetter('fullAge'), reverse=True)
#print(empDict)

# Writing JSON to a File employess.json
with open('employees.json', 'w') as outfile:
    json.dump(empDict, outfile)
