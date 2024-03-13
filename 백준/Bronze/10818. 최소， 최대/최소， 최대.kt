fun main() {

    val list = readLine()!!.split(" ").map { it.toInt() }
    val nums = readLine()!!.split(" ").map { it.toInt() }

    println("${nums.minOrNull()} ${nums.maxOrNull()}")
}
