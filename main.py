# Домашнее задание по теме "Интроспекция"

# импорт методов и библиотек
from pprint import pprint
import inspect

class InfoClass():
    def __init__(self, atr):
        self.atr = atr
        pass

# объявление функции исследования интроспекции
def introspection_info(obj):
    # объявление словаря результатов
    i_info = {'metods' : [],
           'attributes' : [],
           'module' : []}
    # цикл извлечения методов и аттрибутов исследуемого
    # объекта и добавления этих данных в словарь
    for i in dir(obj):
        if callable(getattr(obj, i)):
            i_info['metods'].append(i)
        else:
            i_info['attributes'].append(i)
    # извлечение информации о иодулях объекта интроспекции
    module = inspect.getmodule(obj)
    if module is None:
        i_info['module'] = __name__
    else:
        i_info['module'] = module.__name__
    # возврат словаря полученных данных
    return i_info

# исследуемый объект
number_info = introspection_info(42)
word_info = introspection_info('humen')
cl_info = InfoClass('x')
class_info = introspection_info(cl_info)
# вывод на консоль результатов
print('-'*10, 'number_info', '-'*10)
pprint(number_info)
print('-'*10, 'word_info', '-'*10)
pprint(word_info)
print('-'*10, 'class', '-'*10)
pprint(class_info)