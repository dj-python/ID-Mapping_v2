# Entry Point

import time
from ID_Mapping_GUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from PyQt5.QtCore import pyqtSignal, QThread
import socket
from c_tcp_server import TCPServer
import os

class MainGUI:
    def __init__(self):
        super().__init__()
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.update_widgets()
        self.MainWindow.show()
        self.currentTime = ''

        #self.apply_stylesheet('style.qss')


        # 취득한 Sensor ID 변수 : 두번 확인해서 비교해야 하므로 2개씩 할당
        self.SensorID1 = None
        self.SensorID2 = None

        # 연속실행 변수
        self.isExecProcess = False

        self.connMain = []

        # 서버 IP와 포트 목록
        self.server_addresses = [
            {'ip': '127.0.0.1', 'port': 8001},
            {'ip': '127.0.0.1', 'port': 8002},
            {'ip': '127.0.0.1', 'port': 8003},
            {'ip': '127.0.0.1', 'port': 8004},
            {'ip': '127.0.0.1', 'port': 8005},
            {'ip': '127.0.0.1', 'port': 8006},
            {'ip': '127.0.0.1', 'port': 8007},
            {'ip': '127.0.0.1', 'port': 8008},
        ]


        # region button clicked
        self.ui.pushButton_OpenModelData.clicked.connect(self.OpenModelData)
        self.ui.pushButton_READY.clicked.connect(self.get_ready)

        # txt 파일로부터 읽어오는 Info 변수
        self.file_open = None
        self.All_Info_data = None

        self.model_name = None
        self.Decoding = None
        self.AFDriverSlave = None
        self.Barcode_data_send = None
        self.Barcode_data_check = None

        sys.exit(app.exec_())


    # 'Open Model Data'를 클릭하면 Sensor Info 파일을 열고 정보 display
    def OpenModelData(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow, "Open txt File", "Text Files (*.txt);;All files (*)", options=options)
        if file_name:
            self.Send_Info(file_name)

        # model name display
        self.model_name = self.extract_info('Model Name :')
        self.ui.textBrowser_ModelName.append(self.model_name)
        # Decoding 여부 display
        self.Decoding = self.extract_info('Decoding Enable = ')
        if self.Decoding == '1':
            self.ui.textBrowser_decoding.append('Enable')
        else :
            self.ui.textBrowser_decoding.append('Disable')
        # AF Driver IC 접근 여부 display
        self.AFDriverSlave = self.extract_info('AF Driver IC (if necessary), ')
        if self.AFDriverSlave is not None:
            self.ui.textBrowser_AFDriverIC.append(self.AFDriverSlave)
        else :
            self.ui.textBrowser_AFDriverIC.append('not access')



    def get_ready(self):
        for address in self.server_addresses:
            server = TCPServer(self, address['ip'], address['port'])
            server.data_received.connect(self.update_text_browser)
            server.start()
            self.connMain.append(server)
            self.update_text_browser(f"[*] 서버 시작됨 ({address['ip']}:{address['port']})")

    # 검사 시작을 위한 Pusher 이동
    def pusherLoad(self):
        pass




    # 텍스트 파일에서 특정 문구를 찾아 그 이후의 문자를 리턴
    def extract_info(self, text):
        with open('Sensor Info.txt', 'r', encoding='utf-8') as file_open:
            self.All_Info_data = file_open.readlines()

        for line in self.All_Info_data:
            line = line.strip()
            if text in line:
                start_index = line.index(text)
                extracted_value = line[start_index + len(text):].strip()
                if extracted_value:
                    return extracted_value
        return ''


    # Sensor Info.txt 파일을 한줄씩 PICO로 전송
    def Send_Info(self, file_path):
        try :
            if not os.path.exists(file_path):
                self.update_text_browser("[Error] 선택한 파일이 존재하지 않습니다.")
                return

            with open(file_path, 'r', encoding='utf-8') as self.file_open:
                self.All_Info_data = self.file_open.readlines()

            if not self.All_Info_data:
                self.update_text_browser("[Error] 선택한 파일이 비어 있습니다.")
                return

            for line in self.All_Info_data:
                try :
                    for server in self.connMain:
                        server.conn.sendall(line.encode('utf-8'))
                        self.update_text_browser(f"[서버] 데이터 전송 : {line.strip()}")
                    time.sleep(0.01)
                except Exception as e:
                    self.update_text_browser(f"[Error] 데이터 전송 실패: {str(e)}")
                    return
        except Exception as e:
            self.update_text_browser(f"[Error] 파일 읽기 실패 : {str(e)}")

    def update_text_browser(self, source, msg):                 # 여러 인스턴스로부터 시그널을 받을 때 구분하기 위해 className, obj 인수 설정
        self.ui.textBrowser_Log.append(f"{source}: {msg}")


    def update_widgets(self):
        self.MainWindow.setWindowTitle('PyQt5 GUI')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_app = MainGUI()
    main_app.MainWindow.show()

    sys.exit(app.exec_())





"""
    def apply_stylesheet(self, path):
        with open(path, 'r') as file:
            self.setStyleSheet(file.read())
"""