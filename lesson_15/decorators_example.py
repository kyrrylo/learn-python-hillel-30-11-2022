import os
from animals import Cow


def my_decorator(func):
    return func


@my_decorator
def my_function():
    pass


class CsvFileProcessor:
    FOLDER_IN = 'csv_files'

    def __init__(self, csv_headers: list):
        self.headers = csv_headers

    # декоратор используемый для обозначения методов, которые не нуждаются в контексте объекта класса
    @staticmethod
    def peek_headers(filename: str):
        with open(os.path.join(CsvFileProcessor.FOLDER_IN, filename), newline='') as csv_file:
            pass
            headers = ['header1', 'header2']
            return headers

    @classmethod
    def cls_peek_headers(cls, filename: str):
        with open(os.path.join(cls.FOLDER_IN, filename), newline='') as csv_file:
            pass
            headers = ['header1', 'header2']
            return headers

    # декоратор который принимает имя класса и обладает неким его контекстом (но не объекта!)
    # чаще всего используется при предобработке входных параметров для создания объекта класса
    # создаём объект класса передав туда headers, а в этом методе - добываем headers по наводке на filename
    @classmethod
    def create_processor_from_filename(cls, filename: str):
        print(cls == CsvFileProcessor, type(cls), type(CsvFileProcessor))
        header = cls.peek_headers(filename)
        # return CsvFileProcessor(header)
        return cls(header)

    @staticmethod
    def potential_static_method():
        print(5 + 5)


if __name__ == '__main__':
    print(CsvFileProcessor.FOLDER_IN)
    headers = CsvFileProcessor.peek_headers('csv_file.csv')
    print(headers)
    CsvFileProcessor.potential_static_method()

    cfp = CsvFileProcessor(headers)
    print(cfp.FOLDER_IN)
    cfp.potential_static_method()
    print(cfp.peek_headers('csv_file.csv'))

    cfp2 = CsvFileProcessor.create_processor_from_filename('csv_file.csv')
    print(cfp2)
    print(cfp2.FOLDER_IN)
    cfp2.potential_static_method()
    print(cfp2.peek_headers('csv_file.csv'))
