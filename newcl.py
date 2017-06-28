import socket
import sys
import select


if __name__ = "__main__":
     
    if (len(sys.argv < 3)) :
       print 'Specify host name and port number'
       sys.exit()
    else
        server_ip = sys.argv(1)
        server_port = sys.argv(2)
        cl_soc = socket.socket(socket.AF_INIT, socket.SOCK_STREAM)
        cl_soc = settimeout(2)
        try:
          cl_soc.connect((server_ip,server_port))
        except:
           sys.exit()
        
        print 'client is connected to remote host'
        sys.stdout.write('<you>')
        sys.stdout.flush()

        while true:
            cl_array = [sys.stdin, cl_soc]
            read_soc,write_soc,error_soc = select.select(cl_array,[],[])
            for c_socket in read_sockets:
                if c_socket == cl_soc:
                   message = c_socket.recv(4096)
                    if message:
                     sys.sysout.write(message)
                     sys.stdout.write('<you>')
                     sys.stdout.flush()
                    else:
                     print 'Disconnnected from chat server'
                     sys.exit()
                else :
                  message_cl = sys.sysin.readline()
                  cl_soc =  send(message_cl)
                  sys.stdout.write('<you>')
                  sys.stdout.flush()
              
 
 
