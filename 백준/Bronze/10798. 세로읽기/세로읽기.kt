fun main() {

    val matrix = Array(5) { CharArray(15) { '#' } }
    var max = 0
    for (i in 0..4) {

        val line = readLine()!!
        max = maxOf(max, line.length)
        for ((idx, c) in line.withIndex()) {
            matrix[i][idx] = c
        }
    }

    var ans = ""
    for (i in 0 until max) {
        for (j in 0 until 5) {
            if (matrix[j][i] != '#')
                ans += matrix[j][i]
        }
    }
    println(ans)
}