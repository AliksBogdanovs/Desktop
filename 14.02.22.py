
def csv_1_2(pirmaiscsv, traiscsv):
    with open(pirmaiscsv, 'r' ,encoding="utf-8") as fails:
     lasti_csv = csv.reader(fails)
    saturs = []
    for rinda in lasit_csv:
        saturs.append(rinda)
with open(otraisCSV, 'r',encoding="utf-8") as fails:
    lasit_csv = csv.reader(fails)
    saturs_otrajam = []
    for rinda in lasit_csv:
        saturs_otrajam.appened(rinda)

if len(saturs) == len(saturs_otrajam):
    with open('divikopa.csv', 'w',encoding="utf-8",newline='')as fails:
        csvwrite = csv.writer(fails)
        csvwrite.writerows(saturs)
        csvwrite.writerows(saturs_otrajam)


