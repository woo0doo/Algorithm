fun main() {

    var sum = 0.0
    var total = 0.0

    repeat(20) {
        val grade = readLine()!!.split(" ")
        val credit = grade[1].toDouble()

        total += credit

        when (grade[2]) {
            "A+" -> sum += (credit * 4.5)
            "A0" -> sum += (credit * 4.0)
            "B+" -> sum += (credit * 3.5)
            "B0" -> sum += (credit * 3.0)
            "C+" -> sum += (credit * 2.5)
            "C0" -> sum += (credit * 2.0)
            "D+" -> sum += (credit * 1.5)
            "D0" -> sum += (credit * 1.0)
            "F" -> sum += (credit * 0.0)
            "P" -> total -= grade[1].toFloat()
        }

    }

    println(sum / total)
}
