import socket
import sys

def create():
    try:
        global host
        global port
        global st
        host = ""
        port = 999
        s = socket.socket()
    except socket.error as msg:
        print("Socket error")

def bindSocket():
           try:
               global host
               global port
               global s
               print("binding socket")
           except socket.error as msg:
               print("socket binding error:" + msg)

def accept():
    conn, address = s.accept()
    print("Connection made")
    commands
    conn.close()
def commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close
            s.close()
            sys.exit(1)
            if len(str.encode(cmd)) > 0:
                pass
                print("response made!")

def main():
    socket()
    bindSocket()
    accept()
if __name__ == '__main__':
    main()