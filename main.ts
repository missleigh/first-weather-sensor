input.onButtonPressed(Button.A, function () {
    item += 1
})
let item = 0
weatherbit.startWeatherMonitoring()
basic.forever(function () {
    if (item == 0) {
        basic.showString("Temp C: ")
        basic.showNumber(Math.idiv(weatherbit.temperature(), 100))
    } else if (item == 1) {
        basic.showString("Temp F:")
        basic.showNumber(input.temperature() * (9 / 5) + 32)
    } else if (item == 2) {
        basic.showString("Humidity %: ")
        basic.showNumber(Math.idiv(weatherbit.humidity(), 1024))
    } else if (item == 3) {
        basic.showString("Pressure hPa: ")
        basic.showNumber(Math.idiv(weatherbit.pressure(), 25600))
    } else {
        item = 0
    }
})
