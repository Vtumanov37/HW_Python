from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Apple", "Iphone 18", "+78945612300")
phone2 = Smartphone("Samsung", "Galaxy 91+", "+79632587410")
phone3 = Smartphone("Xiaomi", "14GT Pro", "+74123658901")
phone4 = Smartphone("Nokia", "Connecting people", "+78521463900")
phone5 = Smartphone("Motorolla", "Раскладуха", "+79998541230")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.phone_number}")
    