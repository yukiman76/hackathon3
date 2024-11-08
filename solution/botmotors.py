import serial
from time import sleep

# we are the actions of the robot we move it as needed
# and can move the arm


class mbActions:

    def __init__(self):
        # self.ser = serial.Serial('/dev/tty.usbserial-1140', 115200, timeout=1)
        self.ser = serial.Serial('/dev/tty.wchusbserial2110', 115200, timeout=1)
        self.curr_pos = 0
        self.last_distance = 0
        self.start_distance = 24
        self.total_field = 213
        self.bars = {
                      1: {"height" : 22, "distance": 22},
                      2: {"height" : 42, "distance": 52},
                      3: {"height" : 52, "distance": 47}
                     }

    def send_cmd(self, sCommand):
        self.ser.flushInput()
        print("Sending : {}".format(sCommand))
        self.ser.write("{}\n".format(sCommand).encode())
        self.ser.flushInput()
        print("mbActions - {}".format(self.ser.readline()) )

    def movefwd(self, idistance):
        self.send_cmd("f{}".format(idistance))

    def movebkw(self, idistance):
        self.send_cmd("b{}".format(idistance))

    def touch(self):
        self.send_cmd("a80") # move arm up to touch
        sleep(1)
        self.send_cmd("a0") # bring it back down

    def lift(self):
        self.send_cmd("a100") # try to lift
        sleep(1)
        self.send_cmd("a0") # bring it back down

    def moveto(self, iBar):
        # from closes to furthest we have to move to a given bar
        # from our current position what do we have to do to move
        # if we are grater than the field size total_field we need to move backwards
        if self.curr_pos  == 0:
            # simple case we are starting move foward
            self.movefwd(self.bars[iBar]["distance"])
            self.curr_pos = self.bars[iBar]["distance"]

        elif self.curr_pos + self.bars[iBar]["distance"] > self.total_field:
            # we are moving backwards,
            i = self.bars[iBar]["distance"] -  self.bars[iBar - 1]["distance"]
            self.movebkw(i)
            self.curr_pos = i
        else:
            # we are on the field and have a pos > 0
            # we need to move to new locataion which is infrount of us
            i = self.bars[iBar]["distance"] -  self.curr_pos
            self.movefwd(i)
            self.curr_pos = i

if __name__ == '__main__':
    print("testing")
    a = mbActions()
    a.movefwd(2000)
    a.movebkw(2000)
    a.lift()
