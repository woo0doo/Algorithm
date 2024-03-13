fun main() {

    val n = readLine()!!.toInt()
    val stringNums = readLine()!!

    var sum = 0

    for (stringNum in stringNums) {
        val num = stringNum.digitToInt()
        sum += num
    }
    println(sum)
}
