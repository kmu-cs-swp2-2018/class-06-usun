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
        for i in scdb:
            i['Score'] = int(i['Score'])  # inc실행 시 기존에 있던 이름에도 점수를 추가할 수 있도록 int로 읽어옴
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
            try:
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                # 공백 기준 (2번째 단어 = Name value), (3번째 = Age value), (4번째 = Score value)로 dic record에 저장
                scdb += [record]
            except ValueError:  # 에러처리 : Age, Score의 value가 정수가 아닐 때
                print ("나이, 성적을 정수로 입력해주세요.")
            except IndexError:  # 에러처리 : 입력되지 않은 값이 있을 때
                print("이름, 나이, 성적을 정확히 입력해주세요.")


# del 명령 수정
        elif parse[0] == 'del':
            try:
                isRemoved = False
                for p in scdb[:]:     # name 같은 모든 사람 레코드 제거
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
                        isRemoved = True

                if not isRemoved:     # 에러처리 : 잘못된 이름을 입력했을 때
                    print('삭제할 이름을 정확히 입력해주세요.')


            except IndexError:   # 에러처리 : 이름을 입력하지 않았을 때
                print('삭제할 이름을 입력해주세요.')


# show
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

# find 명령 추가
        elif parse[0] == 'find':
            try :
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for attr in p:
                            print(attr + "={0}".format(p[attr]), end=' ')
                        print()
                    else:     # 에러처리 : 잘못된 이름을 입력했을 때
                        print('검색할 이름을 정확히 입력해주세요.')
                    break
            except IndexError:    # 에러처리 : 이름을 입력하지 않았을 때
                print('이름을 입력해주세요.')


# inc 명령 추가
        elif parse[0] == 'inc':
            try:
                amount = int(parse[2])
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] += amount
                        for attr in sorted(p) :
                            print(attr + "={}".format(p[attr]), end=' ')
                        print()
                    else:     # 에러처리 : 잘못된 이름을 입력했을 때
                        print('점수를 추가할 이름을 정확히 입력해주세요.')
                    break
            except ValueError:     # 에러처리 : 추가할 점수가 정수가 아닐 때
                print('점수를 정확히 입력해주세요.')
            except IndexError:  # 에러처리 : 입력되지 않은 값이 있을 때
                print('이름,점수를 정확히 입력해주세요.')


# quit
        elif parse[0] == 'quit':
            break


        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "={0}".format(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
