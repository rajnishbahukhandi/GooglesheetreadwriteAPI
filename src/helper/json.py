from faker import Faker

fake = Faker()


def payloadTestdata_faker_put():
    payload = {
        "formTitle": fake.text(40),
        "formDate": str(fake.date_between(start_date='today', end_date='+30d'))
    }
    return payload
