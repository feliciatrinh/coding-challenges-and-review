/*
Input: year1, month1, day1, year2, month2, day2
Output: integer representing the number of days in between two dates

Second date is always later than the first date.
*/

int DaysInMonth(int month, int year);
// Do not edit above this line. It is only shown so you can see the function signature.

/*
 * Complete the function below.
 */
int DaysBetween(int year1, int month1, int day1, int year2, int month2, int day2) {
    // Take into account leap years by exclusively using DaysInMonth
    int totalDays = 0;
    // Go forward in the calendar until the years and months match.
    while ((year2 > year1) || (month1 != month2)) {
        totalDays += DaysInMonth(month1, year1);
        if (month1 == 12) {
            year1 += 1;
            month1 = 1;
        } else {
            month1 += 1;
        }
    }
    // Take into account overcounting.
    if (day1 > 1) {
        totalDays -= (day1 - 1);
    }
    // account for the days in between the 1st and day2
    totalDays += (day2 - 1); 
    return totalDays;
}
