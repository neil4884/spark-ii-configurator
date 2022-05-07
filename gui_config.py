import serial
import cmdlist as cl


class SubSerial:
    def __init__(self):
        """

        """


class HardwareConfig:
    def __init__(self, device: serial.Serial):
        """
        A hardware-oriented configurator and useful tools object

        :param device:
        """
        self.device = device

    def writeCommandChained(self, *commands: str):
        for __command in commands:
            self.writeCommand(__command)
        return

    def writeCommand(self, command: str):
        self.device.write(command)
        return

    def readCommand(self) -> str:
        __out_str = self.device.readline().decode(encoding='utf-8', errors='replace')
        return __out_str.replace('\r', '').replace('\n', '').strip()

    def validateDevice(self) -> bool:
        return False

    def readDeviceId(self):
        self.writeCommand(cl.READ_ID)
        return

    def dfuEnter(self):
        return

    def dfuExit(self):
        return

    def sdEnter(self):
        return

    def sdExit(self):
        return

    def sdRead(self, file_name):
        return
