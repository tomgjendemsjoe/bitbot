bitbot.select_model(BBModel.XL)
bitbot.goms(BBDirection.Forward, 21, 5000)
bitbot.setLedColor(0xFF0000)
basic.pause(3000)
bitbot.rotatems(BBRobotDirection.Right, 20, 800)
bitbot.goms(BBDirection.Forward, 21, 5000)
bitbot.ledClear()
basic.pause(3000)
bitbot.rotatems(BBRobotDirection.Right, 20, 800)
bitbot.goms(BBDirection.Forward, 21, 5000)
bitbot.setLedColor(0x40C0FF)
basic.pause(3000)
bitbot.rotatems(BBRobotDirection.Right, 20, 800)
bitbot.goms(BBDirection.Forward, 21, 5000)
bitbot.ledClear()
basic.forever(function () {
	
})
