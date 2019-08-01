from random import randint
from django.db import migrations

from word_service.internal import combinations


queries = []
for combination, parts in combinations.items():
    for i, part in enumerate(parts):
        start = randint(-1, 100)
        increment = i + 1
        query = """
            CREATE SEQUENCE {}_{}_seq
                start {}
                increment {};
        """.format(
            combination, part, start, increment
        )
        queries.append(query)


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [migrations.RunSQL(query) for query in queries]
