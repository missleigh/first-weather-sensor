def on_button_pressed_b():
    global item
    item += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

item = 0
weatherbit.start_weather_monitoring()

def on_forever():
    global item
    if item == 0:
        basic.show_string("Temp C: ")
        basic.show_number(Math.idiv(weatherbit.temperature(), 100))
    elif item == 1:
        basic.show_string("Humidity %: ")
        basic.show_number(Math.idiv(weatherbit.humidity(), 1024))
    elif item == 2:
        basic.show_string("Pressure hPa: ")
        basic.show_number(Math.idiv(weatherbit.pressure(), 25600))
    else:
        item = 0
basic.forever(on_forever)

def on_button_pressed_a():
    basic.show_number(input.temperature() * (9 / 5) + 32)
    basic.show_string("F")
input.on_button_pressed(Button.A, on_button_pressed_a)
