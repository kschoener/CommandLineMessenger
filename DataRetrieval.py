import os
import json
import getpass
# import requests #http://docs.python-requests.org/en/master/
# import urllib.request as urllib
# import urllib.request as request
# import urllib.parse as parse

import requests
from lxml import html

'''
Default Chats HTML:
in div class="guilds-wrapper"
<a draggable="false" class="avatar-small" href="/channels/81384788765712384/81384788765712384" style="background-image: url(&quot;https://cdn.discordapp.com/icons/81384788765712384/2aab26934e72b4ec300c5aa6cf67c7b3.jpg&quot;);"></a>

Default Channels HTML:
in div class="flex-vertical channels-wrap"
<div class="channel channel-text" draggable="true"><a draggable="false" href="/channels/81384788765712384/82648417347571712"><span class="channel-name">info</span><button class="icon icon-instant-invite"></button><!-- react-empty: 1000 --></a></div>

Default Chat HTML:
in div class="chat flex-vertical flex-spacer"
Member names: <div class="member member-status member-status-online"><div class="avatar-small stop-animation" style="background-image: url(&quot;https://cdn.discordapp.com/avatars/80088516616269824/3ecc8f35a128d481980b856e6fd49c5d.jpg&quot;);"><div class="status status-online"></div></div><div class="member-inner"><div class="member-username" style="color: rgb(0, 166, 111);"><span class="member-username-inner">Danny</span></div><div class="member-activity"><!-- react-text: 205 -->Playing <!-- /react-text --><strong><!-- react-text: 207 -->the lonely part of we<!-- /react-text --></strong></div></div></div>
Message View: <div class="message-group hide-overflow"><div class="avatar-large stop-animation" style="background-image: url(&quot;https://cdn.discordapp.com/avatars/57287406247743488/e66cd7fb8d9884c0b09504419d2c2c7d.jpg&quot;);"></div><div class="comment"><div class="message first"><div class="body"><h2><span class="username-wrapper"><strong class="user-name">Kowlin</strong></span><span class="highlight-separator"> - </span><span class="timestamp">Today at 2:29 AM</span></h2><div class="message-text"><div class="markup"><!-- react-text: 1228 -->someone has some example code for application scopes other then bot, the ones that require a RedirectURL<!-- /react-text --></div></div></div><div class="accessory"></div></div></div></div>
Message Entry: <div class="channel-textarea"><div class="channel-textarea-inner"><div class="channel-textarea-upload"><input type="file" class="file-input" multiple="" style="position: absolute; top: 0px; left: 0px; width: 100%; height: 100%; opacity: 0; cursor: pointer;"></div><textarea rows="1" placeholder="Message #general" style="height: auto; overflow: hidden;"></textarea><div class="channel-textarea-emoji"><div class="sprite-item" style="background-image: url(&quot;/assets/f6c2b01391865c4cb06ab768a9f098c6.png&quot;); background-size: 242px 110px;"></div></div></div></div>
'''
# url = 'https://www.discordapp.com/login'
url = 'https://www.discordapp.com/channels/@me'
username = None
password = None

# login_url = "https://discordapp.com/login"
login_url = "https://discordapp.com/channels/@me"

session_requests = None
# loginheaders = {
#     'authority':'discordapp.com',
#     'method':'POST',
#     'path':'/api/v6/auth/login',
#     'scheme':'https',
#     'accept':'*/*',
#     'accept-language':'en-US',
#     'content-length':'56',
#     'content-type':'application/json',
#     'accept-encoding':['gzip', 'deflate', 'br'],
#     'origin':'https://discordapp.com',
#     'referer':'https://discordapp.com/login',
#     'x-super-properties':'eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiJ9',
#     'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
# }
# 'cookie':'__cfduid=dd395bc5c79b8f56bf78296a8f110e9e01476856868'
def main():
    global username
    global password
    username = 'nunya'
    password = 'business'
    username = input('Enter Username: ')
    password = getpass.getpass(prompt='Enter Password: ')
    login()
    skipChangeLog()
    checkLogin("https://discordapp.com/channels/@me")
    checkLogin("https://discordapp.com/channels/226749461374828545/226749461374828545")
#enddef main

def skipChangeLog():
    meUrl = "https://discordapp.com/channels/@me"
    post = {
        "event" : "Change Log Closed",
        "properties" : {
            "seconds_open": 254,
            "max_scrolled_percentage": 0
        },
        "token" : "MjExMzIzMTQ3NDY5ODQ4NTg2.0H1wzplzHd4mb_yfW2IAzCSV3JA"
    }
    changeLogResult = session_requests.post(
        meUrl,
        data=post,
        headers=dict(referer=meUrl)
    )
    print("The skip change result is:\n"+str(changeLogResult.content))
    print("\n\n\n")
#enddef skipChangeLog


def checkLogin(check_url):
    print("Check url is: "+ check_url)
    checkResult = session_requests.get(
        check_url,
        headers=dict(referer=check_url)
    )
    print("Was the result okay? "+str(checkResult.ok).strip())
    print("Status code from login: "+str(checkResult.status_code).strip())
    print("The html is:\n"+str(checkResult.content).strip())
    print("\n\n\n")
#enddef checkLogin

def login():
    global session_requests
    session_requests = requests.session()
    loginPage = session_requests.get(login_url)
    loginresult = session_requests.post(
        login_url,
        data={"email": username, "password": password},
        headers=dict(referer=login_url)
    )
    print("Was the result okay? "+str(loginresult.ok).strip())
    print("Status code from login: "+str(loginresult.status_code).strip())
    print("Html is:\n"+str(loginresult.content))
    print("\n\n\n")

#enddef login

def getOpenConversations():
    conversations = []
    path = 'dummydata/conversations'
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            conversations.append(filename.split('.')[0].replace('_',' '))
    return conversations
#enddef getOpenConversations

def getConversation(conversationName):
    path = 'dummydata/conversations/'+conversationName.replace(' ','_')+'.json'
    data = None
    with open(path, 'r') as handle:
        data = json.loads(handle.read().strip())
    handle.close()
    return data
#enddef getConversation

def getUsername():
    return username
def getPassword():
    return password


































































# def main():
#     # getCreds()
#     # if(username == None or password == None):
#     #     while not checkCreds():
#     #         print('ERROR: Validation did not work. Try again..')
#     # req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#     # req = request.Request(url, headers=disheaders)
#     # html = request.urlopen(req).read()
#     # print(str(html))
#
#     # headers = {'user-agent':'Mozilla/5.0'}
#     values = {"email":"nunya@business.com","password":"tryme"}
#     # pretend to be a chrome 47 browser on a windows 10 machine
#     # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
#     # encode values for the url
#     values = parse.urlencode(values)
#     # encode the values in UTF-8 format
#     values = values.encode("UTF-8")
#     # create the url
#     print('created request')
#     targetUrl = request.Request(url = url, data = values, headers = headers)
#     print('trying to open url')
#     # open the url
#     try:
#         x  = request.urlopen(targetUrl)
#         print('opened url, getting source code')
#         # get the source code
#         sourceCode = x.read()
#         print(str(sourceCode))
#     except:
#         print('First method failed. Trying second')
#
#     # interface()
# #enddef main
#
# def getCreds():
#     global username
#     global password
#     with open('creds.txt', 'r') as handle:
#         lines = handle.readlines()
#         if(len(lines)>=2):
#             username = lines[0].strip()
#             password = lines[1].strip()
#     handle.close()
# #enddef getCreds
#
# def saveCreds():
#     with open('creds.txt', 'w') as handle:
#         handle.write(username+'\n'+password)
#     handle.close()
# #enddef saveCreds
#
# def getNewCreds():
#     global username
#     global password
#     username = input('Enter Username: ')
#     password = getpass.getpass(prompt='Enter Password: ')
#     print(username+':'+password)
# #enddef getNewCreds
#
# def checkCreds():
#     getNewCreds()
#     passman = request.HTTPPasswordMgrWithDefaultRealm()
#     # this creates a password manager
#     print('Created password manager')
#     passman.add_password(None, url, username, password)
#     # because we have put None at the start it will always
#     # use this username/password combination for  urls
#     # for which `url` is a super-url
#     print('Added credentials to pwManager')
#
#     authhandler = request.HTTPBasicAuthHandler(passman)
#     # create the AuthHandler
#     print('Created the authhandler')
#
#     opener = request.build_opener(authhandler)
#     print('Built opener')
#
#     request.install_opener(opener)
#     # All calls to request2.urlopen will now use our handler
#     # Make sure not to include the protocol in with the URL, or
#     # HTTPPasswordMgrWithDefaultRealm will be very confused.
#     # You must (of course) use it when fetching the page though.
#     print('Installed the Auth opener')
#
#     print('Trying to load the page')
#     pagehandle = request.urlopen(url)
#     # authentication is now handled automatically for us
#     print('Loaded the page!!')
#
#     print('Logged in fine.... crazy')
#     saveCreds()
#     return True

if __name__ == '__main__':
    main()
