from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone 17 Pro Max", "+79999999999")
phone2 = Smartphone("Xiaomi", "Redmi 15", "+79256482415")
phone3 = Smartphone("Samsung", "Galaxy S25", "+79362552525")
phone4 = Smartphone("Huawei", "Pura 80", "+79123123111")
phone5 = Smartphone("Tecno", "SPARK 40 Pro", "+79771817718")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
