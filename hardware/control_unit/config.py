UART_BAUD = 921600
UART_BYTESIZE = 8
UART_PARITY = 'N'
UART_STOP = 1
UART_TIMEOUT = None
UART_CHANNELS = ['/dev/ttyAMA1', 
                 '/dev/ttyAMA2']

CMD_SIZE = 12
REPLY_SIZE = 32

REPLY_FORMAT = '<BIhhihhihhhhBB'
CMD_FORMAT = '<BBhhhhh'


# SCALES 
LINEAR_ENCODER_SCALE = 1
MOTOR_ENCODER_SCALE = 1
MOTOR_SPEED_SCALE = 1
MOTOR_TORQUE_SCALE = (1, 1, 1, 1)
LOAD_CELL_SCALE = (1, 1, 1, 1)