import kotlin.text.StringBuilder

fun main() = with(System.`in`.bufferedReader()) {

    val n = readLine().toInt()
    val bw = System.out.bufferedWriter()
    val sb = StringBuilder()

    var deque = ArrayDeque<Int>()

    repeat(n) {
        val arr = readLine().split(" ").map { it.toInt() }
        when (arr.first()) {
            1 -> deque.addFirst(arr.last())
            2 -> deque.addLast(arr.last())
            3 -> sb.append(if (deque.isEmpty()) "-1\n" else "${deque.removeFirst()}\n")
            4 -> sb.append(if (deque.isEmpty()) "-1\n" else "${deque.removeLast()}\n")
            5 -> sb.append("${deque.count()}\n")
            6 -> sb.append(if (deque.isEmpty()) "1\n" else "0\n")
            7 -> sb.append(if (deque.isEmpty()) "-1\n" else "${deque.first()}\n")
            8 -> sb.append(if (deque.isEmpty()) "-1\n" else "${deque.last()}\n")
        }
    }

    bw.write(sb.toString())
    bw.close()
}
