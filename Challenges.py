from string import ascii_letters
from random import choices, randint, shuffle
from string import ascii_lowercase, ascii_uppercase

# Problem 1: Array Flattener


array = [0, 1, 2, [3, 4], 5, [[6], [7], [[8, 9]], [10]], 11]


class Flattener():
    def __init__(self, *flatten):
        self.__flat = []
        self.flatten(flatten)

    def flatten(self, flatten):
        self.__list = [*flatten]
        for item in self.__list:
            if not isinstance(item, list):
                self.__flat.append(item)
            elif isinstance(item, list):
                self.flatten(item)

    def __str__(self):
        return f"{self.__flat}"


# Problem 2: String Reverser
def string_reverser(string):
    empty = ""
    first = []
    second = []
    for element in enumerate(string):
        first.append(element)
    first.sort(key=lambda item: item[0], reverse=True)
    for obj in first:
        second.append(obj[1])
    for each in second:
        empty += each
    return empty


# Problem 3: Caesar Encryption
def ceasar_encrypt(string):
    indexed_true = {letters: number for number,
                    letters in enumerate(ascii_uppercase, start=1)}
    indexed_false = {number: letters for number,
                     letters in enumerate(ascii_uppercase, start=1)}
    written = string.upper()
    true_value = []
    encrypted = []
    for element in written:
        if element in indexed_true:
            number = indexed_true[element]
            if number == 24:
                number_for_false = 1
            elif number == 25:
                number_for_false = 2
            elif number == 26:
                number_for_false = 3
            else:
                number_for_false = number + 3
            true_value.append(number_for_false)
        else:
            true_value.append(element)
    for item in true_value:
        if item in indexed_false:
            encrypted.append(indexed_false[item])
        else:
            encrypted.append(item)
    final = ""
    for items in encrypted:
        final += items
    return final


# Problem 5: Prime Number Sum
class PrimeMagistrate():
    def __init__(self, integer):
        self.__numbers = []
        self.__checkwith = []
        self.primes = []
        self.__primes_summed = []
        self.get_numbers(integer)

    def get_numbers(self, integer):
        for numbers in range(1, integer + 1):
            self.__numbers.append(numbers)
        self.drag_primes(self.__numbers)

    def drag_primes(self, odds):
        for a in odds:
            for b in range(1, a):
                if b == 1:
                    continue
                if b == a:
                    continue
                elif a % b == 0:
                    self.__checkwith.append(a)
            if a not in self.__checkwith and a != 1:
                self.primes.append(a)
        self.sum_primes(self.primes)

    def sum_primes(self, primes_list):
        total = 0
        for elements in primes_list:
            total += elements
        self.__primes_summed.append(total)

    def __str__(self):
        return f"{self.__primes_summed}"


# Problem 6: Unique Sum
def unique_summer(array):
    uniques = []
    total = 0
    for elements in array:
        if array.count(elements) > 1:
            continue
        else:
            uniques.append(elements)
    for items in uniques:
        total += items
    return total


def min_max_sum(array):
    new = sorted(array)
    min = new[0]
    max = new[-1]
    total = min + max
    return total


class WordAnalyzer():
    def __init__(self, words):
        self.words_list = []
        self.initial_sorter(words)

    def initial_sorter(self, *letters: str):
        letter_list = []
        words_string = ""
        for items in letters:
            letter_list.append(items)
        for elements in letter_list:
            if elements != " ":
                words_string += elements
                self.words_list.append(words_string)
                words_string = ""


class SillyString():
    def __init__(self, string: str):
        self.base = string
        self.__compress_list = []
        self.compressed = string

    @property
    def compressed(self):
        out = ""
        for items in self.__compress_list:
            out += str(items)
        return out

    @compressed.setter
    def compressed(self, string: str):
        count = 1
        iteration = 0
        index = 0
        final = -1
        mass = len(string)
        for element in string:
            iteration += 1
            if iteration == mass:
                break
            if index == 0 and string[index] != string[index + 1]:
                self.__compress_list.append(element)
                self.__compress_list.append(1)
            elif string[index] != string[index + 1] and string[index] != string[index - 1]:
                self.__compress_list.append(element)
                self.__compress_list.append(1)
            if string[index] == string[index + 1]:
                count += 1
            if index != 0 and string[index] == string[index - 1] and string[index] != string[index + 1]:
                self.__compress_list.append(element)
                self.__compress_list.append(count)
                count = 1
            if iteration == mass - 1 and string[final] != string[final - 1]:
                self.__compress_list.append(string[final])
                self.__compress_list.append(1)
            if iteration == mass - 1 and string[final] == string[final - 1]:
                self.__compress_list.append(string[final])
                self.__compress_list.append(count)
            index += 1

    def balance_check(string_one, string_two):
        checklist_alpha = [*string_one]
        checklist_beta = [*string_two]
        auth = []
        for item in checklist_alpha:
            if item not in checklist_beta:
                auth.append(False)
        if len(auth) != 0:
            return False
        else:
            return True


def longest_substring(string):
    chars = [*string]
    idx = 0
    lone = []
    check = []

    while idx != len(chars) - 1:
        if chars[idx] != chars[idx + 1] and chars[idx] != chars[idx - 1]:
            check.append(chars[idx])
            lone.append(len(check))
        if chars[idx] == chars[idx + 1]:
            check.clear()
        if idx == len(chars) - 2:
            if chars[idx + 1] != chars[idx]:
                check.append(chars[idx + 1])

        idx += 1

    print(lone)
    print(check)

    lone.sort(reverse=True)
    return lone[0]


def checker(string: str):
    master_length = len(string)
    list = string
    listed_forward = []
    listed_backward = []
    idx = 0
    teller = []

    for _ in list:
        listed_forward.append(list[idx])
        idx += 1

    idx = -1

    for _ in list:
        listed_backward.append(list[idx])
        idx -= 1
    print(listed_forward)
    print(listed_backward)
    idx = 0

    for _ in range(master_length):
        if listed_forward[idx] == listed_backward[idx]:
            teller.append(1)
        else:
            teller.append(0)
        idx += 1

    total = 1
    for __ in teller:
        total *= __

    if total:
        return True
    else:
        return False


def anagrams(string1: str, string2: str):
    stringed = []
    for items in enumerate(ascii_lowercase, start=1):
        stringed.append(items)
    dic = {key: value for value, key in stringed}

    first = []
    second = []

    product1 = None
    product2 = None

    for _ in string1:
        conv1 = dic[_]
        first.append(conv1)

    for __ in string2:
        conv2 = dic[__]
        second.append(conv2)

    total = 1
    for element in first:
        total *= element
    product1 = total
    total = 1
    for elements in second:
        total *= elements
    product2 = total

    if product1 == product2:
        return True
    else:
        return False


def reverser(string: str):
    idx = -1
    counts = []
    letters = [*ascii_letters]
    chars_forward = []
    chars_backward = []
    non_chars = []
    for item in string:
        idx += 1
        if item in letters:
            chars_forward.append(item)
        else:
            non_chars.append(item)
            counts.append(idx)

    idx = -1

    for _ in chars_forward:
        chars_backward.append(chars_forward[idx])
        idx -= 1

    idx = 0
    non_char_idx = 0

    for _ in chars_backward:
        if idx in counts:
            chars_backward.insert(idx, non_chars[non_char_idx])
            non_char_idx += 1
        idx += 1

    reversed = "".join([letter for letter in chars_backward])
    return reversed
