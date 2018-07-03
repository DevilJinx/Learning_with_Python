import random  # 导入random模块

def getAnswer(answerNumber):  # 定义getAnswer函数
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidely so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

# r = random.randint(1, 9)  # 调用random.randint函数，带两个参数,1和9
# fortune = getAnswer(r)  # 调用getAnswer函数，参数为r，
                        # r的值保存到answerNumber变量中
                        # 程序返回到getAnswer()，返回的字符串赋予fortune变量
# print(fortune)
print(getAnswer(random.randint(1, 9)))  # 将返回值作为参数传递给getAnswer()调用