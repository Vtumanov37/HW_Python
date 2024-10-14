from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Проспект Мира", "30", "10")
from_address = Address("654321", "Кострома", "Нижний Вал", "11", "5")
mailing = Mailing(to_address, from_address, 1500, "TRACK12345")
print(mailing)
