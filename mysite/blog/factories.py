import factory
from faker import Factory as FakerFactory
from django.contrib.auth.models import User
from django.utils.timezone import now
from blog.models import Post

faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User  # Define que esta fábrica está relacionada ao modelo User

    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda x: faker.name())

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post  # Define que esta fábrica está relacionada ao modelo Post

    title = factory.LazyAttribute(lambda x: faker.sentence())  
    created_on = factory.LazyAttribute(lambda x: now())  
    status = 0  # Se 0 significa "draft", altere conforme necessário
    author = factory.SubFactory(UserFactory)  # Adicionando um autor válido

