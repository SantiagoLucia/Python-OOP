class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value
        in their name."""
        return [contact for contact in self if name in contact.name]


class Contact:
    all_contacts = ContactList()
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
        
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
        

class Supplier(Contact):
    def order(self, order):
        print(f"""If this where a real system we would send
              '{order} order to '{self.name}'"""
              )
        