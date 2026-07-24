from dataclasses import dataclass

@dataclass(frozen=True)
class Urls:
    QA_DESK: str = "https://qa-desk.education-services.ru/"

name_of_book = "Великий Гэтсби"
description_of_book = "«Великий Гэтсби» — это история о загадочном миллионере Джее Гэтсби, который закатывает роскошные вечеринки ради одной цели: вернуть свою прошлую любовь, Дэйзи Бьюкенен. Роман показывает крах иллюзий и американской мечты в циничном мире богачей 1920-х годов."
price_of_book = 500