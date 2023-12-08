import json
import os
fileName = "./output.json"

#fileName = "/Users/Prayas/Documents/WorkSpace/odp-VulnerableWebApp/result.json"

print(os.path.abspath(fileName))

f = open(fileName)
data = json.load(f)
vuln = 0
sca = 0
for i in data["analysisVulnerabilities"]:
    vulnerabliliy = i["vulnerabilities"]
    if vulnerabliliy["file"] != "pom.xml":
        #print (vulnerabliliy["file"], vulnerabliliy["severity"])
        vuln += 1
    else:
        sca += 1
print(vuln, sca)
