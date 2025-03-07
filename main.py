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

        self.apply_stylesheet('style.qss')

    def apply_stylesheet(self, path):
        with open(path, 'r') as file:
            self.setStyleSheet(file.read())

        # 취득한 Sensor ID 변수 : 두번 확인해서 비교해야 하므로 2개씩 할당
        self.SensorID1 = None
        self.SensorID2 = None

        # 연속실행 변수
        self.isExecProcess = False

        self.connMain = ''

        # region button clicked
        self.ui.pushButton_connect.clicked.connect(self.connection)
        self.ui.pushButton_Get_SensorID.clicked.connect(self.open_file_dialog)

        # txt 파일로부터 읽어오는 Info 변수
        self.file_open = None
        self.All_Info_data = None

        self.serverIp = '127.0.0.0'
        self.serverPort = 8000

        sys.exit(app.exec_())

    # 클라이언트와 연결
    def connection(self):
        self.connMain = TCPServer(self, self.serverIp, self.serverPort)
        self.connMain.data_received.connect(self.update_text_browser)

        self.connMain.start()
        self.update_text_browser("[*] 서버 시작됨")

    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow, "Open txt File", "Text Files (*.txt);;All files (*)", options=options)
        if file_name:
            self.Send_Info(file_name)


    # 텍스트 파일에서 '0x' 이후의 문자열만 추출하여 각 변수에 저장
    def Sensor_extract_info(self, index):
        if '0x' in self.All_Info_data[index]:
            start_index = self.All_Info_data[index].index('0x')
            extracted_value = self.All_Info_data[index][start_index+2:start_index+6]
            if extracted_value is not None:
                print(extracted_value)
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
                    self.connMain.conn.sendall(line.encode('utf-8'))
                    self.update_text_browser(f"[서버] 데이터 전송 : {line.strip()}")
                    time.sleep(0.01)
                except Exception as e:
                    self.update_text_browser(f"[Error] 데이터 전송 실패: {str(e)}")
                    return
        except Exception as e:
            self.update_text_browser(f"[Error] 파일 읽기 실패 : {str(e)}")









    def update_text_browser(self, className, obj, msg):                 # 여러 인스턴스로부터 시그널을 받을 때 구분하기 위해 className, obj 인수 설정
        self.ui.textBrowser_Log.append(msg)


    def update_widgets(self):
        self.MainWindow.setWindowTitle('PyQt5 GUI')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_app = MainGUI()
    main_app.show()

    sys.exit(app.exec_())




"""
        # txt 파일로부터 읽어온 Info 리스트를 각 변수에 할당
        def read_Sensor_info(self):
            self.file_open = open('Sensor Info.txt', 'r')
            self.All_Info_data = self.file_open.readlines()
            self.file_open.close()
            print(self.All_Info_data)

            config.Slave_IDs = 'H10' + ''.join(self.extract_info(i) for i in range(4,8))
            config.Write_Protections = 'H11' + ''.join(self.extract_info(i) for i in range(10, 13))
            config.Sensor_Streaming_Resister_Addresses = 'H12' + ''.join(self.extract_info(i) for i in range(13, 18))
            config.Sensor_Streaming_Datas = 'H13' + ''.join(self.extract_info(i) for i in range(19, 24))
            config.Sensor_Reading_Resister_Addresses = 'H14' + ''.join(self.extract_info(i) for i in range(25, 28))
            config.Sensor_Write_Resister_Addresses = 'H15' + ''.join(self.extract_info(i) for i in range(29, 34))
            config.Sensor_Write_Datas = 'H16' + ''.join(self.extract_info(i) for i in range(35, 40))
            config.Sensor_Read_Resister_Addresses = 'H17' + ''.join(self.extract_info(i) for i in range(41, 48))
            config.EEPROM_Writing_Resister_Addresses = 'H18' + ''.join(self.extract_info(i) for i in range(49, 54))

            # txt 파일로부터 읽어온 데이터를 textBrowser에 표시
            for i in range(4, 24):
                extracted_info = self.extract_info(i)
                if extracted_info:
                    self.ui.textBrowser_model_data.append(config.All_Info[i] + ' = 0x' + self.extract_info)
"""