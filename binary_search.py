from random import randint
from time import time

TIME = time()

vs_mode_enabled = False

options = {
    'from': 1,
    'to': 1024*1024*1024*1024
}

# массив для поиска
search_array = range(options['from'], options['to'] + 1)

# искомое число
search_element = randint(options['from'], options['to'])


class BinarySearch:

    HOPS = 0
    TIME = 0.

    @staticmethod
    def search(search_array, search_element):
        BinarySearch.HOPS = 0
        BinarySearch.TIME = time()

        low = 0
        high = len(search_array) - 1

        while low <= high:
            BinarySearch.HOPS += 1
            mid = (low + high) // 2

            if search_array[mid] == search_element:
                BinarySearch.TIME = time() - BinarySearch.TIME
                return mid
            elif search_array[mid] > search_element:
                high = mid - 1
            elif search_array[mid] < search_element:
                low = mid + 1


class SimpleSearch:

    HOPS = 0
    TIME = 0

    @staticmethod
    def search(search_array, search_element):
        SimpleSearch.TIME = time()
        for i in search_array:
            SimpleSearch.HOPS += 1
            if search_array[i - 1] == search_element:
                SimpleSearch.TIME = time() - SimpleSearch.TIME
                return i - 1

print("Размер массива для поиска: %d" % len(search_array))
print("Искомое число: %d" % search_element)

print()

binary_text = "BinarySearch:"
print(binary_text)
print("="*len(binary_text))
print("Номер элемента в массиве: %d" % BinarySearch.search(search_array, search_element))
print("Количество попыток: %d" % BinarySearch.HOPS)
print("Время работы алгоритма %.5f" % BinarySearch.TIME)

if vs_mode_enabled:
    print()

    simple_text = "SimpleSearch:"
    print(simple_text)
    print("="*len(simple_text))
    print("Номер элемента в массиве: %d" % SimpleSearch.search(search_array, search_element))
    print("Количество попыток: %d" % SimpleSearch.HOPS)
    print("Время работы алгоритма %.5f" % SimpleSearch.TIME)

    print()

    vs = "SimpleSearch/BinarySearch:"
    print(vs)
    print("="*len(vs))
    print("%.5f/%.5f = %.2f" % (BinarySearch.TIME, SimpleSearch.TIME, SimpleSearch.TIME / BinarySearch.TIME))

print()
print("Время работы программы: %.5f" % (time() - TIME))