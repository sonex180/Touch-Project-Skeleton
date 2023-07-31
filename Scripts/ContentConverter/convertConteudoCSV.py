import csv
import sys

with open("conteudoFinal.csv", "w") as outputFilePtr:
  with open("Conteudos Paracatu.csv") as filePtr:
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

