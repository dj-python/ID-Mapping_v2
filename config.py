# 이 모듈은 main_app에서 사용할 변수를 저장하는 공간임.

# MainPC 에서 변수로 입력받을 Slave address
Slave_IDs = ''
# end region

# EEPROM Write Resister, Disable, Enable
Write_Protections = ''

# 센서 스트리밍 레지스터 어드레스 1~5
Sensor_Streaming_Resister_Addresses = ''

# 센서 스트리밍 데이터 1~5
Sensor_Streaming_Datas = ''

# 센서 reading 레지스터 주소 1~3
Sensor_Reading_Resister_Addresses = ''

# 센서 Write 레지스터 주소 1~5
Sensor_Write_Resister_Addresses = ''

# 센서 Write data 1~5
Sensor_Write_Datas = ''

# 센서 Read Resister 1~7
Sensor_Read_Resisters = ''

# EEPROM Write 레지스터 주소 1~6
EEPROM_Writing_Resister_Addresses = ''

# Main PC로부터 받은 바코드 정보
barcode = None

# IP, Port
serverIp = '166.79.26.142'
serverPort = 8000
serverIpPort = ('166.79.26.142', 8000)
writeCardIpPort = ('166.79.26.140', 8000)

All_Info = [
    ''
    ''
    ''
    ''
    'Sensor Slave address'
    'EEPROM Slave address'
    'AF_Driver Slave address'
    'OIS Driver Slave address'
    ''
    'EEPROM Write protection resister address'
    'EEPROM Write protection disable'
    'EEPROM Write protection enable'
    ''
    'Sensor Streaming Resister Address 1'
    'Sensor Streaming Resister Address 2'
    'Sensor Streaming Resister Address 3'
    'Sensor Streaming Resister Address 4'
    'Sensor Streaming Resister Address 5'
    ''
    'Sensor Streaming Write data 1'
    'Sensor Streaming Write data 2'
    'Sensor Streaming Write data 3'
    'Sensor Streaming Write data 4'
    'Sensor Streaming Write data 5'
    ''
    'Sensor Reading Resister Address 1'
    'Sensor Reading Resister Address 2'
    'Sensor Reading Resister Address 3'
    ''
    'Sensor Write Resister Address 1'
    'Sensor Write Resister Address 2'
    'Sensor Write Resister Address 3'
    'Sensor Write Resister Address 4'
    'Sensor Write Resister Address 5'
    ''
    'Sensor Write Data 1'
    'Sensor Write Data 2'
    'Sensor Write Data 3'
    'Sensor Write Data 4'
    'Sensor Write Data 5'
    ''
    'Sensor Read Resister Address 1'
    'Sensor Read Resister Address 2'
    'Sensor Read Resister Address 3'
    'Sensor Read Resister Address 4'
    'Sensor Read Resister Address 5'
    'Sensor Read Resister Address 6'
    'Sensor Read Resister Address 7'
    ''
    'EEPROM Writing Resister Address 1'
    'EEPROM Writing Resister Address 2'
    'EEPROM Writing Resister Address 3'
    'EEPROM Writing Resister Address 4'
    'EEPROM Writing Resister Address 5'
    'EEPROM Writing Resister Address 6(Barocde)'
    ]






