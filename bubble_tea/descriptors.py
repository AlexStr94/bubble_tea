class ClassOnlyMethod:
    """Дескриптор, разрешающий вызов метода только из класса."""

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is not None:
            raise AttributeError("Доступ к методу только через класс")
        return self.func.__get__(owner, owner)
