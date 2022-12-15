
def count_batteries_by_usage(cycles):
  c=input()
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }
  if(c<310):
    return lowCount
  elif(c>310 and c<929):
    return mediumCount
  else:
    return highCount


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
