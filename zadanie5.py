# Задание 5
# Используйте набор данных под кодовым названием - user_data.
# Создайте класс который будет принимать эти данные как аргумент.
# 1.Создайте метод genders() который вернёт всё разнообразие полов в типе данных Tuple.
# Example: ("Male", "Female",...)
# 2. Создайте метод get_domain() который возвращает Tuple ДОМЕННЫХ имён электронной почты ВСЕХ пользователей.
# Что такое доменное имя:
# python.itc@gmail.com
# 1. ИМЯ ПОЧТЫ - python.itc
# 2. РАЗДЕЛИТЕЛЬНЫЙ СИМВОЛ - @
# 3. ДОМЕННОЕ ИМЯ - gmail.com

user_data = [{
  "id": 1,
  "first_name": "Humphrey",
  "last_name": "Wilcox",
  "email": "hwilcox0@odnoklassniki.ru",
  "gender": "Male",
  "ip_address": "80.232.175.95"
}, {
  "id": 2,
  "first_name": "Erhard",
  "last_name": "Byart",
  "email": "ebyart1@addthis.com",
  "gender": "Male",
  "ip_address": "125.7.237.155"
}, {
  "id": 3,
  "first_name": "Brok",
  "last_name": "Leiden",
  "email": "bleiden2@usnews.com",
  "gender": "Male",
  "ip_address": "108.201.248.102"
}, {
  "id": 4,
  "first_name": "Gradeigh",
  "last_name": "Spreckley",
  "email": "gspreckley3@marriott.com",
  "gender": "Male",
  "ip_address": "90.169.195.245"
}, {
  "id": 5,
  "first_name": "Trueman",
  "last_name": "McArd",
  "email": "tmcard4@cargocollective.com",
  "gender": "Male",
  "ip_address": "249.26.239.198"
}, {
  "id": 6,
  "first_name": "Giacobo",
  "last_name": "Rishworth",
  "email": "grishworth5@merriam-webster.com",
  "gender": "Male",
  "ip_address": "156.104.68.219"
}, {
  "id": 7,
  "first_name": "Marcia",
  "last_name": "Burney",
  "email": "mburney6@gmpg.org",
  "gender": "Female",
  "ip_address": "52.104.185.232"
}, {
  "id": 8,
  "first_name": "Court",
  "last_name": "Haysar",
  "email": "chaysar7@eepurl.com",
  "gender": "Hidden",
  "ip_address": "60.138.180.175"
}, {
  "id": 9,
  "first_name": "Penn",
  "last_name": "Slatten",
  "email": "pslatten8@narod.ru",
  "gender": "Male",
  "ip_address": "216.91.212.228"
}, {
  "id": 10,
  "first_name": "Rayna",
  "last_name": "Jacobsson",
  "email": "rjacobsson9@4shared.com",
  "gender": "Female",
  "ip_address": "158.81.126.17"
}, {
  "id": 11,
  "first_name": "Elissa",
  "last_name": "Milch",
  "email": "emilcha@ucoz.ru",
  "gender": "Female",
  "ip_address": "160.46.17.104"
}, {
  "id": 12,
  "first_name": "Cissiee",
  "last_name": "Dever",
  "email": "cdeverb@dailymail.co.uk",
  "gender": "Hidden",
  "ip_address": "198.12.171.92"
}, {
  "id": 13,
  "first_name": "Lorie",
  "last_name": "Cavozzi",
  "email": "lcavozzic@apache.org",
  "gender": "Female",
  "ip_address": "252.228.114.151"
}, {
  "id": 14,
  "first_name": "Shelton",
  "last_name": "Pipe",
  "email": "spiped@opera.com",
  "gender": "Male",
  "ip_address": "217.193.203.141"
}, {
  "id": 15,
  "first_name": "Cordell",
  "last_name": "Hrinchenko",
  "email": "chrinchenkoe@ovh.net",
  "gender": "Transgender",
  "ip_address": "147.76.167.191"
}, {
  "id": 16,
  "first_name": "Dyanna",
  "last_name": "Sizzey",
  "email": "dsizzeyf@xing.com",
  "gender": "Female",
  "ip_address": "8.177.20.12"
}, {
  "id": 17,
  "first_name": "Felice",
  "last_name": "Floyed",
  "email": "ffloyedg@instagram.com",
  "gender": "Male",
  "ip_address": "4.150.254.58"
}, {
  "id": 18,
  "first_name": "Arel",
  "last_name": "Donoher",
  "email": "adonoherh@youtu.be",
  "gender": "Male",
  "ip_address": "186.214.243.230"
}, {
  "id": 19,
  "first_name": "Kristoffer",
  "last_name": "Carvill",
  "email": "kcarvilli@xinhuanet.com",
  "gender": "Male",
  "ip_address": "58.204.72.103"
}, {
  "id": 20,
  "first_name": "Norbie",
  "last_name": "Oleksinski",
  "email": "noleksinskij@free.fr",
  "gender": "Male",
  "ip_address": "242.192.49.216"
}]

class User_Data():
    def __init__(self, id, first_name, last_name, email, gender, ip_address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.ip_address = ip_address
    

    def genders(self):
        print(tuple(self.gender))

    def get_domain(self):
        f = []
        for a in self.email:
            index = a.find('@')     
            f.append(a[(index + 1)::])
        print(tuple(f))
        


id = []
first_name= []
last_name = []
email = []
gender = []
ip_address = []

for i in user_data:
    id.append(i["id"])
    first_name.append(i["first_name"])
    last_name.append(i["last_name"])
    email.append(i["email"])
    gender.append(i["gender"])
    ip_address.append((i["ip_address"]))


a = User_Data(id, first_name, last_name, email, gender, ip_address)    
a.genders()
a.get_domain()
