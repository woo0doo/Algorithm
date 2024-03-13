fun main() {

    val arr = mutableListOf(1, 1, 2, 2, 2, 8)

    val chess = readLine()!!.split(" ").map { it.toInt() }

    for (i in 0 until arr.size) {
        arr[i] -= chess[i]
    }

    println(arr.joinToString(" "))
}