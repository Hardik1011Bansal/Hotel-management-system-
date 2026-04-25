class customer:
    def __init__(self,name,contact,id):
        self.name=name
        self.contact=contact
        self.id=id
    
    def conversion_to_dict(self):
        return {
            "name":self.name,
            "contact":self.contact,
            "id":self.id
        }
        