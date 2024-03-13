fun main() {

    val toCharArray = readLine()!!.toCharArray()

    val arrCount = IntArray(26) {0}

    val upperCharArray = toCharArray.map { it.uppercase() }

    for (c in upperCharArray) {
        arrCount[c[0].code - 65] += 1
    }

    val maxOrNull = arrCount.maxOrNull()
    if (arrCount.count { it == maxOrNull } > 1) {
        print("?")
    } else {
        for ((i, v) in arrCount.withIndex()) {
            if (v == maxOrNull) {
                println((i+65).toChar())
            }
        }
    }
}