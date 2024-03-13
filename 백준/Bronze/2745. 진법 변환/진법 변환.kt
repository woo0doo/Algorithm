fun main() {

    val split = readLine()!!.split(" ")

    val num = split[0]
    val base = split[1].toInt()

    println(num.toLong(base))
}
