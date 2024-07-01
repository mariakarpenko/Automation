from address import Address
from mailing import Mailing

address_1 = Address("888888", "Moscow", "Tverskaya", "7", "77")
address_2 = Address("999999", "London", "Baker", "221B", "1")

mailing_1 = Mailing(address_2, address_1, 5000, "564BC78")

print(f"Отправление {mailing_1.track} "
      f"из {mailing_1.from_address.postcode}, {mailing_1.from_address.city}, {mailing_1.from_address.street}, {mailing_1.from_address.building} - {mailing_1.from_address.apartment}" 
      f" в {mailing_1.to_address.postcode}, {mailing_1.to_address.city}, {mailing_1.to_address.street}, {mailing_1.to_address.building} - {mailing_1.to_address.apartment}. "
      f"Стоимость: {mailing_1.cost} рублей.")