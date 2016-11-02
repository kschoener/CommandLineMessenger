# **CommandLineMessenger**

## Currently Being Developed:
I've run into issues attempting to login to Discordapp via requests. While I'm digging into that problem I will be focusing on the command line interface. I'll add in colors so that the user can choose a color scheme that suits them.

## Motivation / Goal:
My goal is to provide a simple and smooth user experience when messaging via the command line. And giving hackers their dream messaging service

The idea behind scraping data from Discordapp is to provide a very in depth example on the capabilities of the messaging interface, so hopefully in the future developers will implement my messaging interface with their own chat services or their own hacks on bigger chat services like Slack or Facebook Messenger.

## **Current Functionality**
- Built-in backend class that is to be edited by developers
- Working UI that wraps text based on the current size of the terminal
- Frontend connected to Backend (the backend just needs the functionality)

### User Data is not stored
This is due to the lack of security knowledge I have, if you have any ideas let me know!

In the meantime, this is how credentials are prompted:
```
username = input('Enter Username: ')
password = getpass.getpass(prompt='Enter Password: ')
```

The DataRetrieval file is littered with failed attempts of connecting to Discordapp. I urge you not to use that code as it doesn't work.
