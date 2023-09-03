# -*- coding: utf-8 -*-

# 言語を選択
language = int(input('日本語を選ぶ場合は0、英語を選ぶ場合は1を入力してください。 '))

if language == 0:
    # 日本語で計算結果を表示
    print('答えは', int(input('足される数字は？ ')) + int(input('足す数字は？ ')), 'です')
elif language == 1:
    # 英語で計算結果を表示
    print('The answer is', int(input('What is the number that is added? ')) + int(input('What is the number to add? ')), '.')
else:
    # サポートされていない言語のエラーメッセージ
    print('この言語はサポートされていません')
