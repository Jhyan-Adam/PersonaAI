# Original Author: aqeelanwar
# Transformed by: Jhyan Adam
# Created: 15 June, 2020, 4:13 AM
# Transformed: 22 Jan, 2021, 9:15 PM
# Author Email: aqeel.anwar@gatech.edu

# import emoji
import time as T
import re
import numpy as np
import Vectoriser

class ChatReader:
    
    def __init__(self):
        self.path = "./Chats/Chat.txt"
        self.chat = open(self.path, encoding="utf-8", mode="r")
        self.chat = self.chat.read()

    def chatCrawler(self, chat):

        messageSCntr = 1
        messageRCntr = 1
        ratioSR = 1
        pktSizeS = 3
        pktNumberS = 30
        pktSizeR = 6
        pktNumberR = 30
        contactR = "Jhyan"
        contactS = ""
        # rcvrPktCntr = 0
        # sdrPktCntr = 0
        receiverPackets = np.empty(shape=(pktNumberR, pktSizeR), dtype=object) #NEXT STEP: ADD A DIMENSION TO THESE TO PREVENT ARRAY ELEMENT AS SEQUENCE ERROR AND READJUST DATA FORMATTING
        senderPackets = np.empty(shape=(pktNumberS, pktSizeS), dtype=object)

        pattern_time_24hr = ",? (0?[0-9]|1[0-9]|2[0-3]):([0-5][0-9])(:[0-5][0-9])?"
        pattern_time_12hr = (
            ",? (0?[0-9]|1[0-2]):([0-9]|[0-5][0-9])(:[0-5][0-9])? [APap][Mm]"
        )

        pattern_date_US = (
            "(0?[1-9]|1[0-2])[/.-](0?[1-9]|[12][0-9]|3[01])[/.-](\d{2}|\d{4}),? "
        )
        pattern_date_UK = (
            "([12][0-9]|3[01]|0?[1-9])[/.-](0?[1-9]|1[0-2])[/.-](\d{2}|\d{4}),? "
        )

        last_message_end_idx = 0
        is_UK = False
        dp = re.compile(pattern_date_UK)
        for d in dp.finditer(chat):
            date = d.group()
            date = date.replace("-", "/")
            date = date.replace(".", "/")
            if int(date.split("/")[0]) > 12:
                pattern_date = pattern_date_UK
                is_UK = True

        if not is_UK:
            pattern_date = pattern_date_US

        is_12hr = False
        if len(re.findall(pattern_time_12hr, chat)) > 50:
            is_12hr = True
            pattern_time = pattern_time_12hr
        else:
            pattern_time = pattern_time_24hr


        # Array Indices Declaration
        rowIdxR = 0
        colIdxR = 0
        rowIdxS = 0
        colIdxS = 0

        # Date Pattern Declaration
        pattern = pattern_date + pattern_time[3:]
        pattern_time = pattern_time[3:]
        p = re.compile(pattern)
        #cc = re.findall(pattern, chat) #UNUSED
        for m in p.finditer(chat):
            DateTime = m.group()
            # Split dateTime
            time = re.search(pattern_time, DateTime).group()
            date = re.search(pattern_date, DateTime).group()
            if "," in date:
                date = date[:-2]
            date = date.replace("-", "/")
            date = date.replace(".", "/")
            if is_UK:
                spp = date.split("/")
                date = spp[1] + "/" + spp[0] + "/" + spp[2]
            #date = date.replace(' ', '')
            #print(date) #DEBUGGING
            date = date.replace(" ", "")
            if len(date.split("/")[-1]) == 4:
                date_split = date.split("/")
                if len(date_split) < 3:
                    date_split = date.split(".")
                #print(date) #DEBUGGING
                date = date_split[0] + "/" + date_split[1] + "/" + date_split[2][2:4]

            
            flagSetContactS = True
            if last_message_end_idx > 0:
                contact_and_msg = chat[last_message_end_idx + 3 : m.start()-2]
                split_ = contact_and_msg.split(":")
                
                #Send/Receive Counting:
                if len(split_) > 1:
                    # Msg by user
                    contact = split_[0]
                    if contact == contactR:
                        messageRCntr += 1
                    else:
                        if flagSetContactS:
                            contactS = contact
                            flagSetContactS = False
                        messageSCntr += 1

                    message = u""
                    message = split_[1].replace("\n", "\n ")

                elif len(split_) == 1:
                    # System generated message
                    contact = "System Generated"
                    message = split_[0].split("\n")[0]

            last_message_end_idx = m.end()

        # Ratio Calculation: (Seperate into 2 ratios, s/r and r/s. Evaluate larger then use to calculate which packet size to multiply)
        if messageRCntr > messageSCntr:
            ratioSR = messageRCntr/messageSCntr
        else:
            ratioSR = messageSCntr/messageRCntr

        last_message_end_idx = 0
        for m in p.finditer(chat):
            # Data Formatting:
            if last_message_end_idx > 0:
                contact_and_msg = chat[last_message_end_idx + 3 : m.start()-2]
                #print (m.group()) #DEBUGGING
                #print (contact_and_msg) #DEBUGGING
                split_ = contact_and_msg.split(":")
                #print (split_) #DEBUGGING


                if len(split_) > 1:
                    contact = split_[0]
                    message = u""
                    message = split_[1].replace("\n", "\n ")

                # Packet Maker
                if not "<Media omitted>" in message:
                    if colIdxS == pktSizeS:
                        colIdxS = 0
                        rowIdxS += 1
                    if colIdxR == pktSizeR:
                        colIdxR = 0
                        rowIdxR += 1
                    print (message) #DEBUGGING

                    tokens = Vectoriser.bigramTokenise(message) 
                    decimals = (Vectoriser.decimalEncode(tokens))

                    if rowIdxS < pktNumberS:
                        if contactS == contact:
                            senderPackets
                            senderPackets[rowIdxS, colIdxS] = tokens
                            colIdxS += 1

                    if rowIdxR < pktNumberR:
                        if contactR == contact:
                            receiverPackets
                            receiverPackets[rowIdxR, colIdxR] = tokens
                            colIdxR += 1

            last_message_end_idx = m.end()
        
        print(senderPackets) #DEBUGGING
        #print("\n######break######", contactS, "\n") #DEBUGGING
        print(receiverPackets) #DEBUGGING
        #print(ratioSR) #DEBUGGING
        #return (senderPackets, receiverPackets) #DEBUGGING
        return np.asarray(senderPackets, dtype=np.dtype("U100")), np.asarray(receiverPackets, dtype=np.dtype("U100"))

obj = ChatReader() #DEBUGGING
print(obj.chatCrawler(obj.chat)) #DEBUGGING

#TODO make a dictionary for bag of words but don't use just words and counts; use tf-idf weightings and the "words" must be bigram tokens.
#Create a dictionary generation algorithm to automatically generate one for a given chat with each new bigram. test