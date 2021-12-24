class FizzBuzz {
  private int n;
  private int currentNum;

  public FizzBuzz(int n) {
    this.n = n;
    this.currentNum = 1;
  }

  private char derive(int x) {
    if (x % 3 == 0 && x % 5 == 0) return 'z';
    else if (x % 3 == 0) return 'f';
    else if (x % 5 == 0) return 'b';
    else return 'i';
  }

  private void work(char selector, Runnable runnable, IntConsumer intConsumer)
      throws InterruptedException {
    while (currentNum <= n) {
      synchronized (this) {
        if (derive(currentNum) == selector) {
          if (runnable != null) runnable.run();
          else intConsumer.accept(currentNum);
          currentNum++;
          notifyAll();
        } else wait();
      }
    }
  }

  // printFizz.run() outputs "fizz".
  public void fizz(Runnable printFizz) throws InterruptedException {
    work('f', printFizz, null);
  }

  // printBuzz.run() outputs "buzz".
  public void buzz(Runnable printBuzz) throws InterruptedException {
    work('b', printBuzz, null);
  }

  // printFizzBuzz.run() outputs "fizzbuzz".
  public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
    work('z', printFizzBuzz, null);
  }

  // printNumber.accept(x) outputs "x", where x is an integer.
  public void number(IntConsumer printNumber) throws InterruptedException {
    work('i', null, printNumber);
  }
}
