fun main() {
    val (a, b) = readLine()!!.split(" ")

    val aReverse = a.reversed().toInt()
    val bReverse = b.reversed().toInt()

    if (aReverse > bReverse) {
        println(aReverse)
    } else {
        println(bReverse)
    }
}
