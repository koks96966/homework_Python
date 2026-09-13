from address import Address
from mailing import Mailing


def format_address(addr):
    return f"{addr.index}, {addr.city}, {addr.street}, {addr.house} - {addr.apartment}"


from_address = Address("450123", "Тамбов", "ул. Красная", "6", "кв. 3")
to_address = Address("789211", "Саранск", "ул. Советская", "22", "кв. 11")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    track="45005145009749",
    cost=463
)

print(
    f"Отправление {mailing.track} из {format_address(mailing.from_address)} "
    f"в {format_address(mailing.to_address)}. Стоимость {mailing.cost} рублей."
)
