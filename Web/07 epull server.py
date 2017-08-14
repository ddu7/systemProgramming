import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind('', 7788)

s.listen(10)

epoll = select.epoll()

epoll.register(s.fileno(), select.EPOLLIN | select.EPOLLET)

connections, addresses = {}, {}

while True:
    epoll_list = epoll.poll()

    for fd, event in epoll_list:
        if fd == s.fileno():
            conn, addr = s.accept()

            print 'new client: %s'%str(addr)

            connections[conn.fileno()] = conn
            addresses[conn.fileno()] = addr

            epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)

        elif event == select.EPOLLIN:
            recvData = connections[fd].recv(1024)
            if len(recvData) > 0:
                print 'recv: %s' %(recvData)
            else:
                epoll.unregister(fd)
                connections[fd].close()

                print("%s---offline---" % str(addresses[fd]))
