import requests, re
import argparse, os

class proxy_scrape():

    def __init__(self):
        self.reset =   '\033[0m'
        self.parser = argparse.ArgumentParser(description= f"Proxy Scraper [{self.rgb(0, 255, 255)}¥Shinx.ssh{self.reset}]")
        self.parser.add_argument('-t', help= f'type of Proxy [{self.rgb(0, 255, 255)}HTTP/HTTPS/SOCKS4/SOCKS5/ALL{self.reset}]')
        self.parser.add_argument('-o', help= f'Path File Output')
        self.args = self.parser.parse_args()
        self.type = self.args.t
        self.output = self.args.o
        self.proxy_list = [
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/blob/master/socks4.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
            "https://www.proxy-list.download/api/v1/get?type=socks4",
            "https://proxy-spider.com/api/proxies.example.txt",
            "https://multiproxy.org/txt_all/proxy.txt",
            "http://rootjazz.com/proxies/proxies.txt",
            "http://ab57.ru/downloads/proxyold.txt"
            ]

        self.found = []
        self.n = 0

    def rgb(self, r: int, g: int, b: int):
        return f'\033[38;2;{str(r)};{str(g)};{str(b)}m'
    
    def fade(self, text: str):
        return ''.join(f'{self.rgb(0, 150 + 4 * i, 255)}{char}' for i, char in enumerate(text))
    
    def Printer(self):
        self.brand = f'''
    {self.fade('┏┓┳┓┏┓┏┓┏┓┓┏  ┏┓┏┓┳┓┏┓┏┓┏┓┳┓')}
    {self.fade('┃┃┣┫┃┃ ┃┃ ┗┫  ┗┓┃ ┣┫┣┫┃┃┣ ┣┫')}
    {self.fade('┣┛┛┗┗┛┗┛┗┛┗┛  ┗┛┗┛┛┗┛┗┣┛┗┛┛┗')}{self.reset}'''
        print(self.brand)

    def loader(self):
        self.load_list = []
        if str(self.type).lower() == "http" or str(self.type).lower() == "https":
            for link in self.proxy_list:
                link_without_prefix = link.split("://")[-1]
                if "http" in link_without_prefix:
                    self.load_list.append(link)
        elif str(self.type).lower() == "socks4" or str(self.type).lower() == "socks5":
            for link in self.proxy_list :
                if str(self.type).lower() in link:
                    self.load_list.append(link)
        elif str(self.type).lower() == "all" :
            self.load_list = self.proxy_list
        else :
            self.parser.print_help()
            exit()
        return self.load_list

    def scrape(self, url):
        proxylist = requests.get(url, timeout=20).text
        for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), proxylist):
            self.n += 1
            self.found.append(proxy)
            print(" Proxy Found : ", f"{self.rgb(0, 255, 255)}{self.n}{self.reset}", '|', f"{self.rgb(0, 255, 255)}{self.iteration}{self.reset}", '/', f"{self.rgb(0, 255, 255)}{len(self.loader())}{self.reset}", end='\r')
        
    def write_file(self):
        if self.output:
            with open(self.output, "w") as f:
                [f.write(f'{proxy[0]}:{proxy[1]}\n') for proxy in self.found]
                self.output = os.path.abspath(self.output)
        else :
            with open("output.txt", "w") as f:
                [f.write(f'{proxy[0]}:{proxy[1]}\n') for proxy in self.found]
                self.output = os.path.abspath("output.txt")
        print("\n Saved in : ", f"{self.rgb(0, 255, 255)}{self.output}{self.reset}")

    def worker(self):
        self.iteration = 0
        for i in self.loader() :
            self.iteration += 1
            self.scrape(i)
        self.write_file()

proxy_scrape().Printer()
proxy_scrape().worker()