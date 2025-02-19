import time
from ID_Mapping_Test_UI import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import pyqtSignal, QThread
import socket
from tcp_server import TCPServer
import config

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

        # 취득한 Sensor ID 변수 : 두번 확인해서 비교해야 하므로 2개씩 할당
        self.SensorID1 = None
        self.SensorID2 = None

        # 연속실행 변수
        self.isExecProcess = False

        self.connMain = ''

        # region button clicked
        self.ui.pushButton_connect.clicked.connect(self.connection)
        self.ui.pushButton_Load_Model_data.clicked.connect(self.read_Sensor_info)
        self.ui.pushButton_Get_SensorID.clicked.connect(self.Send_Info)
        self.ui.pushButton_Write_EEPROM.clicked.connect(self.Write_EEPROM)
        self.ui.pushButton_Check_EEPROM.clicked.connect(self.Check_EEPROM)

        # txt 파일로부터 읽어오는 Info 변수
        self.file_open = None
        self.All_Info_data = None

        sys.exit(app.exec_())

    # 클라이언트와 연결
    def connection(self):
        self.connMain = TCPServer(self, config.serverIp, config.serverPort)
        self.connMain.data_received.connect(self.update_text_browser)

        self.connMain.start()
        self.update_text_browser("[*] 서버 시작됨")

    # 텍스트 파일에서 '0x' 이후의 문자열만 추출하여 각 변수에 저장
    def Sensor_extract_info(self, index):
        if '0x' in self.All_Info_data[index]:
            start_index = self.All_Info_data[index].index('0x')
            extracted_value = self.All_Info_data[index][start_index+2:start_index+6]
            if extracted_value is not None:
                print(extracted_value)
                return extracted_value
            return ''

    def streaming_setting(self):
        with open('Sensor Info.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        for index, line in enumerate(lines):
            if '# Sensor' in line:
                if index + 1< len(lines):
                    return lines[index+1].strip()
        return None


        self.file_open = open('Sensor Info.txt', 'r')
        self.All_Info_data = self.file_open.readlines()
        self.file_open.close()




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

    def Send_Info(self):
        sender = TCPServer(config.serverIp, 6571)
        success = sender.send_data(config.writeCardIpPort, config.Slave_IDs)
        if success:
            self.update_text_browser('Slave ID 데이터 전송 성공')
        time.sleep(0.1)
        success = sender.send_data(config.writeCardIpPort, config.Sensor_Streaming_Resister_Addresses)
        if success:
            self.update_text_browser('Sensor Streaming Resister Address 전송 성공')
        time.sleep(0.1)
        success = sender.send_data(config.writeCardIpPort, config.Sensor_Streaming_Datas)
        if success:
            self.update_text_browser('Sensor Streaming Resister data 전송 성공')

    def update_text_browser(self, className, obj, msg):                 # 여러 인스턴스로부터 시그널을 받을 때 구분하기 위해 className, obj 인수 설정
        self.ui.textBrowser_Log.append(msg)


    def Write_EEPROM(self):
        pass

    def Check_EEPROM(self):
        pass

    def update_widgets(self):
        self.MainWindow.setWindowTitle('PyQt5 GUI')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_app = MainGUI()
    main_app.show()

    sys.exit(app.exec_())