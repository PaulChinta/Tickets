class User:
    def __init__(self,p_num,first_name,last_name,gender,dob,email_id):
        self.p_num=p_num
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.dob=dob
        self.email_id=email_id
    def print_data(self):
        print(self.p_num,self.first_name,self.last_name,self.gender,self.dob,self.email_id)

class Flight:
    def __init__(self,f_no,origin,destination,number_seats):
        pass