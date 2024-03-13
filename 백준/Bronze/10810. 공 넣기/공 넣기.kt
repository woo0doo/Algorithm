fun main() {

    val nAndM = readLine()!!.split(" ").map { it.toInt() }

    val array = Array(nAndM[0], {0})

    repeat(nAndM[1]) {
        val split = readLine()!!.split(" ").map { it.toInt() }
        val x = split[0]
        val y = split[1]
        val z = split[2]

        for (item in x-1..y-1) {
            array[item] = z
        }
    }

    println(array.joinToString(" "))
}