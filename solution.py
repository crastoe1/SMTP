from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,1025))

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    fromCommand = 'MAIL FROM: <ec136@nyu.edu>\r\n'
    clientSocket.send(fromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
 
    # Fill in end

    # Send RCPT TO command and print server response.
    rcptCommand = 'RCPT TO: <ethan.crasto@gmail.com>\r\n'
    clientSocket.send(rcptCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)

    # Send DATA command and print server response.
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)

    # Send message data.
    clientSocket.send(msg.encode())
    rec5 = clientSocket.recv(1024).decode()

    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
    rec6 = clientSocket.recv(1024).decode()

    # Send QUIT command and get server response.
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv7 = clientSocket.recv(1024).decode()
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
