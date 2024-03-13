fun main() {

    val nums = readLine()!!.split(" ").map { it.toInt() }
    
    val a = nums[0]
    val b = nums[1]
    if (a<b) print("<")
    else if (a>b) print(">")
    else print("==")
    
}