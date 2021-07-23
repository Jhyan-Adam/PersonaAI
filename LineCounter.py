with open("./Chats/Chat.txt", encoding="utf-8") as chatFile:
    lines = chatFile.readlines()
    lineCntrR = 0.0
    lineCntrS = 0.0
    ratioSN = 1.0

    for line in lines:
        if not "<Media omitted>" in line:

            if " - Jhyan:" in line:
                lineCntrR += 1
            # print(containsDate)

            if " - Misha:" in line:
                lineCntrS += 1

print("Receiver:", lineCntrR, "Sender:", lineCntrS)

if lineCntrR > lineCntrS:
    ratioSN = lineCntrR/lineCntrS
else:
    ratioSN = lineCntrS/lineCntrR

print(ratioSN)
