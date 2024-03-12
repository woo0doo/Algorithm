fun main() {

    var (hour, minute) = readLine()!!.split(" ").map(String::toInt)
    minute += readLine()!!.toInt()
    println("${(hour + minute / 60) % 24} ${minute % 60}")
}