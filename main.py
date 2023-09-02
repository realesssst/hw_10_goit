class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)
        self.phones = []

    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        self.phones.append(phone)

    def remove_phone(self, phone_value):
        for phone in self.phones:
            if phone.value == phone_value:
                self.phones.remove(phone)
                return True
        return False

    def edit_phone(self, old_phone_value, new_phone_value):
        for phone in self.phones:
            if phone.value == old_phone_value:
                phone.value = new_phone_value
                return True
        return False


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_records(self, search_str):
        results = []
        for name, record in self.data.items():
            if search_str in name:
                results.append(record)
            for phone in record.phones:
                if search_str in phone.value:
                    results.append(record)
        return results


if __name__ == "__main__":
    address_book = AddressBook()

    while True:
        print("Available commands:")
        print("1. Add contact (format: 'add name phone')")
        print("2. Find contact (format: 'find search_string')")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            input_str = input("Enter name and phone: ")
            name, phone = input_str.split()
            if name in address_book.data:
                address_book.data[name].add_phone(phone)
            else:
                record = Record(name)
                record.add_phone(phone)
                address_book.add_record(record)
        elif choice == "2":
            search_str = input("Enter search string: ")
            found_records = address_book.find_records(search_str)
            if found_records:
                print("Found records:")
                for record in found_records:
                    print(f"Name: {record.name}, Phones: {', '.join(record.phones)}")
            else:
                print("No matching records found.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')