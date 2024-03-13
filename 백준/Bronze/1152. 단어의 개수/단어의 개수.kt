fun main() {

    val words = readLine()!!.split(" ")
    println(words.filter { it.isNotBlank() }.size)
}
