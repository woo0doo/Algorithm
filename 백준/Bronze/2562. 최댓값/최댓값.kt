fun main() {

    var maxNum = 0
    var index = 0

    for (i in 1..9) {
        val num = readLine()!!.toInt()
        if (num > maxNum) {
            maxNum = num
            index = i
        }
    }
    println(maxNum)
    println(index)
}