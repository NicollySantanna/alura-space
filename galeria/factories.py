import factory
from django.utils.text import slugify
from faker import Faker
from .models import Fotografia

fake = Faker()


class FotografiaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Fotografia

    nome = factory.LazyAttribute(lambda _: f"{fake.word().capitalize()} {fake.random_element(['Alpha', 'Beta', 'Gamma', 'Nebula', 'Star', 'Cluster'])}")
    legenda = factory.Faker('sentence', nb_words=8)
    descricao = factory.Faker('text', max_nb_chars=300)
    categoria = factory.Faker('random_element', elements=[cat[0] for cat in Fotografia.OPCOES_CATEGORIA])
    foto = factory.LazyAttribute(lambda obj: f"fotos/{slugify(obj.nome)}.jpg")
