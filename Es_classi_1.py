class ContactManager: #Gestisce tutte le operazioni legate ai contatti.
    def __init__(self):
        self.contacts = {}
    
    def create_contact(self,name: str, phone_numbers: list[str]):
        if name in self.contacts:
            raise ValueError("Error! THe contact you are trying to add already exist!")
        else:
            self.contacts[name]=phone_numbers
        return  {name:phone_numbers}

    def add_phone_number(self,contact_name: str, phone_number: str):
        if contact_name not in ContactManager:
            raise ValueError("Errore the contact is not known!")
        
        if phone_number in self.contacts:
            raise ValueError("Error! The contact already exist.")
        
        self.contacts(contact_name).append(phone_number)
        return {contact_name: self.contacts[contact_name]}
    
    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Error! The contact is not known.")
        
        if phone_number not in self.contacts[contact_name]:
            raise ValueError("Error! The phone number is not known.")
        
        self.contact[contact_name].remove[phone_number]

        return {contact_name: self.contacts[contact_name]}
    
    def update_phone_number(self,contact_name: str, old_phone_number: str,new_phone_number: str): #con alt z si può andare a capo senza contare una nuova riga di codice
        if contact_name not in self.contacts:
            raise ValueError("Error! Contact name is not known")
        if old_phone_number not in self.contacts[contact_name]:
            raise ValueError("Error! Old phone number is not known")
        index:int= self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][index] = new_phone_number

        return {contact_name: self.contacts[contact_name]}
    def list_contacts(self): 
        return list(self.contacts.keys())
    
    