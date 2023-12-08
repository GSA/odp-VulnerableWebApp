import json
fileName = "./output.json"

#fileName = "/Users/Prayas/Documents/WorkSpace/odp-VulnerableWebApp/result.json"

f = open(fileName)
data = json.load(f)
vuln = 0
sca = 0
sev = {}
lan = {}
for i in data["analysisVulnerabilities"]:
    vulnerabliliy = i["vulnerabilities"]
    
    severity = vulnerabliliy ["severity"]
    if severity in sev:
        sev[severity] += 1
    else:
        sev[severity] = 1

    language = vulnerabliliy ["language"]
    if language in lan:
        lan[language] += 1
    else:
        lan[language] = 1

print (str(sev))
print(lan)
