  // The following reads 20 into t and 999999995 into a and b.
  t, a, b = readline_int_list()
  // The judge secretly picks R = 999999995 (it had no choice) and X = -1,
  // Y = 3 (it did have a choice here). (Note: the actual Test Set 1 will
  // not necessarily use the values in this example.)
  // We try to throw at the upper left corner of the wall, and the dartboard
  // does not overlap with that point.
  printline -1000000000 1000000000 to stdout
  flush stdout
  r = readline_string()  // reads MISS.
  // We try to throw at the center of the wall. That does hit the dartboard,
  // but not the center.
  printline 0 0 to stdout
  flush stdout
  r = readline_string()  // reads HIT.
  // We make a super lucky choice and throw at the center of the dartboard.
  printline -1 3 to stdout
  flush stdout
  r = readline_string()  // reads CENTER.
  // The judge begins the next test case. It secretly picks R = 999999995
  // and X = 5, Y = 5.
  // We accidentally throw a dart out of the allowed range.
  printline -1234567890 1234567890 to stdout
  flush stdout
  r = readline_string()  // reads WRONG.
  exit  // exits to avoid an ambiguous TLE error.