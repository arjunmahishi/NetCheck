import os

def getCommand(title, body):
    return "notify-send '%s' '%s'" % (title, body)

def notify(title, body):
    os.system(getCommand(title, body))

if __name__ == "__main__":
    notify("test", "test")