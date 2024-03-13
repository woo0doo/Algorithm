fun main() {

    val (n, m) = readLine()!!.split(" ").map { it.toInt() }
    val matrixA = Array(n) { IntArray(m) }

    for (i in 0 until n) {
        val temp = readLine()!!.split(" ")
        for (j in 0 until m) {
            matrixA[i][j] = temp[j].toInt()
        }
    }

    val matrixB = Array(n) { IntArray(m) }

    for (i in 0 until n) {
        val temp = readLine()!!.split(" ")
        for (j in 0 until m) {
            matrixB[i][j] = temp[j].toInt()
        }
    }

    for (i in 0 until n) {
        for (j in 0 until m) {
            print("${matrixA[i][j] + matrixB[i][j]} ")
        }
        println()
    }

}
