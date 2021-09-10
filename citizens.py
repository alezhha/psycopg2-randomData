import psycopg2
import random as rd
import datas

connection = psycopg2.connect(
    database = 'citizens', 
    user = 'postgres', 
    password = 'zxcv1234', 
    port = '5432', 
    host = 'localhost')

cursor = connection.cursor()

passwords = []
emails = []
phone_numbers = []
adresses = []
followers = tuple(rd.randint(0, 10000000) for i in range(5000))

for name in datas.logins:
    email = name + datas.domains[rd.randint(0, len(datas.domains)-1)]
    emails.append(email.lower())
# print(emails)

for i in range(5000):
    pswrd = ''
    for p in range(rd.randint(8, 15)):
        pswrd += datas.pswd_symbols[rd.randint(0, len(datas.pswd_symbols)-1)]
    passwords.append(pswrd)
# print(passwords)

for num in range(5000):
    number = '+996' + str(datas.code[rd.randint(0, len(datas.code)-1)] + str(rd.randint(111111, 999999)))
    phone_numbers.append(number)
# print(phone_numbers)

for add in range(5000):
    adress = datas.streets[rd.randint(0, len(datas.streets)-1)] + ' st. ' + str(rd.randint(0, 999))
    adresses.append(adress)
# print(adresses)



query = f'''INSERT INTO users (login, password, email, phone_number, country, address, profession, followers) VALUES '''

for _ in range(10000):
    query += f'''(
        '{datas.logins[rd.randint(0, len(datas.logins)-1)]}',
        '{passwords[rd.randint(0, len(passwords)-1)]}',
        '{emails[rd.randint(0, len(emails)-1)]}',
        '{phone_numbers[rd.randint(0, len(phone_numbers)-1)]}',
        '{datas.countries[rd.randint(0, len(datas.countries)-1)]}',
        '{adresses[rd.randint(0, len(adresses)-1)]}',
        '{datas.professions[rd.randint(0, len(datas.professions)-1)]}',
        {followers[rd.randint(0, len(followers)-1)]}
        ),'''

sql_query = query[:-1] + ';'

cursor.execute(sql_query)
connection.commit()

cursor.close()
connection.close()