from database.models import db, Offer


def check_database(id: int):
    with db:
        offers = Offer.select()
        for offer in offers:
            if offer.offer_id == id:
                return True
        return None


def save_to_db(items: list):
    with db.atomic():
        for item in items:
            Offer.create(
                offer_id=item['id'],
                title=item['title'],
                price=item['price'],
                url=item['url'],
                geo=item['geo'],
                description=item['description'],
                date=item['date']
            )
