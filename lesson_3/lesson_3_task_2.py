from smartphone import Smartphone

phone_1 = Smartphone("Apple", "IPhone 6", "+79898787654")
phone_2 = Smartphone("Xiaomi", "Redmi Note 13 Pro", "+76543210987")
phone_3 = Smartphone("Samsung", " Samsung Galaxy A55", "+71234567890")
phone_4 = Smartphone("Apple", "IPhone 14 Pro", "+79895436782")
phone_5 = Smartphone("Huawei", "Huawei Pura 70", "+74527845678")

catalog = [phone_1, phone_2, phone_3, phone_4, phone_5]

for item in catalog:
    print(item)