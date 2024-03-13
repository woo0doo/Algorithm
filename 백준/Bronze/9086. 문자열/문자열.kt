fun main() {

    val a = readLine()!!.toInt()

    repeat(a) {
        val b = readLine()!!
        println("${b.first()}${b.last()}")
    }
}
