#
# by d4v.id
#
import os, time
from colorama import Fore, Style, Back
from concurrent.futures import ThreadPoolExecutor
start_time = time.time()
bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
bgr = Back.GREEN
rd = Fore.RED
def screen_clear():
  _ = os.system('cls')

def v2(star):
 host = ''
 port = ''
 user = ''
 pwd = ''
 if "URL:" in star:
    star = fp.readline()
 if "METHOD:" in star:
    star = fp.readline()
 if "MAILHOST:" in star:
    star = star.replace(" ", "")
    star = star.replace('"', "")
    star = star.replace('\n', "")
    x = star.split(':', 1)
    host = x[1] + "|"
    star = fp.readline()
 if "MAILPORT:" in star:
    star = star.replace(" ", "")
    star = star.replace('"', "")
    star = star.replace('\n', "")
    x = star.split(':', 1)
    port = x[1] + "|"
    star = fp.readline()
 if "MAILUSER:" in star:
    star = star.replace(" ", "")
    star = star.replace('"', "")
    star = star.replace('\n', "")
    x = star.split(':', 1)
    user = x[1] + "|"
    star = fp.readline()
 if "MAILPASS:" in star:
    star = star.replace(" ", "")
    star = star.replace('"', "")
    star = star.replace("\n", "")
    x = star.split(':', 1)
    pwd = x[1]
    star = fp.readline()
 if "MAILFROM:" in star:
    star = fp.readline()
 if "FROMNAME:" in star:
    pass

 mrigel = open("Duplicated-smtp.txt", "a")
 mrigel.write(f'{host}{port}{user}{pwd}\n')
 mrigel.close()
 lines_seen = set()
 with open("format-smtp.txt", "w") as output_file:
   for each_line in open("Duplicated-smtp.txt", "r"):
     if each_line not in lines_seen:
       output_file.write(each_line)
       lines_seen.add(each_line)
 output_file.close()  


def v3(star):
 host = ''
 port = ''
 user = ''
 pwd = ''
 if "URL:" in star:
    star = fp.readline()
 if "METHOD:" in star:
    star = fp.readline()
 if "AWS ACCESS KEY:" in star:
    star = star.replace(" ", "")
    star = star.replace('"', "")
    star = star.replace('\n', "")
    x = star.split(':', 1)
    host = x[1] + "|"
    star = fp.readline()
 if "AWS SECRET KEY:" in star:
    star = star.replace(" ", "")
    star = star.replace('"', "")
    star = star.replace('\n', "")
    x = star.split(':', 1)
    port = x[1] + "|"
    star = fp.readline()
 if "AWS REGION:" in star:
    star = star.replace(" ", "")
    star = star.replace('"', "")
    star = star.replace('\n', "")
    x = star.split(':', 1)
    user = x[1]
    star = fp.readline()
    
 mrigel = open("Duplicated-aws.txt", "a")
 mrigel.write(f'{host}{port}{user}{pwd}\n')
 mrigel.close()
 lines_seen = set()
 with open("format-aws.txt", "w") as output_file:
   for each_line in open("Duplicated-aws.txt", "r"):
     if each_line not in lines_seen:
       output_file.write(each_line)
       lines_seen.add(each_line)
 output_file.close()      




#OUT
screen_clear()
print(Fore.GREEN+"\n\t//"+Style.RESET_ALL+Fore.RED+" d-Format AWS Key / SMTPs"+Style.RESET_ALL)
print(Fore.GREEN+"\t//"+Style.RESET_ALL+Fore.RED+" by d4v.id"+Style.RESET_ALL)
print("""
---- AWS KEY ----"""+Fore.GREEN+"""
URL: http://localhost
METHOD: debug
AWS ACCESS KEY: xxxxxxxx
AWS SECRET KEY: xxxxxxxx
AWS REGION: us-east-1
AWS BUCKET: xxxx

Format >> Aws_key|Aws_sec|Aws_reg
"""+Style.RESET_ALL+"""
----  SMTPs  ----"""+Fore.GREEN+"""
URL: http://localhost
METHOD: /.env
MAILHOST: volare.websiteexample.com
MAILPORT: 465
MAILUSER: "xxxxxxx"
MAILPASS: "xxxxxxx"
MAILFROM: "xxxx@lion-example.com"
FROMNAME: "xxxx"

Format >> mailhost|port|mailuser|mailpass
    """+Style.RESET_ALL)

print("\tChoose:")
print("\t  1. SMTPs")
print("\t  2. AWS Key")

try:
    select = int(input(Fore.GREEN+"\n\t>> "+Style.RESET_ALL))
    link = input("\tEnter Filename(.txt) :"+Fore.GREEN+"\n\t>> "+Style.RESET_ALL)
    if select == 1:
        if not os.path.isfile(link):
            print(f'{rd}Enter a valid .txt file')
        with open(link) as fp:
          for star in fp:
            if not star:
               pass
            with ThreadPoolExecutor(max_workers=50) as executor:
                executor.map(v2, [star])
                executor.shutdown(wait=True)

        print(f"\n\t[READY To CHECK] {rd}--- %s seconds --- {gr}format-smtp.txt {Style.RESET_ALL}" % (time.time() - start_time))

    elif select == 2:
        if not os.path.isfile(link):
            print(f'{rd}Enter a valid .txt file')
        with open(link) as fp:
          for star in fp:
            if not star:
               pass
            with ThreadPoolExecutor(max_workers=50) as executor:
                executor.map(v3, [star])
                executor.shutdown(wait=True)

        print(f"\n\t{gr}[READY To CHECK] {rd}--- %s seconds --- {gr}format-aws.txt {Style.RESET_ALL}" % (time.time() - start_time))

except ValueError:
    print(f"{rd}\nWrong Input...{Style.RESET_ALL}")
except FileNotFoundError:
    print(f"{rd}\nFile NotFound...{Style.RESET_ALL}")
except KeyboardInterrupt:
    print(f"{rd}\nExit...{Style.RESET_ALL}")