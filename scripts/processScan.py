fileName = "./outputHS.json"

#fileName = "/Users/Prayas/Documents/WorkSpace/odp-VulnerableWebApp/result.json"

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
