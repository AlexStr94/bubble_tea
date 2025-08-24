import json
import os
import random
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import Category, Product, ProductImage
from faker import Faker

fake = Faker("ru_RU")
AVITO_CATEGORIES = [
    ("Авто", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_1.png"),
    ("Недвижимость", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_4_v2.png"),
    ("Работа", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_110_new_2.png"),
    ("Одежда, обувь, аксессуары", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_27.png"),
    ("Хобби и отдых", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_7.png"),
    ("Животные", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_35.png"),
    ("Готовый бизнес и оборудование", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_8_v2.png"),
    ("Услуги", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_114.png"),
    ("Электроника", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_6.png"),
    (
        "Для дома и дачи",
        "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_2_with_wood_desktop.png",
    ),
    ("Запчасти", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_10.png"),
    ("Товары для детей", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_30.png"),
    ("Жильё для путешествия", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_337_travel.png"),
    ("Красота и здоровье", "https://www.avito.st/s/avito/components/visual_rubricator/156x90/cat_88.png"),
]


class Command(BaseCommand):
    help = "Load fake data"

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()
        User.objects.all().delete()

        # Пользователи
        for _ in range(5):
            User.objects.create_user(username=fake.user_name(), email=fake.email(), password="password123")
        self.stdout.write(self.style.SUCCESS("Users created"))

        # Категории
        categories = []
        for name, img in AVITO_CATEGORIES:
            categories.append(Category.objects.create(name=name, img_prev_url=img))
        self.stdout.write(self.style.SUCCESS("Categories created"))

        # Продукты
        users = list(User.objects.all())
        json_path = os.path.join(settings.BASE_DIR, "avito/management/commands/avito_ads.json")

        if not os.path.exists(json_path):
            self.stdout.write(self.style.ERROR(f"Файл {json_path} не найден"))
            return

        with open(json_path, "r", encoding="utf-8") as f:
            ads = json.load(f)
        created_count = 0
        for ad in ads:
            product = Product.objects.create(
                title=ad["title"],
                description=fake.text(),
                price=ad["price"],
                owner=random.choice(users),
                category=random.choice(categories),
                city=ad["location"],
            )

            if ad["image_url"]:
                ProductImage.objects.create(
                    product=product,
                    image_url=ad["image_url"],
                    is_main=True,
                )

            created_count += 1

        self.stdout.write(self.style.SUCCESS(f"Успешно создано {created_count} объявлений"))
