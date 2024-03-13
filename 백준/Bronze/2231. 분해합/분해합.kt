fun main() {

    var flag = false
    val n = readLine()!!.toInt()

    for (i in 1..n) {
        val stringNumber = i.toString()
        var sum = i
        for (c in stringNumber) {
            val digitToInt = c.digitToInt()
            sum += digitToInt
        }
        if (sum == n) {
            println(i)
            flag = true
            break
        }
    }

    if (!flag) {
        println(0)
    }
}