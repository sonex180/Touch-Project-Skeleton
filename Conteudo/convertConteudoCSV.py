import csv
import sys

with open("Animal_test.csv", "w") as outputFilePtr:
  with open("Animais_Diorama.csv", encoding="utf-8") as filePtr:
    reader = csv.reader(filePtr, delimiter=';', quotechar='"')
    writer = csv.writer(outputFilePtr, delimiter='|', quotechar='"', lineterminator="|", quoting=csv.QUOTE_MINIMAL)

    for row in reader:
      for index, cel in enumerate(row):
        firstChar = cel[:1]
        if firstChar == '\n' or firstChar == '\r':
          row[index] = cel[1:]

        lastChar = cel[len(cel) - 1:]
        if lastChar == '\n' or lastChar == '\r':
          row[index] = cel[:len(cel) - 1]

      writer.writerow(row)

