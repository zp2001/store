class  user:
    __account = None
    __username = None
    __password = None
    __moeny = None
    __address = None
    __registerDate = None
    __bankName = None



    def setAccount(self,account):
        self.__account = account
    def getAccount(self):
        return self.__account

    def setusername(self,username):
        self.__username = username
    def getusername(self):
        return self.__username

    def setpassword(self,password):
        self.__password = password
    def getpassword(self):
        return self.__password

    def setmoeny(self,moeny):
        self.__moeny = moeny
    def getmoeny(self):
        return self.__moeny

    def setaddress(self,address):
        self.__address = address
    def getaddress(self):
        return self.__address

    def setregisterDate(self,registerDate):
        self.__registerDate = registerDate
    def getregisterDate(self):
        return self.__registerDate

    def setbankName(self,bankName):
        self.__bankName = bankName
    def getbankName(self):
        return self.__bankName

class Address:
    __country = None
    __province = None
    __street = None
    __door = None

    def setcountry(self,country):
        self.__country = country
    def getcountry(self):
        return self.__country

    def setprovince(self,province):
        self.__province = province
    def getprovince(self):
        return self.__province

    def setstreet(self,street):
        self.__street = street
    def getstreet(self):
        return self.__street

    def setdoor(self,door):
        self.__door = door
    def getdoor(self):
        return self.__door

class View:
    def printWelcome(self):
        welcome = '''
            ******************************************
            *    欢迎来到中国工商银行账户管理系统      *
            ******************************************
            *   1.开户                                *
            *   2.存款                                *
            *   3.取款                                *
            *   4.转账                                * 
            *   5.查询账户                            *
            *   6.退卡                                *
            ******************************************
        '''
        print(welcome)








