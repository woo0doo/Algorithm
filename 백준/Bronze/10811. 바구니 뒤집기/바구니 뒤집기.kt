fun main() {

    val (n, m) = readLine()!!.split(" ").map { it.toInt() }

    var buckets = IntArray(n) { it + 1 }

    repeat(m) {
        val (i, j) = readLine()!!.split(" ").map { it.toInt() }
        buckets.reverse(i-1, j)
    }

    println(buckets.joinToString(" "))

}
