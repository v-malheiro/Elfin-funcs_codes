#-------------------MOVEREL------------------#
    def MoveRelL(self, coordinate, direction, distance):
        """
        function: Robot moves straight to the specified space coordinates
        :param: target:[X,Y,Z,RX,RY,RZ]
        :return:
        """
        target = [coordinate, direction, distance]
        target = [str(s) for s in target]
        target = (",".join(target))
        message = "MoveRelL," + self.rbtID + ',' + target + self.end_msg
        return self.send(message)
    
    def MoveRelJ(self, coordinate, direction, distance):
        """
        function: Robot moves straight to the specified space coordinates
        :param: target:[X,Y,Z,RX,RY,RZ]
        :return:
        """
        target = [coordinate, direction, distance]
        target = [str(s) for s in target]
        target = (",".join(target))
        message = "MoveRelJ," + self.rbtID + ',' + target + self.end_msg
        return self.send(message)

    def CalibrationL(self, coordinate, direction, distance):
        status = self.ReadMoveState()
        while status == 1009:
            status = self.ReadMoveState()
            self.MoveRelL(coordinate, direction, distance)
    
    def CalibrationJ(self, coordinate, direction, distance):
        status = self.ReadMoveState()
        while status == 1009:
            status = self.ReadMoveState()
            self.MoveRelL(coordinate, direction, distance)
    #-------------------MOVEREL------------------#

#---------------------CALIBRAÇÂO----------------#
from typing import NoReturn
import elfin
import time

SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 10003
SIZE = 1024
rbtID = 0

cobot = elfin.elfin()
cobot.connect(SERVER_IP, PORT_NUMBER, SIZE, rbtID)

targetJ = [0.000,13.139,70.271,38.306,27.023,0.000]
cobot.MoveJ(targetJ)

status = cobot.ReadMoveState()
if status == 0:
    cobot.MoveHoming()
i = 0

while i < 1:
    cobot.CalibrationL(2,0,200)
    cobot.CalibrationL(1,0,200)
    cobot.CalibrationL(2,1,200)
    cobot.CalibrationL(1,1,200)

    cobot.CalibrationL(0,1,200)
    cobot.CalibrationL(1,0,200)
    cobot.CalibrationL(0,0,200)
    cobot.CalibrationL(1,1,200)

    cobot.CalibrationL(2,0,200)

    cobot.CalibrationL(0,1,200)
    cobot.CalibrationL(1,0,200)
    cobot.CalibrationL(0,0,200)
    cobot.CalibrationL(2,1,200)

    cobot.CalibrationL(1,1,200)
    i += 1
#---------------------CALIBRAÇÂO----------------#