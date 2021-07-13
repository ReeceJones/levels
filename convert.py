import subprocess
import json
import csv

RESOURCE_LOCATION = 'https://www.levels.fyi/js/salaryData.json'

def main():
    # download dataz
    dl = subprocess.call(f'wget --compression=gzip {RESOURCE_LOCATION}', shell=True)

    if dl != 0:
        print('ERROR: could not download salaryData.json, aborting')
        return 1

    unique_schemas = set()
    print('starting conversion')
    with open('salaryData.json', 'r') as f:
        salary_data = json.load(f)
        with open('salaryData.csv', 'w') as c:
            writer = csv.writer(c, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([
                'timestamp', 'company', 'level', 'title',
                'totalyearlycompensation', 'location', 'yearsofexperience',
                'yearsatcompany', 'tag', 'basesalary', 'stockgrantvalue',
                'bonus', 'gender', 'otherdetails', 'cityid', 'dmaid', 'rowNumber'
            ])
            for row in salary_data:
                schema = row.keys()
                unique_schemas.add(str(list(schema)))
                writer.writerow([
                    row['timestamp'],
                    row['company'],
                    row['level'],
                    row['title'],
                    row['totalyearlycompensation'],
                    row['location'],
                    row['yearsofexperience'],
                    row['yearsatcompany'],
                    row['tag'],
                    row['basesalary'],
                    row['stockgrantvalue'],
                    row['bonus'],
                    row['gender'],
                    row['otherdetails'],
                    row['cityid'],
                    row['dmaid'],
                    row['rowNumber']
                ])

    print('unique schemas:', len(unique_schemas))


if __name__=='__main__':
    main()
