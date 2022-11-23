import csv

def writeTXT(path, data):
    with open(path, 'w', encoding='utf-8') as writer:
        writer.write(data)
    return None

def readCSV(path):
    res = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            res.append(row)
    return res[1:]

def csv2dict(data):
    res = {}
    for row in data:
        idx = row[2].find('20')
        row.append(int(row[2][idx:idx+4]))
        if row[0] not in res:
            res[row[0]] = []
        res[row[0]].append(row[1:])
    return res

def paper_survey(data):
    body = '<ul>\n'
    for k,v in data.items():
        # print(v)
        v = sorted(v, key = lambda x: x[4])
        content = '<li>' + k + '\n\t<ul>\n'
        for p in v:
            paper = '\t<li>%s\n\t\t<ul>\n' %(p[1])
            if len(p[2]) != 0:
                paper += '\t\t<li>Paper: <a href="%s">%s</a></li>\n' %(p[2], p[2])
            if len(p[3]) != 0:
                paper += '\t\t<li>Code: <a href="GitHub">%s</a></li>\n' %(p[3])
            if len(p[0]) != 0:
                paper += '\t\t<li>Notes: %s</li>\n' %(p[0])
            paper += '\t\t</ul>\n\t</li>\n'
            content += paper
        content += '\t</ul>\n</li>\n\n'
        body += content
    body += '</ul>\n'
    return body

if __name__ == '__main__':
    data = readCSV('paper_survey.csv')
    data = csv2dict(data)
    body = paper_survey(data)
    writeTXT('paper_survey.txt', body)
    
    
    