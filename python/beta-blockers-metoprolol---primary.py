# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"34092","system":"gprdproduct"},{"code":"34509","system":"gprdproduct"},{"code":"34125","system":"gprdproduct"},{"code":"34890","system":"gprdproduct"},{"code":"40167","system":"gprdproduct"},{"code":"34430","system":"gprdproduct"},{"code":"34584","system":"gprdproduct"},{"code":"34094","system":"gprdproduct"},{"code":"34925","system":"gprdproduct"},{"code":"753","system":"gprdproduct"},{"code":"32836","system":"gprdproduct"},{"code":"739","system":"gprdproduct"},{"code":"34407","system":"gprdproduct"},{"code":"34854","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('beta-blockers-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["beta-blockers-metoprolol---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["beta-blockers-metoprolol---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["beta-blockers-metoprolol---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
