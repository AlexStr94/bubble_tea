from dataclasses import dataclass
from django.urls import reverse
from bubble_tea import app_views
from bubble_tea.app_views import constants
from bubble_tea.datasource.datasource import DataSource

@dataclass
class CategoryView(app_views.AppView):
    name: str
    image: str
    

main = app_views.ScreenAppView(
    name="index",
    title="Главная",
    start=True,
    elements=[
        app_views.StackAppView(
            axis=constants.Axis.HORIZONTAL,
            alignment=constants.TextAlignment.JUSTIFIED,
            spacing=30,
            elements=[
                app_views.TextAppView(content="Поиск в Симферополе"),
                app_views.ButtonAppView(title="Фильтр", action="open_filters"),
                app_views.ButtonAppView(title="Корзина", action="open_cart"),
            ]
        ),
        app_views.ScrollAppView(
            axis=constants.Axis.HORIZONTAL,
            shows_scroll_indicator=False,
            content=app_views.StackAppView(
                axis=constants.Axis.HORIZONTAL,
                elements=[
                    app_views.ButtonAppView(
                        title="Скидки",
                    ),
                    app_views.ButtonAppView(
                        title="Гараж",
                    ),
                    app_views.ButtonAppView(
                        title="Жилье для поездки",
                    ),
                ]
            )
        ),
        app_views.ScrollAppView(
            axis=constants.Axis.HORIZONTAL,
            shows_scroll_indicator=False,
            content=app_views.ListAppView(
                data_source=DataSource(
                    url=reverse('api:category-list'),
                ),
                item=CategoryView(
                    name="{{name}}",
                    image="{{img_prev_url}}", 
                )
            )
        ),
        app_views.ListAppView(
            data_source=DataSource(url=reverse("api:product-list")),
            item=app_views.StackAppView(
                axis="vertical",
                spacing=8,
                elements=[
                    app_views.ImageAppView(source="{images[0]}"),
                    app_views.TextAppView(content="{title}"),
                    app_views.TextAppView(content="{price} ₽"),
                    app_views.TextAppView(content="{city}"),
                ],
            ),
        )
        
    ],
)
