fun main() {

    val matrix = Array(100) { IntArray(100) {0} }

    val n = readLine()!!.toInt()

    var sum = 0

    repeat(n) {
        val (x, y) = readLine()!!.split(" ").map { it.toInt() }

        for (i in x until x+10) {
            for (j in y until y+10) {
                if (matrix[j][i] == 0) {
                    matrix[j][i] += 1
                    sum += 1
                }
            }
        }
    }
    println(sum)
}
