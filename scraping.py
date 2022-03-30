import requests
import argparse
# Run
# python scraping.py -t https://shopage.es
parser = argparse.ArgumentParser(description = "Detector de Web")
parser.add_argument('-t', '--target', help="objetivo")
parser = parser.parse_args()

def main():
    if parser.target:
        try:
            url=requests.get(url=parser.target)
            web = dict(url.headers)
            for x in web:
                print(x+" : " + web[x])
        except:
            print("No se logro llegar al objetivo")
    else:
        print("No se encuentra objetivo")
        
if __name__ == '__main__':
    main()




