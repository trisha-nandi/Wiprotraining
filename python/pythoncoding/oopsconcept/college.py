from zipfile import compressor_names


class college:
    def __init__(self,ccode,cname,ccity):
        self.collcode=ccode
        self.collname=cname
        self.collcity=ccity

    def welcome_messege(self):
        print('hello there')

    def display_college_details(self):
        print(f'college code: {self.collcode} \n college name: {self.collname} \n city: {self.collcity}'