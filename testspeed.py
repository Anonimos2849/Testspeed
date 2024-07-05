import time
import socket

def download_speed_test(server='8.8.8.8', port=53, package_size=1024):
    start_time = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, port))

    sock.send(b'*3\r\n' + b'$1' + b'\r\n' + b'server-speed-test\r\n' + b'*\r\n' + b'.\r\n')
    response, _ = sock.recvfrom(package_size + 1)

    end_time = time.time()
    duration = end_time - start_time
    return package_size / duration / 1024

def upload_speed_test(server='8.8.8.8', port=53, package_size=1024):
    start_time = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, port))

    sock.send(b'*3\r\n' + b'$\r\n' + b'client-ip\r\n' + b'*' + str(socket.gethostname()).encode() + b'\r\n' + b'.\r\n')
    response, _ = sock.recvfrom(package_size + 1)

    sock.send(b'*3\r\n' + b'$1\r\n' + b'server-speed-test\r\n' + b'*\r\n' + b'.\r\n')
    response, _ = sock.recvfrom(package_size + 1)

    end_time = time.time()
    duration = end_time - start_time
    return package_size / duration / 1024

download_speed = download_speed_test()
upload_speed = upload_speed_test()

print(f"Download Speed: {download_speed} Kbps")
print(f"Upload Speed: {upload_speed} Kbps")