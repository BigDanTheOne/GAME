import random

trains = []
cities = ['Alexandria', 'Aurora', 'Austin', 'Boston', 'Chandler', 'Charlotte', 'Dallas', 'Dayton', 'Elizabeth',
          'Eugene', 'Gilbert', 'Houston', 'Jackson', 'Rancho Cucamonga', 'Oceansid_ve', 'Santa Rosa', 'Lancaster',
          'Sunnyvale', 'Savannah', 'Pasadena']
marshruts_number = 10
id_v = 0
id_s = 0
vagons = []
marshruts = []
marshruts1 = []
for i in range(marshruts_number):
    l = random.randint(3, 6)
    a = []
    while len(a) < l:
        x = random.randint(0, len(cities) - 1)
        v = cities[x]
        if not (v in a):
            a.append([v, x])
    marshruts.append(a)

with open('a.txt', 'w') as x:
    x.write("insert into train values")
    for i in range(0, 100):
        trains.append([i, 7, random.choice(range(1, marshruts_number))])
        x.write('({}, {}, {}),'.format(trains[i][0], trains[i][1], trains[i][2]))
        x.write('\n')
    trains.append([100, 7, random.choice(range(marshruts_number))])
    x.write('({}, {}, {});'.format(trains[100][0], trains[100][1], trains[100][2]))
    x.write('\n')

    x.write('insert into vagon values ')
    for train in trains:
        w = random.choice(range(2, 7))
        x.write('({}, {}, 0, {}, 1),'.format(id_v, """'head'""", train[0]))
        id_v += 1
        x.write('\n')
        x.write('({}, {}, 0, {}, {}), '.format(id_v, """'rest'""", train[0], w))
        x.write('\n')
        id_v += 1
        for i in range(2, 7):
            if i == w:
                continue
            vagons.append([id_v])
            x.write('({}, {}, 8, {}, {}),'.format(id_v, """'pass'""", train[0], i))
            x.write('\n')
            id_v += 1

    x.write('insert into seat_in_vagon values ')
    for vagon in vagons:
        for i in range(1, 9):
            z = True
            if random.randint(1, 10) > 3:
                z = False
            x.write(str('({}, {}, {}, {}),' + " \n").format(vagon[0], random.randint(2000, 3000), i, z))

    x.write('insert into station values' + '\n')
    for city in cities:
        x.write(str('({}, {}),' + '\n').format("""'{}'""".format(city), id_s))
        id_s += 1

    x.write('insert into marshrut values' + '\n')
    for train in trains:
        x.write(str("({}, {}, {}, {})," + '\n').format(train[2], train[0], len(marshruts[train[2]]),
                                                       random.choice([True, False])))

    x.write('insert into stop values' + '\n')
    for train in trains:
        day1 = random.randint(10, 15)
        h1 = random.randint(10, 23)
        m1 = random.randint(10, 59)
        for st, num in marshruts[train[2]]:
            day2 = random.randint(day1 + 1, day1 + 2)
            h2 = random.randint(10, 23)
            m2 = random.randint(10, 59)
            x.write(str(
                '''({}, {} ,'2019-01-{} '''.format(train[2], train[0], day1) + '''{}:{}', '2019-01-{} {}:{}', {}),'''.format(h1, m1,
                                                                                  day2, h2, m2, num)) + '\n')
            day1 = day2
            h1 = h2
            m1 = m2
