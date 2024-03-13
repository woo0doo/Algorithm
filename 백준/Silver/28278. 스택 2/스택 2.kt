import java.lang.StringBuilder
import java.util.Stack

fun main() = with(System.`in`.bufferedReader()) {

    val bw = System.out.bufferedWriter()
    val sb = StringBuilder()

    val n = readLine().toInt()
    val stack = Stack<Int>()

    repeat(n) {

        val split = readLine().split(" ")

        when (split[0]) {
            "1" -> stack.add(split[1].toInt())
            "2" -> sb.append(if(stack.empty()) "${-1}\n" else "${stack.pop()}\n")
            "3" -> sb.append("${stack.size}\n")
            "4" -> sb.append(if(stack.empty()) "${1}\n" else "${0}\n")
            "5" -> sb.append(if(stack.empty()) "${-1}\n" else "${stack.peek()}\n")
        }
    }
    bw.write(sb.toString())
    bw.close()
}