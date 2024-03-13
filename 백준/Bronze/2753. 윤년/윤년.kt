fun main() {

    val yearNum = readLine()!!.toInt()

    if (yearNum % 400 == 0) {
        println(1)
    } else if (yearNum % 4 == 0 && yearNum % 100 != 0) {
        println(1)
    } else {
        println(0)
    }

}