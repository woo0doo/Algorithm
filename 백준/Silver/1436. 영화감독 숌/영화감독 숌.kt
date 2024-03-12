fun main() {

    var num = readLine()!!.toInt()
    var title_num = 665
    while (num > 0) {
        title_num++
        if (title_num.toString().contains("666")) {
            num--
        }
    }

    println(title_num)
}