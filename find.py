import requests
print('Git Directory Finder')
print('Author : angga1337\n')

az = input('list: ')
url = open(az, 'r')
exploit = '/.git'

def gitFind():
        global url,exploit
        for a in url.readlines():
                b = a.replace('\n', '')
                try:
                        r = requests.get(b+exploit)
                        if 'Index of /.git' in r.text:
                                print('[\033[1;32;40m+\033[0;37;40m] '+b+'/.git --> \033[1;32;40mGit Directory Found!\033[0;37;40m')
                                makeResult = open('result.txt', 'a')
                                makeResult.write(b)
                        else:
                                print('[\033[1;31;40mx\033[0;37;40m] '+b+' --> \033[1;31;40mFailed!\033[0;37;40m')
                except:
                        print('[\033[1;31;40mx\033[0;37;40m] '+b+' --> \033[1;31;40mError Site!\033[0;37;40m')

gitFind()
