fun main() {

    val (n, k) = readLine()!!.split(" ").map { it.toInt() }
    val scores = readLine()!!.split(" ").map { it.toInt() }

    val sortedScore = scores.sorted()

    println(sortedScore[n-k])
}
