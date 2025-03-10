# Entry Point

import time
from v_mainWindow import Ui_MainWindow
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
            {'ip': '127.0.0.1', 'port': 8000},
            {'ip': '127.0.0.1', 'port': 8001},
            {'ip': '127.0.0.1', 'port': 8002},
            {'ip': '127.0.0.1', 'port': 8003},
            {'ip': '127.0.0.1', 'port': 8004},
            {'ip': '127.0.0.1', 'port': 8005},
            {'ip': '127.0.0.1', 'port': 8006},
            {'ip': '127.0.0.1', 'port': 8007},
            {'ip': '127.0.0.1', 'port': 8008},
            {'ip': '127.0.0.1', 'port': 8010},

        ]

        # txt 파일로부터 읽어오는 Info 변수
        self.file_open = None
        self.All_Info_data = None

        self.model_name = None
        self.Decoding = None
        self.AFDriverSlave = None
        self.Barcode_data_send = None
        self.Barcode_data_check = None

        # Populate customer folders
        self.populate_customer_folders()
        # 고객명이 선택되면 폴더 내의 스크립트 파일명을 모델명 콤보박스에 추가하는 시그널 연결
        self.ui.cb_customerName.currentIndexChanged.connect(self.populate_model_files)
        # 모델을 선택하면 통신준비와 Sensor Info.txt 파일 내용을 Wirte card로 전송하는 시그널 연결
        self.ui.cb_selectedModel.currentIndexChanged.connect(self.on_model_selected)

        sys.exit(app.exec_())


    # 'Open Model Data'를 클릭하면 Sensor Info 파일을 열고 정보 display
    def OpenModelData(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow, "Open txt File", "Text Files (*.txt);;All files (*)", options=options)
        if file_name:
            self.Send_Info(file_name)


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

    # Sensor Info.txt 파일을 한줄씩 Write card로 전송
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
        self.ui.textBrowser_4.append(f"{source}: {msg}")


    def update_widgets(self):
        self.MainWindow.setWindowTitle('PyQt5 GUI')

    # 고객 폴더들을 스캔하여 콤보박스에 추가 (프로그램 실행되면 자동 실행)
    def populate_customer_folders(self):
        customer_folder_path = os.path.join(os.getcwd(), 'customer')
        if os.path.exists(customer_folder_path) and os.path.isdir(customer_folder_path):
            subfolders = [f.name for f in os.scandir(customer_folder_path) if f.is_dir()]
            self.ui.cb_customerName.addItems(subfolders)

    # 고객 폴더가 지정되면 폴더 내 스크립트들을 콤보박스에 추가 (고객명 콤보박스 선택되면 자동 실행)
    def populate_model_files(self):
        selected_customer = self.ui.cb_customerName.currentText()
        if selected_customer:
            model_folder_path = os.path.join(os.getcwd(), 'customer', selected_customer)
            if os.path.exists(model_folder_path) and os.path.isdir(model_folder_path):
                model_files = [f.name for f in os.scandir(model_folder_path) if f.is_file() and f.name.endswith('.txt')]
                self.ui.cb_selectedModel.clear()
                self.ui.cb_selectedModel.addItems(model_files)

    # 통신 준비 및 스크립트를 Wirte card에 전송 (모델명 콤보박스 선택되면 자동 실행)
    def on_model_selected(self):
        selected_model = self.ui.cb_selectedModel.currentText()
        if selected_model:
            self.ui.lbl_equipmentId.setText(f"Model Name: {selected_model}")
            self.update_text_browser(f"Model Selected : {selected_model}")
            self.get_ready()
            model_folder_path = os.path.join(os.getcwd(), 'customer', self.ui.cb_customerName.currentText())
            file_path = os.path.join(model_folder_path, selected_model)
            self.Send_Info(file_path)


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