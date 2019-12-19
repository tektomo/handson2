# Welcome to Hands-on #2
よろしくお願いします  

# 概要
Pythonでタイピングゲームを作ってみよう

# 必要なもの
- Pythonの実行環境
  - Pygame
- エディタ（VSCode, Atom, Sublime, メモ帳, etc...）
- Git(Hub)

# #0 環境を整えよう
## 0.1 調理器具を揃えよう
※この手順はWindows向けです  
料理を作るためには包丁やガスコンロが必要なように、ゲームを作るためにも必要なものがあります。  
今回はPythonを使っていきます。  
Pythonの実行環境を作っていきましょう  
[公式サイト](https://www.python.org/downloads/)から`Python3.7.5`をダウンロード、インストールしてください。(3.8.0だと必要なライブラリが動きません。)  

## 0.2 特別な器具を揃えよう
先の節で一般的な器具を揃えたので、目玉焼きを作れるようになりました。しかし、まだご飯が炊けません。  
ご飯を炊くために炊飯器が必要なように、ゲームを作るためにも必要なものがあります。  
炊飯器に多数のメーカーがあるように、ゲーム制作のために必要なものにも多くの種類がありますが、今回はPygameというものを採用します。  
スタートメニューを右クリックして、`Windows Power Shell`もしくは`コマンドプロンプト`を実行してください。  
開いたウィンドウに、`python -m pip install pygame`と打ち込み、エンターキーを押すとPygameがインストールされます。  
  
正しくインストールされているか確認するために、実際に実行してみましょう。  
`python -m pygame.examples.aliens`と打ち込みエンターを押すと、インベーダーゲームが起動します。  

## 0.3 冷蔵庫を導入しよう
ところでみなさんは、お店で買ってきた野菜をどこに保管しますか？  
ほとんどを冷蔵庫に入れていると思います。そして、時折ジップロックに入れて日付を書いたりしますよね。  
プログラミングにおいても、ソースコードを置き、またバージョン管理をするためによく使われるものがあります。  
それが **Git** です。  
今回は詳しく説明しませんが、とりあえずこのGitというものを使用するとバージョンの管理がとても楽になります。  
また、それと合わせて使われることが多いのが、**GitHub**です。エッチなサイトではありません。  
このGitHubというのは、オンライン上にファイルをアップロードすることで、  　
例えば自分の別の環境で動かしたり、集団で開発したり、広く様々な人と開発したりと、  
プログラミングをする上でとても便利なものです。  
今回はこれらを使用してファイルの管理も行ってみようと思います。  
[GitHub Desktop公式](https://desktop.github.com/)からGitHub Desktopをダウンロード・インストールして、実行してみましょう。
最初はアカウント登録をする必要があるので、登録しておいてください。


## 0.4 便利グッズを買おう（オプション）
これで皆さんは食事をすることができるようになりましたが、もっと器具を便利にすることができます。  
プログラミングのためのエディタを使用することでQoLが爆上がりします。是非導入して下さい。  
最近ではGUIエディタはVSCodeが一番シェアが高い **(諸説あり)** ので、VSCodeをインストールしていきましょう。（と言っても今回はインストールする以外のことはしません）  
[公式サイト](https://code.visualstudio.com/)よりダウンロード、インストールしてください。  

# #1 はじめの一歩
## 1.1 なにをつくる？
さて、これで料理を作る準備は整ったので、あとは実際に料理を作るだけです。  
今回は、実際にゲームを作りながらPythonを学んでいきます。ずっとみじん切りの練習をしてもつまらないですよね？  
ところで、タイピングゲームを作る前に実際にどのような機能があるのかを考える必要があります。これは料理の材料を考えるのに似ています。  
今回は以下のような機能を持ったタイピングゲームを作っていこうと思います。

- 用意された単語から無作為に選ぶ
- 単語を打ち終わったら新しい単語を表示
- 規定の数を打ち終わったらかかった秒数と正しく打てた数/ミスの数を表示する

これだとまだあまりイメージが沸かないと思うので、ここに完成したものをご用意してあります。  
ダウンロードした後、コマンドプロンプトや任意のシェルで実行してください。
ここではWindows環境での実行方法を提示します。
```sh
py -3.7 app.py
```
チープに見えるかもしれませんが、それは見た目が質素だからです。きっとそう。  
重要なのは機能です。先程の3つの機能が実装されています。  
今回はこれを作っていって、余裕があれば拡張していくことにします。*Done is better than perfect.*  

## 1.2 START
とりあえずHello, worldを表示させてみましょう。  
```py
print("Hello, world")
```
これを実行すると画面にHello,worldと表示されるはずです。  
Pythonの参考書とかであればここから文法の説明に入ると思うのですが、今回の目的はゲームを作るという体験を得ることなので、  
とりあえずこのコマンドを行うとコンソールに何か表示されるんだなぐらいの認識で大丈夫です。  
  
ではここから、実際にゲームを作っていきましょう。  
まずはこれを入力してみてください。  
```python
import random
import sys
import time
import pygame


screen_size_x = 720 # 画面の大きさのXを指定
screen_size_y = 480 # 画面の大きさのYを指定
pygame.init() # Pygameを初期化しますよ〜というコマンド
screen = pygame.display.set_mode((screen_size_x, screen_size_y)) # 新しいスクリーンを作りますよのコマンド
```
これは、Pygameを初期化してみるというコマンドです。  
これを実行してみると、画面が一瞬だけ表示されると思います。  
これでは何がおきているのかわからないので、無限ループを入れてずっと実行し続けてみましょう。
```python
screen_size_x = 720 # 画面の大きさのXを指定
screen_size_y = 480 # 画面の大きさのYを指定
pygame.init() # Pygameを初期化しますよ〜というコマンド
screen = pygame.display.set_mode((screen_size_x, screen_size_y)) # 新しいスクリーンを作りますよのコマンド
while True:
    print("Windows appear!")

```
これで、画面がずっと表示されるはずです。
そうしたら、まずはタイトル画面を作っていきましょう。
まず、タイトル画面に出力するための文字のフォントを設定する必要があります。
先ほどの`screen`変数の下にこれを追加してください。
```
font_en_big = pygame.font.SysFont(None, 128)
font_ja = pygame.font.SysFont('yugothicmediumyugothicuiregular', 128)
font_en = pygame.font.SysFont(None, 64)
```
また先ほどのwhile True:の中身を消して、新しくこの一行を追加してください。
```python
in_title()
```
これでは未定義エラーが出てしまうので、この`while True`の上に関数を定義しましょう。
```python
def in_title():
    print("In title")
    # 文字列をレンダリングする
    start_ap = font_en.render("Press Enter or Space to Start", True, (0, 0, 0))
    end_ap = font_en.render("Press ESC to Quit", True, (0, 0, 0))
    flag = True
    while flag:
        # 画面描画を行う
        screen.fill((200, 200, 200))
        screen.blit(start_ap, (0, 0))
        screen.blit(end_ap, (0, 200))
        pygame.display.update()
```
これを実行してみてください。  
タイトル画面が表示されると思います。  
下に説明を書きます。  
```python
def in_title():
    print("In title")
    # 文字列をレンダリングする
    start_ap = font_en.render("Press Enter or Space to Start", True, (0, 0, 0)) # "Press Enter ..."の文字をfont_enのフォントでレンダリングして"start_ap"Surfaceオブジェクトを生成する
    end_ap = font_en.render("Press ESC to Quit", True, (0, 0, 0)) # "Press ESC ..."の文字をfont_enのフォントでレンダリングして"end_ap"Surfaceオブジェクトを生成する
    flag = True # 続行フラグを立てます
    while flag: # flag = Trueなので無限ループです
        # 画面描画を行う
        screen.fill((200, 200, 200)) # 画面を引数の値の色で塗りつぶす 引数:(R, G, B)
        screen.blit(start_ap, (0, 0)) # start_apを(x, y)の位置に表示する
        screen.blit(end_ap, (0, 200)) # end_apを(x, y)の位置に表示する
        pygame.display.update() # ディスプレイをアップデートする
```

これでタイトル画面ができました。次はキーを押したらゲーム画面に進むようにしていきましょう。  
まずは次の画面に行くためにキー入力をうけるコマンドを作りましょう。  
```python
        # イベントを取得し、特定のキーが押されたときのみ動作を行う
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE or \
                        event.key == pygame.K_RETURN:
                    flag = False
```
下にこれを追加してください  
次に遷移先の画面を作ります。  
新しくゲーム画面の関数を作っていきましょう。  
先ほど打った文の下に、次のコードを載せてください。  
```python
def in_game():
    while flag:
        # 画面を描画する
        screen.fill((200, 200, 200))
        pygame.display.update()
```
そして、一番下のwhile True:に以下の文を追加してください。
```python
in_game()
```
今のコードはこうなっているはずです。説明付きでコードを貼ります。
```py
# ライブラリをインポート
import random
import sys
import time
import pygame


def in_title():
    print("In title")
    # 文字列をレンダリングする
    start_ap = font_en.render("Press Enter or Space to Start", True, (0, 0, 0)) # "Press Enter ..."の文字をfont_enのフォントでレンダリングして"start_ap"Surfaceオブジェクトを生成する
    end_ap = font_en.render("Press ESC to Quit", True, (0, 0, 0)) # "Press ESC ..."の文字をfont_enのフォントでレンダリングして"end_ap"Surfaceオブジェクトを生成する
    flag = True # 続行フラグを立てます
    while flag: # flag = Trueなので無限ループです
        # 画面描画を行う
        screen.fill((200, 200, 200)) # 画面を引数の値の色で塗りつぶす 引数:(R, G, B)
        screen.blit(start_ap, (0, 0)) # start_apを(x, y)の位置に表示する
        screen.blit(end_ap, (0, 200)) # end_apを(x, y)の位置に表示する
        pygame.display.update() # ディスプレイをアップデートする
        # イベントを取得し、特定のキーが押されたときのみ動作を行う
        for event in pygame.event.get(): # 起きたイベントを全て取得
            if event.type == pygame.QUIT: # もしQUITイベントがおこったら終了
                sys.exit()
            if event.type == pygame.KEYDOWN: # もしキーが押されたら
                if event.key == pygame.K_ESCAPE: # もしESCキーが押されたら終了
                    sys.exit()
                elif event.key == pygame.K_SPACE or \
                        event.key == pygame.K_RETURN: # もしSpaceキーかEnterキーが押されたらタイトル画面を終了（無限ループを抜ける）
                    flag = False


def in_game():
    while flag:
        # 画面を描画する
        screen.fill((200, 200, 200)) # スクリーンを(R,G,B)色で塗り潰し
        pygame.display.update() # スクリーンをアップロード


screen_size_x = 720 # 画面の大きさのXを指定
screen_size_y = 480 # 画面の大きさのYを指定
pygame.init() # Pygameを初期化しますよ〜というコマンド
screen = pygame.display.set_mode((screen_size_x, screen_size_y)) # 新しいスクリーンを作りますよのコマンド
# フォントの設定
font_en_big = pygame.font.SysFont(None, 128)
font_ja = pygame.font.SysFont('yugothicmediumyugothicuiregular', 128)
font_en = pygame.font.SysFont(None, 64)
while True: # 無限ループ
    in_title() # in_title関数を実行
    in_game() # in_game関数を実行
```

これで、とりあえずタイトル画面とゲーム画面が出せるようになりました。  
ここから一気に関数を追加して、実際にゲームが作れるところまで進めます。  
以下のようなコードになるように入力してください。  

```py
import random
import sys
import time
import pygame


def select_word(): # 問題となる単語を選択する関数
    word_list = [
        ["ringo", "りんご"],
        ["banana", "ばなな"],
        ["budou", "ぶどう"],
        ["kaki", "かき"],
        ["mikan", "みかん"],
        ["neko", "ねこ"],
        ["inu", "いぬ"],
        ["uma", "うま"],
        ["saru", "さる"],
        ["tori", "とり"]
    ]
    # ワードをランダムで抽出し、抽出したワードは最後尾になる
    i = random.randint(0, len(word_list)-1) # ランダムに選ぶ
    selected_word = word_list.pop(i) # 選んだリストを抽出し削除
    word_list.append(selected_word) # 先ほど消したリストを一番後ろに挿入
    # 選んだワードのリストを返す
    return selected_word


def cut_head_char(word):
    # 先頭をカットした引数を返す
    return word[1:]


def is_empty_word(word):
    # WordがNoneならTrueを、そうでないのならFalseを返す
    return not word


def in_title():
    print("In title")
    # 文字列をレンダリングする
    start_ap = font_en.render("Press Enter or Space to Start", True, (0, 0, 0)) # "Press Enter ..."の文字をfont_enのフォントでレンダリングして"start_ap"Surfaceオブジェクトを生成する
    end_ap = font_en.render("Press ESC to Quit", True, (0, 0, 0)) # "Press ESC ..."の文字をfont_enのフォントでレンダリングして"end_ap"Surfaceオブジェクトを生成する
    flag = True # 続行フラグを立てます
    while flag: # flag = Trueなので無限ループです
        # 画面描画を行う
        screen.fill((200, 200, 200)) # 画面を引数の値の色で塗りつぶす 引数:(R, G, B)
        screen.blit(start_ap, (0, 0)) # start_apを(x, y)の位置に表示する
        screen.blit(end_ap, (0, 200)) # end_apを(x, y)の位置に表示する
        pygame.display.update() # ディスプレイをアップデートする
        # イベントを取得し、特定のキーが押されたときのみ動作を行う
        for event in pygame.event.get(): # 起きたイベントを全て取得
            if event.type == pygame.QUIT: # もしQUITイベントがおこったら終了
                sys.exit()
            if event.type == pygame.KEYDOWN: # もしキーが押されたら
                if event.key == pygame.K_ESCAPE: # もしESCキーが押されたら終了
                    sys.exit()
                elif event.key == pygame.K_SPACE or \
                        event.key == pygame.K_RETURN: # もしSpaceキーかEnterキーが押されたらタイトル画面を終了（無限ループを抜ける）
                    flag = False


def in_game():
    flag = True # フラグ
    count = 1 # 問題数
    score = 0 # 得点
    mistake = 0 # ミス数
    print("In game")
    # 最初のワードをとってきて、それをそれぞれ変数に代入
    word = select_word()
    word_roma = word[0]
    word_ja = word[1]
    # 3秒前のカウントダウンを表示
    for i in range(3):
        screen.fill((200, 200, 200)) # 画面を引数の値の色で塗りつぶす 引数:(R, G, B)
        now_ap = font_en.render(str(3-i), True, (0, 0, 0)) # 今の秒数をレンダリング
        screen.blit(now_ap, (0, 200)) # now_apを表示
        pygame.display.update() # ディスプレイをアップデート
        time.sleep(0.9) # 0.9秒間まつ
    while flag:
        # 画面を描画する
        screen.fill((200, 200, 200))　# 画面を引数の値の色で塗りつぶす 引数:(R, G, B)
        word_ja_ap = font_ja.render(word_ja, True, (0, 0, 0)) # 問題の日本語をレンダリング
        word_roma_ap = font_en_big.render(word_roma, True, (0, 0, 0))　# 問題の英語をレンダリング
        screen.blit(word_ja_ap, (0, 0)) # 問題の日本語を表示
        screen.blit(word_roma_ap, (0, 200)) # 問題の英語を表示
        pygame.display.update()
        # イベントを取得し、正しいキーが押されていれば先頭文字をカット、もう文字がない（=完答した）ときは新しい文字列を探す（ただし回数制限で終了）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == word_roma[0]:
                    score += 1
                    word_roma = cut_head_char(word_roma)
                    if is_empty_word(word_roma):
                        count += 1
                        if count > num_word:
                            flag = False # 問題数が制限に達したら終了
                        word = select_word()
                        word_roma = word[0]
                        word_ja = word[1]
                else:
                    mistake += 1
    return [score, mistake] # スコアとミスを返す


num_word = 10
screen_size_x = 720 # 画面の大きさのXを指定
screen_size_y = 480 # 画面の大きさのYを指定
pygame.init() # Pygameを初期化しますよ〜というコマンド
screen = pygame.display.set_mode((screen_size_x, screen_size_y)) # 新しいスクリーンを作りますよのコマンド
# フォントの設定
font_en_big = pygame.font.SysFont(None, 128)
font_ja = pygame.font.SysFont('yugothicmediumyugothicuiregular', 128)
font_en = pygame.font.SysFont(None, 64)
while True: # 無限ループ
    in_title() # in_title関数を実行
    point = in_game() # in_game関数を実行
```

最後に、result画面を追加しましょう。  
`num_word = ...`の上に新しく以下を追加してください  
```py
def in_result(point):
    print("In result")
    score = point[0]
    mistake = point[1]
    score_ap = font_en.render("Your score is "+str(score), True, (0, 0, 0))
    mistake_ap = font_en.render("Your mistakes are "+str(mistake),
                                True, (0, 0, 0))
    flag = True
    while flag:
        screen.fill((200, 200, 200))
        screen.blit(score_ap, (0, 0))
        screen.blit(mistake_ap, (0, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    flag = False
```
また、`score = in_game()`の下に以下を追加してください
```py
in_result(point) # in_result()関数を実行
```
これで、完成しています。  
この状態で，サンプルのapp.pyと比べてみて，同じならば完成です．

では、ここまでのファイルをGitHubに上げてみましょう。  
GitHub Desktopで，File->Create a new repositoryを選択してください．  
NameとDiscriptionにタイトル，説明をそれぞれ入れ，Local pathに先ほどまで作業していたフォルダを選択してください．  
そのほかは何もせず，Create Repositoryを押すと，リポジトリが作成されます．