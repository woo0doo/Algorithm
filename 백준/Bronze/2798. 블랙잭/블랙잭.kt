fun main() {
    val (n, m) = readLine()!!.split(" ").map { it.toInt() }

    val cards = readLine()!!.split(" ").map { it.toInt() }

    val sortCard = cards.sorted()

    var answer = 0

    for (i in 0 until n) {
        for (j in (i + 1) until n) {
            for (k in (j + 1) until n) {
                val sum = sortCard[i] + sortCard[j] + sortCard[k]
                if (sum > m) {
                    break
                } else if (sum > answer) {
                    answer = sum
                }
            }
        }
    }

    println(answer)
}
