# NAME

system - 開発環境の設定の仕方について

# SYNOPSIS

主に Raspbian と手元 PC は Mac および Windows を活用

# SETUP

- UNIX(Linux)系のコマンドラインの操作が不安な場合は事前に学習しておく
    - 「Raspberry Pi を始めよう」の2章が参考になる
    - [SEE ALSO](#see-also) の「Raspberry Pi を始めよう 第3版」
- 遠隔操作については完璧ではないことに注意する
    - 「Raspberry Piクックブック」の2章が参考になる
    - [SEE ALSO](#see-also) の「Raspberry Piクックブック 第2版」
- ラズパイに設定するパスワードなどについては事前になににするのか決めておく
    - 例:
    - host: raspberrypi
    - user: pi
    - pass: ****
- Python について
    - 基本的には Python3 を活用する

## RASPBIAN

__ラズパイのシステムとハードの情報を調べる__

- 左上のラズパイマーク -> アクセサリ -> LXTerminal

```
(OSのディストリビューション名)
$ cat /etc/os-release

(Linuxカーネルのバージョン)
$ cat /proc/version

(ボードのバージョンを調べる)
$ cat /proc/cpuinfo
```

このドキュメント作成時は(Raspbian GNU/Linux 4.14.98-v7)の最新

__デスクトップの設定 (こちらの選択は好みでも良い)__

- 左上のラズパイマーク -> 設定 -> Appearance Settings -> Desktop
    - Docments(ドキュメント): チェックしない
    - Wastebasket(ゴミ箱): チェックする
    - Mounted Disks(挿入されているSDカード): チェックしない

__パスワードの設定__

- 左上のラズパイマーク -> 設定 -> Raspberry Pi の設定 -> システム
- インストールの段階で初期パスワードを変更していない場合は変更する
    - 変更しないと ssh や vnc を有効にした時に警告がでる
    - パスワードを設定しない場合は初期パスワードは `raspberry`

__遠隔操作の設定__

- 左上のラズパイマーク -> 設定 -> Raspberry Pi の設定 -> システム -> インターフェイス
    - SSH, VNC 有効にする
    - 変更した後は再起動する

__ネットワーク接続状況確認__

- 左上のラズパイマーク -> アクセサリ -> LXTerminal

```
(IPアドレスを調べる)
$ hostname -I

(もっと詳しく調べる)
$ ifconfig
```

- eth0(有線LAN), lo(ループバック), wlan0(無線LAN)
- ちなみにこのドキュメント作成時は 192.168.1.129 とでる

__IPアドレスを固定するやり方__

なぜIPアドレスを固定するのか

```
お手元のPCからラズパイへリモートアクセスしたい場合、別途 ssh や vnc
などのアプリからアクセスをすることのなるが、その時のアクセス先を指定するのに
IPアドレスを指定しなくてはいけない、ローカルホスト内においてルーターで自動的に
IPアドレスが振り当てられることがおおいので、毎回アクセス中のIPアドレスを
調べる手間を省くために固定にするやり方が取られることがよくある
代替え案として、ホストネームを使ってアクセスするやり方もあるので、
IPアドレスを固定することは必須ではない
```

- ラズパイが接続している無線LANルーターのIPアドレスを調べる
    - ちなみにこのドキュメント作成時は 192.168.1.1 とでる

```
(arp はアクセスしたもしくはされたIPアドレスの履歴がみれる)
$ arp -a
```

- 固定したい IP アドレスを決める(この値は任意で決める)
    - ちなみにこのドキュメント作成時は 192.168.1.200/24 にした

- /etc/dhcpcd.conf ファイルに書き込む

暫定で下記をIPアドレスと仮定した場合

固定したIP: 192.168.1.200/24
ルーターのIP: 192.168.1.1

GUI で設定するやり方

- 右上のwifiマーク右クリック -> Network Preferences
    - Configure: interface, wlan0
    - Automatically configure empty options: チェックしない
    - Disable IPv6: チェックしない
    - IPv4 Address: (固定したIP)
    - IPv6 Address: (入力しない)
    - Router: (ルーターのIP)
    - DNS Servers: (ルーターのIP)
    - DNS Search: (入力しない)
- 適用をクリック、その後は再起動

CUI で設定するやり方

```
(このコマンドでは nano が立ち上がる nano がわからない人は GUI でやった方がいい)
$ sudoedit /etc/dhcpcd.conf

(ファイルの最後に下記を追加して保存後、再起動)
interface wlan0
static ip_address=(固定したIP)
static routers=(ルーターのIP)
static domain_name_servers=(ルーターのIP)
```

__注意__

- 固定したIPは今回は [192.168.1.200/24] にしたが、末尾 200 が使われているとうまくいかない
- 末尾が使われるか、もしくは使用不可なのかはネットワークの設定にもよるので試すしかない
- 違うwifiに接続した場合はまた設定をみなおさないといけない

__ソースコードを配置する__

下記の場所をラズパイを制御するスクリプト置き場としたい

`/home/pi`

github を活用する

```
(今いる場所)
$ pwd
$ /home/pi

(現在のディレクトリ状況確認)
pi@raspberrypi:~ $ ls -a
.            .bash_history  .cache   .gnupg   .mozc  .pp_backup  .vnc                  MagPi         デスクトップ  音楽
..           .bash_logout   .config  .idlerc  .nano  .presage    .xsession-errors      ダウンロード  ドキュメント  画像
.Xauthority  .bashrc        .dbus    .local   .pki   .profile    .xsession-errors.old  テンプレート  ビデオ        公開

(鍵を保管するディレクトリを作成)
$ mkdir ~/.ssh

(パーミッションを変更)
$ chmod 700 ~/.ssh

(ラズパイ 側で鍵の生成、いろいろ聞かれるがすべてリターン)
$ ssh-keygen -t rsa -C 'ayame'

(id_rsa -> 秘密鍵 id_rsa.pub -> 公開鍵)
$ ls -a ~/.ssh/
.  ..  id_rsa  id_rsa.pub

$ cat ~/.ssh/id_rsa.pub
(cat コマンドで標準出力し内容をコピペ)
```

Github に公開鍵を登録

- Becom の Github サイトに登録する
    - [SEE ALSO](#see-also) の「Becom github」
    - ayame リボジトリが見れない場合は権限をもらう
- ayame リポジトリ
    - Settings -> Deploy keys -> Add deploy key(クリック)
    - Title -> raspberry (もし使われていたら別の名前)
    - key -> 公開鍵の内容をコピペする

ラズパイから通信確認

```
pi@raspberrypi:~ $ ssh -T git@github.com
The authenticity of host 'github.com (192.30.255.113)' can't be established.
... connecting (yes/no)? yes

(yes と入力)

RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.255.113' (RSA) to the list of known hosts.

(known_hosts に履歴が追加)

Hi Becom-Developer/ayame! You've successfully authenticated, but GitHub does not provide shell access.
(Github と接続ができたメッセージ)
```

__githubとうまく通信できない場合__

```
ssh: Could not resolve hostname github.com: Temporary failure in name resolution
```

```
このようなエラーが出てうまく通信できない場合はIPを固定したことによるものかもしれない
いちど固定IPの設定を外して再起動後、しばらくしてから通信してみる
```

github から ラズパイへ git clone

```
(ソースコードを展開する場所へ移動)
$ cd ~/

(git を展開、このリポジトリは pull しかできない)
$ git clone git@github.com:Becom-Developer/ayame.git
```

__Python の確認__

- python 自体や pip コマンドが何であるのかがわからない人は基本的な学習をしておく
    - [SEE ALSO](#see-also) の「Python Boot Camp」参考

```
(実行コマンドを調べる)
$ which python
/usr/bin/python
(実行コマンドを調べる python3)
$ which python3
/usr/bin/python3

(使っているバージョンを調べる)
$ python --version
Python 2.7.13
$ python3 --version
Python 3.5.3

(追加でインストールされたライブラリは pip コマンドで管理)

(pip コマンドはいろんな指定がある)
$ pip3 --version
pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.5)
$ pip2 --version
pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)
$ pip --version
pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)

(インストールすみのライブラリ)
$ pip3 list --format columns
...
RPi.GPIO          0.6.5
...

(GPIO はすでに入っている)

(WiringPi というライブラリを類似のものも含めて検索)
$ pip3 search wiringpi
wiringpi (2.46.0)   - A python interface ...
wiringpi2 (2.32.3)  - A python interface ...

(WiringPi インストール)
$ pip3 install wiringpi

(ayame のサンプルコードを実行してみる)
$ python3 ~/ayame/welcom.py
Welcome ayame!!
```

## MAC

__SSH による接続__

SSH による接続はコマンドラインの操作しかできないが操作は軽快になる

- 接続先の IP アドレスとパスワードを調べておく
- ターミナルで下記を入力 (Open SSH が最初から入っている)

```
(IP アドレスが 192.168.1.129 の場合、IP アドレスはそれぞれの環境でことなる)
$ slogin pi@192.168.1.129
...
(yes と入力)
Are you sure you want to continue connecting (yes/no)?

(パスワード入力)
pi@192.168.1.129's password:
...
(ログインできた)
Last login: Sun Mar 17 13:22:28 2019 from 192.168.1.114
pi@raspberrypi:~ $

(ログアウトするとき)
pi@raspberrypi:~ $ logout
Connection to 192.168.1.129 closed.
$

(こういうやり方でもアクセスできる)
$ ssh 192.168.1.129 -l pi

(control + c のショートカットでもログアウトできる)
```

ホスト名をつかってアクセスするやり方もある

```
(最後に .local をつけるところに注意)
$ ssh pi@raspberrypi.local
```

__VNC による接続__

VNC による接続は全体的に動作が重く、画面の解像度の問題やコピペがうまくできないなどの問題がある

- vnc viewer をダウンロードする
    - [SEE ALSO](#see-also) の「vnc viewer ダウンロード」
- インストール完了後、起動する
- 接続先の IP アドレスを入力
- Username: (接続先のユーザー名、この場合は pi)
- Password: (パスワード入力)

## WINDOWS

# SEE ALSO

- <https://www.oreilly.co.jp/books/9784873118314/> - Raspberry Pi を始めよう 第3版
- <https://www.oreilly.co.jp/books/9784873118116/> - Raspberry Piクックブック 第2版
- <https://www.realvnc.com/en/connect/download/viewer/> - vnc viewer ダウンロード
- <https://github.com/Becom-Developer> - Becom github
- <http://pycamp.pycon.jp/index.html> - Python Boot Camp


