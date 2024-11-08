import pygatt

adapter = pygatt.GATTToolBackend()

try:
    adapter.start()
    device = adapter.connect('Makeblock_LE703e97eb4c2e')
    value = device.char_read("067D70D7-B533-BBBC-E888-1C810094B77E")
    print(vale)
finally:
    adapter.stop()
