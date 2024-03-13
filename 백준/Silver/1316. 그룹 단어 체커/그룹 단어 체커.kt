fun main() {

    val n = readLine()!!.toInt()
    var cnt = 0

    repeat(n) {

        val intArray = IntArray(26) { 0 }
        var flag = true

        val word = readLine()!!
        for ((idx, c) in word.withIndex()) {
            val cIdx = c.code - 97
            if (idx != 0) {
                if (intArray[cIdx] != 0 && word[idx] != word[idx-1]) {
                    flag = false
                    break
                }
            }
            intArray[cIdx] += 1
        }
        if (flag) {
            cnt += 1
        }
    }
    print(cnt)
}
