fun main() {

    val n = readLine()!!.toInt()
    val nums = readLine()!!.split(" ").map { it.toInt() }
    val findNum = readLine()!!.toInt()

    println(nums.count { it == findNum })

}