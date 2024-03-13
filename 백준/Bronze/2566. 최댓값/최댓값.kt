fun main() {

    var maxNumber = 0
    var rowIdx = 0
    var columnIdx = 0

    for (i in 0..8) {
        val line = readLine()!!.split(" ").map { it.toInt() }
        for ((idx,n) in line.withIndex()) {
            if (n > maxNumber) {
                rowIdx = i
                columnIdx = idx
                maxNumber = n
            }
        }
    }

    println(maxNumber)
    println("${rowIdx+1} ${columnIdx+1}")

}