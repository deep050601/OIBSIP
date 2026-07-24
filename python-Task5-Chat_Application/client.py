import socket
import threading

def listen_from_server(c):
    while True:
        try:
            message = c.recv(2048).decode("utf-8")
            if message != "":
               time = message.split("~")[0]
               username = message.split("~")[1]
               content = message.split("~")[2]

               print(f"[{time}] {username}: {content}")
            else:
                  print("message recive from server is empty")
        except:
            print("disconnected from sever")
            c.close()
            break

def  send_message_to_server(c):
   while True:
      message=input("message: ")
      if message!='':
         c.sendall(message.encode())
      else:
         print("empty message")

def send_to_srever(c):
   username=input("Enter user name: ")
   if username!='':
      c.sendall(username.encode())
   else:
      print("user name cannot be empty")
   threading.Thread(target=listen_from_server,args=(c, ),daemon=True).start()
   send_message_to_server(c)

def main():
   c=socket.socket()
   try:
      c.connect(("localhost",9999))
      print("successfully connected to server ")
   except:
      print("enable to connect with server")

   send_to_srever(c)

if __name__=='__main__':
   main()
