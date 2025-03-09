import socket
import threading
import time
from PyQt5.QtCore import QThread, pyqtSignal

class TCPServer(QThread):
    data_received = pyqtSignal(str, str)        # 데이터 수신 시그널 정의     # main_app의 update_textBrowser 함수에 연결

    def __init__(self, mainwindow, ip, port, timeout=20):
        super().__init__()
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self._running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))                # 포트에서 수신
        self.sock.listen(8)                                 # 최대 8개의 클라이언트 연결 대기
        self.conn = None
        self.objectName('tcpServer')
        self.pMainWindow = mainwindow

        self.pMainWindow.comboBox.text()                   # Main app의 변수를 상속받아 읽어올 수 있음(읽기만 가능) Main app 함수에 self 쓰고 읽는 함수에 임의 변수 지정 필요


    def run(self):
        try:
            self.wait_for_client()
        except Exception as e:
            self.data_received.emit(f"Error in TCP server: {self.__class__.__name__, self.objectName(), str(e)}")
        finally:
            self.sock.close()

    def wait_for_client(self):
        self.data_received.emit(f"[*] TCP 서버 대기 중... ({self.ip}:{self.port})")
        self.sock.settimeout(self.timeout)                                  # 연결되지 않으면 타임아웃
        while self._running:
            try:
                client_socket, addr = self.sock.accept()                    # 클라이언트 연결 대기
                self.data_received.emit(f"[+] 클라이언트 연결됨: {addr}")
                # 새 스레드를 생성하여 클라이언트를 처리
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, addr))
                client_thread.start()
            except socket.timeout:
                self.data_received.emit("[!] 클라이언트 연결 타임아웃")
                self._running = False

    def handle_client(self, client_socket, addr):
        try:
            while self._running:
                data = client_socket.recv(1024)
                if data:
                    self.data_received.emit(f"Client {addr}", f"[서버] {addr}로부터 수신된 데이터: {data.decode()}")
                    client_socket.sendall("Message received".encode('utf-8'))
                time.sleep(0.1)
        except ConnectionResetError:
            self.data_received.emit("Server", f"[!] 클라이언트 연결 끊김: {addr}")
        finally:
            client_socket.close()

    def receive_data(self):
        try:
            data = self.conn.recv(1024)
            if data:
                self.data_received.emit(f"[서버] 수신된 데이터: {data.decode()}")
        except Exception as e:
            self.data_received.emit(f"Error: {str(e)}")

    def send_data(self, client_socket, data) -> bool:
        if client_socket:
            try:
                client_socket.sendall(data.encode())
                self.data_received.emit("Server", f"[서버] 데이터 전송: {data}")
                return True
            except Exception as e:
                self.data_received.emit("Server", f"Error: {str(e)}")
                return False

    def stop(self):
        self._running = False
        self.sock.close()
        self.data_received.emit("Server", "[*] TCP 서버 종료")