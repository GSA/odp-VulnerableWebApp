import json
import sys

fileName = "./output.json"

#fileName = "/Users/Prayas/Desktop/WorkSpace/output.json"

def getResult():
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

    critVuln = sev["CRITICAL"]
    critThreshold = 10
    if critVuln > critThreshold:
        print("Scan failed because the app still has " + critVuln + " CRITICAL vulnerabilities\nThe amount of CRITICAL vulnerabilities allowed is: " + critThreshold"
        sys.exit(1)
    else:
        sys.exit(0)


getResult()
