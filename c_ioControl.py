# H/W 제어 (실린더, 시그널 타워, 스위치 등등)

from machine import Pin
import time
import c_tcp_server
import c_tcp_client_IO as TCPClient

class PusherStatus:
    UNKNOWN = 1
    READY = 2
    DOING = 3
    ERROR = 4

class PusherError:
    NONE = 'ERROR_NONE'
    PUSHER_BACK = 'ERROR_PUSHER_BACK'
    PUSHER_FRONT = 'ERROR_PUSHER_FRONT'
    PUSHER_UP = 'ERROR_PUSHER_UP'
    PUSHER_DOWN = 'ERROR_PUSHER_DOWN'

class MainPusher:
    cTemp = 0

    def __init__(self):
        self.sysBuzzer = Pin(14, Pin.OUT)
        self.gpioIn_sel = Pin(15, Pin.OUT)
        self.sysLed_pico = Pin(25, Pin.OUT)
        self.sysLed_board = Pin(28, Pin.OUT)

        #region Init GPIO_OUT
        self.gpioOut_pusherBack = Pin(0, Pin.OUT)
        self.gpioOut_pusherFront = Pin(1, Pin.OUT)
        self.gpioOut_pusherUp = Pin(2, Pin.OUT)
        self.gpioOut_pusherDown = Pin(3, Pin.OUT)
        #end region

        #region Init GPIO_IN
        self.gpioIn0 = Pin(10, Pin.IN)
        self.gpioIn1 = Pin(11, Pin.IN)
        self.gpioIn2 = Pin(12, Pin.IN)
        self.gpioIn3 = Pin(13, Pin.IN)

        self.gpioIn4 = Pin(22, Pin.IN)
        self.gpioIn5 = Pin(26, Pin.IN)
        self.gpioIn6 = Pin(27, Pin.IN)

        self.gpioIn_pusherBack = None
        self.gpioIn_PusherFront = None
        self.gpioIn_PusherUp = None
        self.gpioIn_PusherDown = None
        self.gpioIn_Light = None
        self.gpioIn_PushButtonLeft = None
        self.gpioIn_PushButtonRight = None
        #end region

        TCPClient.init(server_ip= '', server_port='')

        self.rxMessage = str()

        self.cntExecProcess = 0
        self.cntTimeOutExecProcess = 0

        self.isExecProcess_unit0p = False
        self.idxExecProcess_unit0p = 0
        self.isExecProcess_loadUnload = False
        self.idxExecProcess_loadUnload = 0

        self.pusherStatus = PusherStatus.UNKNOWN
        self.pusherError = PusherError.NONE

        self.isInitedSocket = False
        self.isExecProcess_initPusherPos = False
        self.idxExecProcess_initPusherPos = 0

    def init_gpioOut(self):
        self.set_gpioOut(self.sysBuzzer, False)
        self.set_gpioOut(self.gpioOut_pusherUp, False)
        self.set_gpioOut(self.gpioOut_pusherDown, False)
        self.set_gpioOut(self.gpioOut_pusherBack, False)
        self.set_gpioOut(self.gpioOut_pusherFront, False)


    @staticmethod
    def set_gpioOut(target, value):
        target.value(not value)

    def get_gpioIn(self):
        self.gpioIn_pusherBack = not self.gpioIn0.value()
        self.gpioIn_PusherFront = not self.gpioIn1.value()
        self.gpioIn_PusherUp = not self.gpioIn2.value()
        self.gpioIn_PusherDown = not self.gpioIn3.value()
        self.gpioIn_Light = not self.gpioIn4.value()
        self.gpioIn_PushButtonLeft = not self.gpioIn5.value()
        self.gpioIn_PushButtonRight = not self.gpioIn6.value()

    def func_10msec(self):
        message, address = TCPClient.receive_data()
        if message is not None:
            self.rxMessage = message.decode('utf-8')
            print(address, self.rxMessage, self.pusherStatus)

            if self.rxMessage[1:3] == '20':
                self.cntTimeOutExecProcess = 0
                self.idxExecProcess_initPusherPos = 0
                self.pusherStatus = PusherStatus.DOING
                self.isExecProcess_initPusherPos = True

    def func_100msec(self):
        if self.isExecProcess_loadUnload:
            self.execProcess_loadUnload()
        elif self.isExecProcess_unit0p:
            self.execProcess_unit0p()


    def execProcess_loadUnload(self):
        if self.rxMessage[3:5] == '00':
            if self.idxExecProcess_loadUnload == 1:                     # Pusher 전진 동작
                self.set_gpioOut(self.gpioOut_pusherFront, True)
                self.set_gpioOut(self.gpioOut_pusherBack, False)
                self.idxExecProcess_loadUnload += 1
            elif self.idxExecProcess_loadUnload == 2:                   # Pusher 전진 확인
                self.pusherError = PusherError.PUSHER_FRONT
                if self.gpioIn_PusherFront:
                    self.cntTimeOutExecProcess = 0
                    self.cntExecProcess = 0
                    self.idxExecProcess_loadUnload += 1
            elif self.idxExecProcess_loadUnload == 3:                   # delay 500ms 부여 구간
                self.cntExecProcess += 1
                if self.cntExecProcess >= 5:
                    self.cntTimeOutExecProcess = 0
                    self.idxExecProcess_loadUnload += 1
            elif self.idxExecProcess_loadUnload ==4:                   # Pusher 하강 동작
                self.set_gpioOut(self.gpioOut_pusherUp, False)
                self.set_gpioOut(self.gpioOut_pusherDown, True)
                self.cntExecProcess = 0
                self.idxExecProcess_loadUnload += 1
            elif self.idxExecProcess_loadUnload == 5:                   # Pusher 하강 확인
                self.pusherError = PusherError.PUSHER_DOWN
                if self.gpioIn_PusherDown:
                    self.isExecProcess_loadUnload = False
                    self.pusherStatus = PusherStatus.READY
                    self.pusherError = PusherError.NONE
                    self.replyMessage('S' + self.rxMessage[1:5] + '000')
        self.cntTimeOutExecProcess += 1
        if self.cntTimeOutExecProcess >= 30:
            errorCode = self.checkErrorCode()

            self.isExecProcess_loadUnload = False
            self.pusherStatus = PusherStatus.ERROR
            self.pusherError = PusherError.LOAD_UNLOAD
            self.replyMessage('S' + self.rxMessage[1:5] + errorCode)


    def checkErrorCode(self):
        errorCode = '001'

        if self.pusherError == PusherError.PUSHER_FRONT:
            errorCode = '010'
        if self.pusherError == PusherError.PUSHER_BACK:
            errorCode = '011'




        pass

    def execProcess_unit0p(self):
        pass
