angle = 135

def on_button_a():
    global angle
        angle = min(255, angle + 30)
            wuKong.set_servo_angle(wuKong.ServoTypeList._270, wuKong.ServoList.S0, angle)
                basic.show_number(angle)
                input.on_button_pressed(Button.A, on_button_a)
                
                def on_button_b():
                    global angle
                        angle = max(15, angle - 30)
                            wuKong.set_servo_angle(wuKong.ServoTypeList._270, wuKong.ServoList.S0, angle)
                                basic.show_number(angle)
                                input.on_button_pressed(Button.B, on_button_b)
                                
                                wuKong.set_servo_angle(wuKong.ServoTypeList._270, wuKong.ServoList.S0, angle)                                                            sleep(50)