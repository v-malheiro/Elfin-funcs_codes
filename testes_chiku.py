import elfin

server_ip = '169.254.153.251'
port_number = 10003
message_size = 1024
robot_id = 0

cobot = elfin.Elfin()
cobot.connect(server_ip, port_number, message_size, robot_id)

target = cobot.ReadPcsActualPos()
cobot.MoveL(target)

status = cobot.ReadMoveState()

i = 0
while i < 1:
    cobot.CalibrationL(1,1,20)
    cobot.CalibrationL(0,1,180)
    cobot.CalibrationL(1,0,40)
    cobot.CalibrationL(0,0,180)
    cobot.CalibrationL(1,1,20)

    cobot.CalibrationL(2,0,40)

    cobot.CalibrationL(1,1,20)
    cobot.CalibrationL(0,1,180)
    cobot.CalibrationL(1,0,40)
    cobot.CalibrationL(0,0,180)
    cobot.CalibrationL(1,1,20)

    cobot.CalibrationL(2,1,40)

    i += 1
