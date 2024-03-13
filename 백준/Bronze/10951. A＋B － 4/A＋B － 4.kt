fun main() {

    repeat(5) {

        while (true) {
            val nums = readLine()?.split(" ") ?: break
            println(nums[0].toInt() + nums[1].toInt())
        }
    }
}