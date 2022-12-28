import pytest


class Phonebook:

    def __init__(self):
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def names(self):
        return set(self.numbers.keys())


def test_lookup_by_name():
    phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_phonebook_contains_all_names():
    phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()


def test_missing_name_raises_a_keyerror():
    phonebook = Phonebook()
    phonebook.add("bOB", "1234")
    with pytest.raises(KeyError):
        phonebook.lookup("Missing")
