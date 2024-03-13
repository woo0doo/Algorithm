fun main() {

    val n = readLine()!!.toInt()
    val nums = readLine()!!.split(" ").map { it.toInt() }

    var max = nums.maxOrNull()

    val sum = nums.sumOf { (it.toDouble() / max!!.toDouble()) * 100 }
    print(sum/nums.size)
}
