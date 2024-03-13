fun main() {

    val t = readLine()!!.toInt()

    repeat(t) {
        val (strLength, word) = readLine()!!.split(" ")

        val length = strLength.toInt()
        for (c in word) {
            for (i in 1..length) {
                print("${c}")
            }
        }
        println()
    }
}
