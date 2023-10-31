per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму денег, которую планируете внести под проценты: '))
deposit = [money / 100 * per_cent.get('ТКБ'), money / 100 * per_cent.get('СКБ'), money / 100 * per_cent.get('ВТБ'), money / 100 * per_cent.get('СБЕР')]
print(deposit)
print('Максимальная сумма, которую вы можете заработать - ', max(deposit))