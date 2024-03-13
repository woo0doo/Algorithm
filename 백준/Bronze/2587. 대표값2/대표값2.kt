fun main() {

    val scores = IntArray(5) {0}

    for (i in 0 until 5) {
        val score = readLine()!!.toInt()
        scores[i] = score
    }

    scores.sort()

    println(scores.sum() / 5)
    println(scores[2])

}
