import socket
import threading
from datetime import datetime

active_client=[]

def listen(c,username):
   while True:
      try:
         responce=c.recv(2048).decode('utf-8')
      
         if responce !='':
            time=datetime.now().strftime("%H:%M")
            final_msg = time + '~' + username + '~' + responce           
            send_message(final_msg)
         else:
            print(f"the message send from {username} is empty")
      except:
         print(f"{username} is disconnected")
         active_client.remove((username,c))
         time = datetime.now().strftime("%H:%M")
         send_message(f"{time}~SERVER~{username} left the chat")
         c.close()
         break

def send_message_c(c,message):
   c.sendall(message.encode())

def send_message(message):
   for user in active_client:
      send_message_c(user[1],message)

def c_handler(c):
   while True:
      try:
            username = c.recv(2048).decode("utf-8")
            if username != "":
               active_client.append((username, c))
               time = datetime.now().strftime("%H:%M")
               prompt = f"{time}~SERVER~{username} added to the chat"
               send_message(prompt)
               break
            else:
               print("Client username is empty")
      except ConnectionResetError:
            print("Client disconnected before sending username")
            c.close()
            return

   threading.Thread(target=listen, args=(c, username), daemon=True).start()


def main():
    s= socket.socket()

    try:
        s.bind(("localhost",9999))
        print("Running the server ")
    except:
        print("unable to connect with host and port")

    s.listen(5)

    while True:
        c, addr = s.accept()
        print("successfully connected with client", addr)
        threading.Thread(target=c_handler, args=(c,), daemon=True).start()


if  __name__=="__main__":
   main()
