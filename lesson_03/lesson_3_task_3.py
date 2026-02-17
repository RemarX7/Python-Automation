from address import Address
from mailing import Mailing

to_address = Address('522000', 'Rostov-on-Don', 'Pushkina', 11, 209)
from_address = Address('500100', 'Rostov-on-Don', 'Lermontova', 14, 1)
mailing = Mailing(to_address, from_address, 14999, '0123456789B')

print(
    f'Отправление {mailing.track} из {from_address.index}, '
    f'{from_address.city}, {from_address.street}, {from_address.house}'
    f' - {from_address.apartment} в {to_address.index}, {to_address.city}'
    f', {to_address.street}, {to_address.house} -'
    f'{to_address.apartment}. Стоимость {mailing.cost} рублей.'
)
