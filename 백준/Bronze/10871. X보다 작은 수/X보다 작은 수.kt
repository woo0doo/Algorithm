fun main() {

    val list = readLine()!!.split(" ").map { it.toInt() }
    val nums = readLine()!!.split(" ").map { it.toInt() }

    val filterNum = nums.filter { it < list[1] }

    for (i in filterNum) {
        print("$i ")
    }
}