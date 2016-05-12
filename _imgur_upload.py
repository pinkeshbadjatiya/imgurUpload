import pyimgur
import time
import pynotify
import urllib2
import json
import pyperclip
import sys


CLIENT_ID = ""     # As shown on imgur.com
PATH = ""

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def get_name(name):
    return name.split('/')[-1]

#def generateRandomName():
#    content = urllib2.urlopen("https://randomuser.me/api/").read()
#    return json.loads(content)['results'][0]['user']['username']


# MAIN FUNCTION
if __name__ == "__main__":
    pynotify.init("Imgur Upload Script")
    if len(sys.argv) !=2:
        notice = pynotify.Notification("IMGUR Upload | CLIPBOARD", "Please provide a file name :|")
        notice.set_urgency(pynotify.URGENCY_CRITICAL)
        notice.show()
        exit(1)

    PATH = sys.argv[1]
    if PATH == "":
        notice = pynotify.Notification("IMGUR Upload | CLIPBOARD", "Please provide a VALID file name :|")
        notice.set_urgency(pynotify.URGENCY_CRITICAL)
        notice.show()
        exit(1)
        
        
    im = pyimgur.Imgur(CLIENT_ID)
    #uploaded_image = im.upload_image(PATH, title=generateRandomName())
    uploaded_image = im.upload_image(PATH, title=get_name(PATH))
    pynotify.init("Imgur Upload Script")
    
    message = ""
    message += uploaded_image.title
    message += '<br>'
    message += uploaded_image.link
    message += '<br>'
    message += sizeof_fmt(uploaded_image.size)
    message += '<br>'
    message += time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(uploaded_image.datetime))
    message += '<br>'
    
    notice = pynotify.Notification("IMGUR Upload | CLIPBOARD", message)
    notice.set_urgency(pynotify.URGENCY_CRITICAL)
    notice.show()
    pyperclip.copy(uploaded_image.link)
    print uploaded_image.link

