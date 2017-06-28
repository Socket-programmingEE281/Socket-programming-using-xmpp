import socket
import select

def broadcast_data (c_soc, message):
    for socket in client_array:
        if socket != s_soc and socket != c_soc :
                try :
                   socket.send(message)
                except :                           
                   socket.close()
                   client_array.remove(socket)                           

if __name__ == "__main__":
     
    client_array = []
    s_buffer = 4096
    s_port = 15000
    s_ip = "10.0.0.253"

    s_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s_soc.bind((s_ip,s_port))
    s_soc.listen(2)
    client_array.append(s_soc)
    print "Chat server started on port " + str(s_port)

    while 1:
        read_soc,write_soc,error_soc = select.select(client_array,[],[])
        for c_soc in read_soc:
            if c_soc == s_soc:
               c_socobj,c_add = s_soc.accept()
               client_array.append(c_socobj)
               print "client (%s, %s) connected" % c_add
               broadcast_data(c_socobj, "[%s:%s] entered room\n" % c_add)
            else:
                try:
                    message = c_soc.recv(s_buffer)
                    if message:
                       broadcast_data(c_soc, '<' + str(c_soc.getpeername()) + '>' + message)
                except:
                   broadcast_data(c_soc, "client is offline")
                   c_soc.close()
                   client_array.remove(c_soc)
                   continue
    server.socket.close()                                        