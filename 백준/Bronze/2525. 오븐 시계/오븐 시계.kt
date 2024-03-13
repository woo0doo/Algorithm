fun main() {

    val time = readLine()!!.split(" ").map { it.toInt() }
    val plusTime = readLine()!!.toInt()

    var hour = time[0]
    var minute = time[1]

    val plusMinute = minute + plusTime
    hour = (hour + (plusMinute / 60)) % 24
    println("${hour} ${plusMinute % 60}")

}