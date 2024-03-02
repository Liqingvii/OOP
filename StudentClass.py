class StudentClass:

    def __init__(self, S, N, D, C):
        self.__StudentID = S
        self.__Name = N
        self.__DOB = D
        self.__classification = C

    def get_showage(self):
        import datetime
        current_time = datetime.datetime.now()
        Current_year = int(str(current_time).split('-')[0])
        Dob_year = self.__DOB
        print(Current_year - Dob_year)
    
    def get_register(self):
        if self.__classification == 'Sr':
            print(f"The register time is 4/1 to 4/3")
        if self.__classification == 'Jr':
            print(f"The register time is 4/4 to 4/6")
        if self.__classification == 'S':
            print(f"The register time is 4/7 to 4/9")
        if self.__classification == 'F':
            print(f"The register time is 4/10 to 4/12")

    def get_returnage(self):
        import datetime
        current_time = datetime.datetime.now()
        Current_year = int(str(current_time).split('-')[0])
        Dob_year = self.__DOB
        return Current_year - Dob_year
    
    def get_register2(self):
        if self.__classification == 'Sr':
            return "The register time is 4/1 to 4/3"
        if self.__classification == 'Jr':
            return "The register time is 4/4 to 4/6"
        if self.__classification == 'S':
            return "The register time is 4/7 to 4/9"
        if self.__classification == 'F':
            return "The register time is 4/10 to 4/12"
        
