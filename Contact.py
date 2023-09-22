
class Contact:
    """ Class to explore some on dunder / magic methods in python !!"""

    def __init__(self,first_name,last_name,phone=None,email=None,
                 display_mode="masked"):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode
    def __eq__(self,other_self):
        """ If phone no or email is equal then both are same instance
        if different but first name and last name is same then also 
        same instance"""
        if self.phone == other_self.phone or self.email == other_self.email:
            return True
        elif self.first_name == other_self.first_name and self.last_name == other_self.last_name:
            return True
        return False 
    
    def __repr__(self):
        if self.display_mode == "masked":
            return f"Contact({self.first_name[0:2]+'*'*4},{self.last_name+'*'*4})"
        else:
            return f"Contact({self.first_name},{self.last_name},{self.phone},{self.email})"
        
    def __str__(self):
        return f"{self.last_name[0:1]+ self.first_name[0:1]}"
    
    def __format__(self,format_spec):
        if format_spec == 'masked':
            return f"Contact({self.first_name},{self.last_name})"
        elif format_spec=='unmasked':
            return f"Contact({self.first_name},{self.last_name},{self.phone},{self.email})"
        
if __name__=='__main__':
    aditya1 = Contact('Aditya','Kumar')
    aditya2 = Contact('Aditya','Kumar','12345678')
    aditya3 = Contact('Aditya','Kumar','12345678','hey@aditya.co.in')
    aditya4 = Contact('Aditya','Kumar','12345678','hey@aditya.co.in',display_mode='masked')
    print(aditya1==aditya2)
    print(aditya3==aditya4)
    print(repr(aditya1),repr(aditya4))
    print(str(aditya3),str(aditya4))
    print(aditya3.__format__("masked"))
    print(aditya1.__format__("unmasked"))
