import serial
import struct
from time import ctime, sleep

"""
Binary protocol decode (HEX)

header
ff 55
0  1

command body
len idx action device port slot data a
2   3   4      5      6    7    8

"""

# Function to convert a short integer to a two-byte array
def short2bytes(sval):
    val = struct.pack("h", sval)  # Pack short integer as bytes
    print(val)
    return [val[0], val[1]]  # Return as a list of two bytes

# Function to stop the motors by sending a specific byte sequence to the serial device
def stop_motors(ser):
    print("motor stopping")
    # Write a stop command to the serial device
    ser.write(bytearray([0xff, 0x55, 0x07, 0x00, 0x02, 0x05, 0x00, 0x00, 0x00, 0x00]))
    print(ser.readline())  # Read and print the response from the device

# Open the serial connection
with serial.Serial('/dev/tty.wchusbserial21110', 115200, timeout=1) as ser:
    ser.flushInput()  # Flush any existing input in the serial buffer

    # Example: Uncommented code below demonstrates serial write commands
    # head = b'\xff\x55'
    # ser.write(head + b'\x06\x00\x02\x22\x09\x00\x00\x0a\r')  # Send a command as byte sequence
    # line = ser.readline()  # Read a line terminated by '\n'
    # print(line)
    # ser.write(head + b'\x04\x03\x01\x01\x01\x0a')  # Another command as byte sequence
    # line = ser.readline()  # Read response line
    # print(ser.readline())  # Print the response from the device

    # Example: Forward motor at 100 speed
    # print("motor run")
    # print(short2bytes(100))  # Convert integer 100 to byte format and print

    # Example: Wide circle using joystick command (0x05)
    # ser.write(bytearray([0xff, 0x55, 0x07, 0x00, 0x02, 0x05] + [0x0d, 0x00] + [0x0d, 0x0d]))
    # ser.write(bytearray([0xff, 0x55, 0x07, 0x00, 0x02, 0x05] + [0x9c, 0x00] + [0x00, 0x00]))

    # Command body format
    # len idx action device port slot data a
    # 2   3   4      5      6    7    8

    # Command to move the servo to a position
    print('run Servo')
    ser.write(bytearray([0xff, 0x55, 0x07, 0x00, 0x02, 0xB] + [0x01] + [0x01] + [0xB4]))
    print(ser.readline())  # Print the device response
    ser.write(bytearray([0xff, 0x55, 0x07, 0x00, 0x02, 0xB] + [0x01] + [0x01] + [0x00]))
    print(ser.readline())  # Print the device response

    sleep(5)  # Wait for 5 seconds

    # Stop the motors after the servo operation
    stop_motors(ser)

    ser.close()  # Close the serial connection
    # IPython interactive session (uncomment if needed for debugging)
    # import IPython
    # IPython.embed()
