
def decor_add_input_eror(func):
    """Декоратор для обробки помилок при додаванні нової записи"""
    def inner_func(args, *qwargs):
        try:
            func(args, *qwargs)
        except ValueError:
            return "Невірна команда: введіть Add Name Phone\n"
        return "Contact added.\n"
    return inner_func


@decor_add_input_eror
def add_contact(args, contacts):
    # "add username phone". За цією командою бот зберігає у
    # пам'яті, наприклад у словнику, новий контакт.
    # Користувач вводить ім'я username та номер телефону phone,
    # обов'язково через пробіл.
    name, phone = args
    contacts.append({'name': name, 'phone': phone})


def decor_chg_cont_input_eror(func):
    """Декоратор для обробки помилок при спробі змінити запис"""
    def inner_func(args, *qwargs):
        try:
            name, new_phone = args
            func(args, *qwargs)
        except StopIteration:
            return (f"Запис з іменем {name} не знайдена!\n")
        except TypeError:
            return "Невірна команда: введіть Change Username Phone\n"
        except ValueError:
            return "Невірна команда: введіть Change Username Phone\n"
        return (f"Номер телефону для {name} оновлено на {new_phone}\n")
    return inner_func


@decor_chg_cont_input_eror
def change_contact(args, contacts):
    # "change username phone". За цією командою бот зберігає
    # в пам'яті новий номер телефону phone для контакту
    # username, що вже існує в записнику.
    name, new_phone = args
    next(filter(lambda c: c["name"] == name, contacts)).update(
        {"phone": new_phone})


def decor_get_name_input_eror(func):
    """Декоратор для обробки помилок пошуку контакту"""
    def inner_func(args, *qwargs):
        try:
            name, = args
            result = func(args, *qwargs)
        except StopIteration:
            return (f"Запис з іменем {name} не знайдена!\n")
        except TypeError:
            return "Невірна команда: введіть Phone username\n"
        except ValueError:
            return "Невірна команда: введіть Phone username\n"
        return result
    return inner_func


@decor_get_name_input_eror
def get_name_byphone(args, contacts):
    # "phone username" За цією командою бот виводить у консоль
    # номер телефону для зазначеного контакту username.
    name, = args
    return f"Номер телефона для {name}: {next(filter(lambda c: c["name"] == name, contacts))["phone"]}\n"


def get_all(contacts):
    # "all". За цією командою бот виводить всі збереженні контакти з
    # номерами телефонів у консоль.
    if not contacts:
        return f"Нема жодного користувача\n"
    result = ''
    for contact in contacts:
        result = result + \
            (f"Їм'я: {contact["name"]}, телефон: {contact["phone"]}\n")
    return result
