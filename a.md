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
とりあえずHello, worldを表示させてみましょう．  
```py
print(Hello, world)
```
これを実行すると画面にHello,worldと表示されるはずです．  
Pythonの参考書とかであればここから文法の説明に入ると思うのですが，今回の目的はゲームを作るという体験を得ることなので，  
とりあえずこのコマンドを行うとコンソールに何か表示されるんだなぐらいの認識で大丈夫です．  
  
ではここから，実際にゲームを作っていきましょう．  
まずはこれを入力してみてください．  
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
これは，Pygameを初期化してみるというコマンドです．  
これを実行してみると，画面が一瞬だけ表示されると思います．  
これでは何がおきているのかわからないので，無限ループを入れてずっと実行し続けてみましょう．
```python
screen_size_x = 720 # 画面の大きさのXを指定
screen_size_y = 480 # 画面の大きさのYを指定
pygame.init() # Pygameを初期化しますよ〜というコマンド
screen = pygame.display.set_mode((screen_size_x, screen_size_y)) # 新しいスクリーンを作りますよのコマンド
while True:
    print("Windows appear!")

```
これで，画面がずっと表示されるはずです．
そうしたら，まずはタイトル画面を作っていきましょう．
まず，タイトル画面に出力するための文字のフォントを設定する必要があります．
先ほどの`screen`変数の下にこれを追加してください．
```
font_en_big = pygame.font.SysFont(None, 128)
font_ja = pygame.font.SysFont('yugothicmediumyugothicuiregular', 128)
font_en = pygame.font.SysFont(None, 64)
```
また先ほどのwhile True:の中身を消して，新しくこの一行を追加してください．
```python
def in_title()
```
これでは未定義エラーが出てしまうので，これらの上に関数を定義しましょう．
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
これを実行してみてください．  
タイトル画面が表示されると思います．  
下に説明を書きます．  
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

