fun main() {

    val n = readln().toInt()
    val map = readln().split(" ").map { it.toInt() }.toMutableSet()

    val m = readln().toInt()
    val map2 = readln().split(" ").map { it.toInt() }

    for (card in map2) {
        if (card in map) {
            print("1 ")
        } else {
            print("0 ")
        }
    }
}
