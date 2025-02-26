import socket
import time
from PyQt5.QtCore import QThread, pyqtSignal

class TCPServer(QThread):
    data_received = pyqtSignal(str, str, str)        # 데이터 수신 시그널 정의     # main_app의 update_textBrowser 함수에 연결

    def __init__(self, mainwindow, ip, port, timeout=20):
        super().__init__()
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self._running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))  # 포트에서 수신
        self.sock.listen(1)  # 연결 대기
        self.conn = None
        self.objectName('tcpServer')
        self.pMainWindow = mainwindow

        self.pMainWindow.comboBox.text()                   # Main app의 변수를 상속받아 읽어올 수 있음(읽기만 가능) Main app 함수에 self 쓰고 읽는 함수에 임의 변수 지정 필요


    def run(self):
        try:
            self.wait_for_client()
            while self._running:
                self.receive_data()
                time.sleep(0.1)
        except Exception as e:
            self.data_received.emit(f"Error in TCP server: {self.__class__.__name__, self.objectName(), str(e)}")
        finally:
            if self.conn:
                self.conn.close()
            self.sock.close()

    def wait_for_client(self):
        self.data_received.emit(f"[*] TCP 서버 대기 중... ({self.ip}:{self.port})")
        self.sock.settimeout(self.timeout)  # 연결되지 않으면 타임아웃
        try:
            self.conn, addr = self.sock.accept()  # 클라이언트 연결 대기
            self.data_received.emit(f"[+] 클라이언트 연결됨: {addr}")
        except socket.timeout:
            self.data_received.emit("[!] 클라이언트 연결 타임아웃")
            self._running = False

    def receive_data(self):
        try:
            data = self.conn.recv(1024)
            if data:
                self.data_received.emit(f"[서버] 수신된 데이터: {data.decode()}")
        except Exception as e:
            self.data_received.emit(f"Error: {str(e)}")

    def send_data(self, address, data) -> bool:
        if self.conn:
            try:
                self.conn.sendall(data.encode())
                self.data_received.emit(f"[서버] 데이터 전송: {data}")
                return True
            except Exception as e:
                self.data_received.emit(f"Error: {str(e)}")

    def stop(self):
        self._running = False
        if self.conn:
            self.conn.close()
        self.sock.close()
        self.data_received.emit("[*] TCP 서버 종료")