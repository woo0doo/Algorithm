fun main() {

    val nAndM = readLine()!!.split(" ").map { it.toInt() }

    var buckets = IntArray(nAndM[0]) { it + 1 }

    repeat(nAndM[1]) {
        val changeBallNumber = readLine()!!.split(" ").map { it.toInt() }

        val temp = buckets[changeBallNumber[0] - 1]
        buckets[changeBallNumber[0] - 1] = buckets[changeBallNumber[1] - 1]
        buckets[changeBallNumber[1] - 1] = temp

    }

    println(buckets.joinToString(" "))
}