bitbot.select_model(BBModel.XL)
bitbot.goms(BBDirection.FORWARD, 21, 5000)
bitbot.set_led_color(0xFF0000)
basic.pause(3000)
bitbot.rotatems(BBRobotDirection.RIGHT, 20, 800)
bitbot.goms(BBDirection.FORWARD, 21, 5000)
bitbot.led_clear()
basic.pause(3000)
bitbot.rotatems(BBRobotDirection.RIGHT, 20, 800)
bitbot.goms(BBDirection.FORWARD, 21, 5000)
bitbot.set_led_color(0x40C0FF)
basic.pause(3000)
bitbot.rotatems(BBRobotDirection.RIGHT, 20, 800)
bitbot.goms(BBDirection.FORWARD, 21, 5000)
bitbot.led_clear()

def on_forever():
    pass
basic.forever(on_forever)
