import myeyes
import botmotors
# I need to be able to detect the lines and move the robot to it
# once i am close to the bar i can engage the arm to lift up
# then disconnect and move to next bar

class hackathon2:

    def __init__(self):
        self.eyes = myeyes.myEyes()
        self.actions = botmotors.mbActions()

    def run(self, colors):
        # we have the colors we need to run by, lets ask our eyes to see what colors there are
        found_colors = self.eyes.find_bars()
        # we have something like this
        # {'B': 1, 'R': 2, 'G': 3}
        # now we need to get the given bar distance and tell actions to go there
        for step_color in colors.split(','):
            if step_color in found_colors:
                # yaa we found the color we are looking for
                self.actions.moveto(found_colors[step_color])
                # we should be at the bar now lets touch it
                self.actions.touch()
                # self.actions.lift()

        # we will try to lift on the last bar
        self.actions.lift()



if __name__ == '__main__':
    s = """
        Enter Color Sequence (Red=R, Blue-B, Green=G)
         sepereated by commas \n
        Automions mode :
    """
    x = ""
    while x.split(',') < 3:
        print(s)
        x = input()
        if x.split(',') < 3:
            print('Error Need 3 colors')

    print('Running' + x)
    print("hit any key to start process")
    _ = input()
    h = hackathon2()
    h.run(x)
