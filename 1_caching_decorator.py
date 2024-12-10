def caching_decorator(max_cache_size=128):
    cache = {}

    def decorator(func):
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            # Проверка на хранение кэша заданной функции и аргументов
            if func_name in cache:
                if args in cache[func_name]:
                    print(f'Получение значения из кэша: {cache[func_name][args]}')
                    return cache[func_name][args]

                func_result = func(*args, **kwargs)

                # Удаление самого старого элемента в кэше, при отсутствии места для хранения
                if len(cache[func_name]) >= max_cache_size:
                    print(f'Удаление самого старого элемента: {next(iter(cache[func_name]))}')
                    cache[func_name].pop(next(iter(cache[func_name])))

                cache[func_name][args] = func_result
            else:
                func_result = func(*args, **kwargs)
                cache[func_name] = {args: func_result}

            return func_result

        return wrapper

    return decorator


@caching_decorator(2)
def addition(x, y):
    print(f'Выполнение функции addition({x}, {y})')
    return x + y


@caching_decorator(3)
def square(x):
    print(f'Выполнение функции square({x})')
    return x * x


def main():
    print('--------------Тест функции addition()--------------')
    print(f'Результат: {addition(1, 2)}\n')  # Добавление первого результата в кэш
    print(f'Результат: {addition(3, 4)}\n')  # Добавление второго результата в кэш
    print(f'Результат: {addition(1, 2)}\n')  # Значение берётся из кэша
    print(f'Результат: {addition(3, 4)}\n')  # Значение берётся из кэша
    print(f'Результат: {addition(5, 6)}\n')  # Переполнение кэша: удаление старого значения и добавление нового
    print(f'Результат: {addition(1, 2)}\n')  # Переполнение кэша и повторное вычисление самого первого результата

    print('--------------Тест функции square()--------------')
    print(f'Результат: {square(1)}\n')  # Добавление первого результата в кэш
    print(f'Результат: {square(2)}\n')  # Добавление второго результата в кэш
    print(f'Результат: {square(3)}\n')  # Добавление третьего результата в кэш
    print(f'Результат: {square(1)}\n')  # Значение берётся из кэша
    print(f'Результат: {square(4)}\n')  # Переполнение кэша: удаление старого значения и добавление нового
    print(f'Результат: {square(1)}\n')  # Переполнение кэша и повторное вычисление самого первого результата


if __name__ == '__main__':
    main()
