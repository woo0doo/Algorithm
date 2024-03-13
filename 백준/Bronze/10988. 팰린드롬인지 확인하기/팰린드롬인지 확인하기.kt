fun main() {

    val word = readLine()!!
    val reversedWord = word.reversed()

    if (word == reversedWord) {
        println(1)
    } else {
        println(0)
    }
}
