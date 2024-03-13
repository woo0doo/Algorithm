import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder
import java.util.Stack

fun main() {

    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = System.out.bufferedWriter()
    val sb = StringBuilder()

    val n = br.readLine().toInt()
    val stack = Stack<Int>()

    repeat(n) {

        val split = br.readLine().split(" ")

        when (split[0]) {
            "1" -> stack.add(split[1].toInt())
            "2" -> {
                if (stack.empty()) {
                    sb.append("${-1}\n")
                } else {
                    sb.append("${stack.pop()}\n")
                }
            }
            "3" -> sb.append("${stack.size}\n")
            "4" -> {
                if (stack.empty()) {
                    sb.append("${1}\n")
                } else {
                    sb.append("${0}\n")
                }
            }
            "5" -> {
                if (stack.empty()) {
                    sb.append("${-1}\n")
                } else {
                    sb.append("${stack.peek()}\n")
                }
            }
        }
    }
    bw.write(sb.toString())
    bw.close()
    br.close()
}
