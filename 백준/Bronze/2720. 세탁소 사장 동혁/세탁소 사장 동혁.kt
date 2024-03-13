fun main() {

    val n = readLine()!!.toInt()
    repeat(n) {
        var moneys = IntArray(4) { 0 }
        var totalMoney = readLine()!!.toInt()
        moneys[0] = totalMoney/25
        totalMoney%=25

        moneys[1] = totalMoney/10
        totalMoney%=10

        moneys[2] = totalMoney/5
        totalMoney%=5

        moneys[3] =totalMoney/1
        println(moneys.joinToString(" "))
    }
}
