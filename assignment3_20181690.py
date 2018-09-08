# 20181690 정유선

import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')     # r:read, b:binary
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []

    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")     #inputstr 값을 공백 기준으로 잘라 parse에 저장

# add
        if parse[0] == 'add':
            if len(parse) == 4:
                try:
                    record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                    # 공백 기준 (2번째 단어 = Name value), (3번째 = Age value), (4번째 = Score value)로 dic record에 저장
                    scdb += [record]
                except:  # 에러처리 : Age, Score의 value가 정수가 아닐 때
                    print("나이(정수 값), 성적(정수 값)을 정확히 입력해주세요.")
            else:      # 에러처리 : value에 입력되지 않은 값이 있을 때
                print ("이름, 나이, 성적을 정확히 입력해주세요.")

# del 명령 수정
        elif parse[0] == 'del':
            for i in scdb:      # 이중 for문으로 name 같은 모든 사람 레코드 제거
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)

# show
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

# find 명령 추가
        elif parse[0] == 'find':
            if len(parse) == 2:    # 입력값이 find, name 2개 일 경우
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for attr in p:
                            p[attr] = str(p[attr])     # int + str 하면 에러가 나므로 Age, Score를 str로 변환
                            print(attr + "=" + p[attr], end=' ')
                        print()
                    elif p['Name'] != str(parse[1]):     # 에러처리 : 이름을 숫자로 입력했을 때
                        print('이름을 정확히 입력해주세요.')
                        break
            else:
                print('이름을 정확히 입력해주세요.')

# inc 명령 추가
        elif parse[0] == 'inc':
            if len(parse) == 3:     # 입력값이 inc, Name, amount 일 경우
                amount = int(parse[2])
                for i in scdb:
                    i['Age'] = int(i['Age'])
                    i['Score'] = int(i['Score'])
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] += amount
                        for attr in p:
                            p[attr] = str(p[attr])
                            print(attr + "=" + p[attr], end=' ')
                        print()
            else:
                print('점수를 정확히 입력해주세요.')

# quit
        elif parse[0] == 'quit':
            break

        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            p[attr] = str(p[attr])     # int + string이 안되므로 바꿔줌
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
