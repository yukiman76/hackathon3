# https://github.com/Makeblock-official/Makeblock-Libraries/blob/master/examples/Firmware_For_mBlock/mbot_firmware/mbot_firmware.ino
# https://github.com/Makeblock-official/Makeblock-Libraries/issues/27
# https://arduino.stackexchange.com/questions/72773/mcorearduino-python-bluetooth-communication
# https://github.com/Atonbom/KimPyRaptor
# https://www.vernier.com/til/4140
import asyncio


from bleak import BleakScanner, BleakClient

name_or_address = "Makeblock_LE703e97eb4c2e"
# UART_SERVICE_UUID = '067D70D7-B533-BBBC-E888-1C810094B77E'
device = await BleakScanner.find_device_by_name(name_or_address)
MY_CHAR_UUID = "1234"

if device is None:
    print("%s not found", name_or_address)
    exit(-1)
else:
    client = BleakClient(device)
    # nus = client.services.get_service(UART_SERVICE_UUID)
    # rx_char = nus.get_characteristic(UART_RX_CHAR_UUID)
    await client.write_gatt_char("FFE1", b"001", response=False)
