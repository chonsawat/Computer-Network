from socket import(
    socket,
    gethostname
)
from pickle import dumps, loads

s = socket()
host = gethostname()
print(host)

port = 9999
s.bind((host,port))
s.listen()

print(host,port)
while True:
    c, addr = s.accept()
    print('Connection From : ',addr)
    c.send(dumps('Hi...I am groot'))



