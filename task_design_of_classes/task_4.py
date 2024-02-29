# Классы Domain и DomainException
# 574
# Реализуйте класс исключений DomainException. Также реализуйте класс Domain для работы с доменами. Класс Domain должен поддерживать три способа создания своего экземпляра: напрямую через вызов класса, а также с помощью двух методов класса from_url() и from_email():
# domain1 = Domain('pygen.ru')                       # непосредственно на основе домена
# domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
# domain3 = Domain.from_email('support@pygen.ru')    # на основе адреса электронной почты
# При попытке создания экземпляра класса Domain на основе некорректных домена, url-адреса или адреса электронной почты должно быть возбуждено исключение DomainException с текстом:
# Недопустимый домен, url или email
# В качестве неформального строкового представления экземпляр класса Domain должен иметь собственный домен:
# print(str(domain1))                                # pygen.ru
# print(str(domain2))                                # pygen.ru
# print(str(domain3))                                # pygen.ru
# Примечание 1. Будем считать домен корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует точка, а затем снова одна или более латинских букв.
# Примечание 2. Будем считать url-адрес корректным, если он представляет собой строку http:// или https://, за которой следует корректный домен.
# Примечание 3. Будем считать адрес электронной почты корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует собачка (@), а затем корректный домен.
# ---------------------------------------------------------------

import re


class DomainException(Exception):
    pass


class Domain:
    """
    класс Domain для работы с доменами. Класс Domain должен поддерживать три способа создания своего экземпляра: напрямую через вызов класса, а также с помощью двух методов класса from_url() и from_email()
    """
    __CORRECT_DOMAIN = r'[A-Za-z]+[.][A-Za-z]+'

    def __init__(self, string_whis_domain: str) -> None:
        regex = rf'[A-Za-z]*({__class__.__CORRECT_DOMAIN})'   # шаблон домена
        self.domain = __class__.is_valid_domain(string_whis_domain, regex)

    def __str__(self): return str(self.domain)

    @classmethod
    def from_url(cls, string_whis_domain: str):
        regex = fr'https?://({cls.__CORRECT_DOMAIN})'   # шаблон url-адреса
        name_domen = cls.is_valid_domain(string_whis_domain, regex)
        return cls(name_domen)

    @classmethod
    def from_email(cls, string_whis_domain: str):
        regex = fr'[A-Za-z]+\@({cls.__CORRECT_DOMAIN})'   # шаблон email
        name_domen = cls.is_valid_domain(string_whis_domain, regex)
        return cls(name_domen)

    @staticmethod
    def is_valid_domain(string_whis_domain: str, regex: str):
        """проверка на корректность имён"""

        # проверяем вся ли строка соответствует переданному шаблону
        valid_match = re.fullmatch(regex, string_whis_domain)
        # ищем вхождение домена
        search_match = re.search(
            rf'({__class__.__CORRECT_DOMAIN})', string_whis_domain)

        if valid_match and search_match:
            value = str(search_match.group(1))
            return value
        raise DomainException('Недопустимый домен, url или email')


# -----тесты 1-----------
# непосредственно на основе домена
domain1 = Domain('pygen.ru')
domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
# на основе адреса электронной почты
domain3 = Domain.from_email('support@pygen.ru')

print(type(domain1))
print(type(domain2))
print(type(domain3))
# ------2----------------
domains = ['ip.ru', 'ao.org', 'npo.com', 'npo.com', 'zao.org', 'sibtred.info', 'ao.biz', 'npo.net', 'npo.net',
           'oao.net', 'zao.com', 'pahomov.org', 'bikova.ru', 'ooo.ru', 'transol.net', 'zao.com', 'rao.info', 'ooo.org',
           'krjukov.com', 'nikonova.com']

for d in domains:
    domain = Domain(d)
    print(domain)
# ------3----------
try:
    domain1 = Domain('12fergen..org')
except DomainException as e:
    print(e)


try:
    domain1 = Domain('https://dsrengen.ru///')
except DomainException as e:
    print(e)


try:
    domain1 = Domain('1support@rengegen.ru')
except DomainException as e:
    print(e)
