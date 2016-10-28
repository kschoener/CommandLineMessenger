import os
import json
import DataRetrieval as data

myData = None

commands = [
    'conversations',
    'open',
    'refresh',
    'send',
]

def main():
    global myData
    myData = data
    myData.main()
    interface()
#enddef main

def interface():
    mode = ''
    keepRunning = True
    while keepRunning:
        #if the user enters a command // group that doesn't exist try to autocomplete
        com = input('Command: ')
        keepRunning = check(com)
    #endwhile
#enddef interface

def check(com):
    if(com == 'exit' or com == 'logout'):
        return False
    elif com == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif len(com) == 0 or com == '?':
        prompt = 'Commands:'
        for command in commands:
            prompt += '\n'+command
        print(prompt)
    elif com in commands:
        doSomething(com)
    else:
        possibilities = ''
        for command in commands:
            if command.startswith(com):
                possibilities += '\n\t ' + command
        if(len(possibilities.strip().split(' ')) == 1):
            check(possibilities.strip().split(' ')[0])
        elif(len(possibilities) > 0):
            print('Could you have meant: '+possibilities)
        else:
            print(com+' not a valid command')
    #endif
    return True
#enddef check

def doSomething(com):
    if com == 'conversations':
        for openConv in myData.getOpenConversations():
            print(openConv)
    elif com == 'open':
        lookForConversation()
    else:
        print("Cool, you entered '"+com+"' which I've done nothing with")


def lookForConversation():
    conversations = myData.getOpenConversations()
    userInput = input("Which conversation would you like to open? (If you don't want to, enter '!'): ")
    if(userInput == '!'):
        return
    elif(userInput in conversations):
        showMessages(userInput)
    else:
        possibilities = ''
        for name in conversations:
            if name.startswith(userInput):
                possibilities += '\n\t ' + name
            #endif
        #endfor
        if(len(possibilities)==0):
            print('Not a valid conversation. Quitting open..')
        elif(len(possibilities.strip().split(' '))==1):
            print('Showing conversation for: '+possibilities.strip().split(' ')[0])
            showMessages(possibilities.strip().split(' ')[0])
        else:
            print('Did you mean'+possibilities)
            lookForConversation()
    #endif
#enddef lookForConversation

def showMessages(conversation):
    rows, columns = os.popen('stty size', 'r').read().split()
    rows = int(rows)
    columns = int(columns)
    #jsonData organized by:
    #{"names":{"kschoener6":"Kyle"}, "messages":[{"from":"fromname", "time":"12/23/2012 00:23:47", "text":"hello"},...]}
    jsonData = myData.getConversation(conversation)
    nickname = conversation
    names = jsonData['names']
    allMessages = jsonData['messages']
    for message in allMessages:
        infoLine, tempRowCount1 = fit(names[message['from']]+' on/at '+message['time'], columns)
        print('\n'+infoLine)
        messageContent, tempRowCount2 = fit(message['text'], columns)
        print(messageContent)
#enddef showMessages

def fit(line, columns):
    rowcount = 0
    if(len(line) < columns):
        for x in range(columns-len(line)):
            line += '_'
        #endfor
        rowcount += 1
    else:
        #this is where to split the message up into separate lines
        newLine = ''
        split = line.split(' ')
        rowcount += 1
        temp = 0
        for piece in split:
            if(temp + len(piece) + 1 > columns):
                newLine += '\n' + piece
                temp = 0
            else:
                temp += len(piece) + 1
                newLine += ' ' + piece
                rowcount += 1
            #endif
        #endfor
        line = newLine[1:]
    #endif
    return (line, rowcount)
#enddef fit

if __name__ == '__main__':
    main()
