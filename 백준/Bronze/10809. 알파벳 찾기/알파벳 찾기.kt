fun main() {

    val word = readLine()!!

    val arr = IntArray(26) {-1}

    for ((index, c) in word.withIndex()) {
        if (arr[c.code-97] == -1) {
            arr[c.code-97] = index
        }
    }
    println(arr.joinToString(" "))
}
