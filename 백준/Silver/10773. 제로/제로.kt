import java.util.Stack

fun main() {

    val n = readLine()!!.toInt()
    val stack = Stack<Int>()
    repeat(n) {
        val k = readLine()!!.toInt()
        if (k != 0) stack.add(k)
        else stack.pop()
    }

    println(stack.sum())
}