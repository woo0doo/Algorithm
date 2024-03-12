fun main() {

    var age = readLine()!!.toList()
    for (i in age.sortedDescending()) {
        print(i)
    }
}