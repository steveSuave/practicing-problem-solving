/*
 * You are given the following information, but you may prefer to do some research for yourself.
 *
 *  1 Jan 1900 was a Monday.
 *  Thirty days has September,
 *  April, June and November.
 *  All the rest have thirty-one,
 *  Saving February alone,
 *  Which has twenty-eight, rain or shine.
 *  And on leap years, twenty-nine.
 *  A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
 *
 * How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
 */

class DDate {

  private int year;
  private int month;
  private int day;
  private int monthDays[] = {0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

  public static void main(String[] args) {
    int count = 0;
    DDate sunday = new DDate(1901, 1, 6);
    while (sunday.getYear() <= 2000) {
      sunday.addDays(7);
      if (sunday.getDay() == 1) count++;
    }
    System.out.println(count);
  }

  public DDate(int year, int month, int day) {
    int february = isLeapYear(year) ? 29 : 28;
    this.monthDays[2] = february;
    this.year = year;
    this.month = month;
    this.day = day;
  }

  public int getYear() {
    return year;
  }

  public void setYear(int year) {
    this.year = year;
    if (isLeapYear(year)) {
      this.getMonthDays()[2] = 29;
    } else {
      this.getMonthDays()[2] = 28;
    }
  }

  public int getMonth() {
    return month;
  }

  public void setMonth(int month) {
    this.month = month;
  }

  public int getDay() {
    return day;
  }

  public void setDay(int day) {
    this.day = day;
  }

  public int[] getMonthDays() {
    return monthDays;
  }

  public void setMonthDays(int[] monthDays) {
    this.monthDays = monthDays;
  }

  public boolean isLeapYear(int year) {
    return year % 4 == 0 && year % 100 != 0 || year % 400 == 0;
  }

  public void addDays(int num) {
    for (int i = 1; i <= num; i++) {
      this.setDay(this.getDay() + 1);
      // if day got bigger than current month's capacity
      if (this.getDay() > this.getMonthDays()[this.getMonth()]) {
        this.setDay(1);
        this.setMonth(this.getMonth() + 1);
      }
      if (this.getMonth() > 12) {
        this.setMonth(1);
        this.setYear(this.getYear() + 1);
      }
    }
  }
}
