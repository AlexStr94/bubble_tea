from typing import TYPE_CHECKING

from django.http import JsonResponse
from django.views import View

from .app_views import ScreenAppView

if TYPE_CHECKING:
    from django.http import HttpRequest


class ScreenListView(View):
    """Возвращает список всех экранов приложения."""

    def get(self, request: "HttpRequest") -> JsonResponse:
        screens = ScreenAppView.get_screens()
        start_screen: ScreenAppView | None = next(filter(lambda x: x.start, screens), None)
        data = {
            "start": start_screen.name if start_screen else None,
            "screens": [screen.name for screen in screens],
        }

        return JsonResponse({"screens": data})


class ScreenView(View):
    """Возвращает информацию об экране приложения."""

    def get(self, request: "HttpRequest", name: str) -> JsonResponse:
        screens = ScreenAppView.get_screens()
        screen: ScreenAppView | None = next(filter(lambda x: x.name == name, screens), None)
        if not screen:
            raise Exception

        return JsonResponse(data=screen.to_dict(), json_dumps_params={"ensure_ascii": False})
