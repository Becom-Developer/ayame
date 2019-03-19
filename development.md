# NAME

development - 開発の進め方について

# SYNOPSIS

具体的な開発手順や注意事項

# GPIO

ラズパイからハードウェアーをコントロールするには GPIO 端子を活用する

## WARNING

- GPIO 端子を活用するときにやってはいけない事
    - 想定以上の電流を出力、入力させてはいけない
    - 曲げたり、折ったり、切ったり、極端に汚してはいけいない

__GPIO 端子に機器を直接接続するこは危険な行為なので、抵抗など活用する__

## CHECK

__GPIO 端子が壊れていないかを確認する__

予備知識

- GPIO 端子の各名称を確かめる
    - [SEE ALSO](#see-also) の「pinout」参照
- 赤色のジャンパー線(オス-メス) -> プラスにつかう
- 青色のジャンパー線(オス-メス) -> マイナスにつかう
- 抵抗器(470オーム) -> 電流に抵抗を加える
- [BD] -> ブレッドボード
- [R] -> ラズベリーパイ側の意味
- LED -> 発光ダイオード、線が長い方がプラス

点灯確認の流れと考え方

```
LED点灯スクリプト実行 〜 LED点灯まで

[R] 12: BCM 18 (PWM0) -> ジャンパー線(赤) -> [BD] プラス -> 抵抗(470オーム) -> LED(プラス側) -> LED点灯

LED点灯後 〜 終了まで

LED(マイナス側) -> [BD] マイナス -> ジャンパー線(青) -> [R] 6: Ground (GND)
```

メモ

- GND (接地) - 電気を逃す、アース
- 抵抗器のカラーについては見にくいので不安な場合はテスターで計測する
- 赤のLEDを使う場合は抵抗器は470オームか1kオーム両方でやると明るさの違いがわかる

LED点灯スクリプト実行

下記のスクリプトをラズパイ側のターミナルで直接入力する場合(sshでログインでも可能)

```
$ python
>>> import RPi.GPIO as GPIO
>>> GPIO.setmode(GPIO.BCM)
>>> GPIO.setup(18, GPIO.OUT)
>>> GPIO.output(18, GPIO.HIGH)
>>> GPIO.output(18, GPIO.LOW)
>>> GPIO.cleanup()
>>> exit()
```

- (古いバーションの Raspbian では `sudo python` として実行する必要あり)

ayame のサンプルスクリプトで確認する場合

```
(LEDが点滅するスクリプト)
$ python ~/ayame/led/lighting.py
(無限ループで動き続けるので control + c で強制終了)
```

```
(LEDが点灯するスクリプトだが一瞬すぎて確認ができない)
$ python ~/ayame/led/lighting.py
```

__うまく点灯できない場合__

- ラズパイのピンの差し込む場所に注意、`BCM 18` とは 18番目のピンのことではない
- ラズパイのピンの指定は物理的な配置で指定する場合とチップの信号名でしてする場合と二つある

## LED

LEDを使った様々なスクリプト

### PDM

パルス幅変調 (PWM) を使って明るさを調整



# SEE ALSO

- <https://www.oreilly.co.jp/books/9784873118314/> - Raspberry Pi を始めよう 第3版
- <https://www.oreilly.co.jp/books/9784873118116/> - Raspberry Piクックブック 第2版
- <https://pinout.xyz/> - pinout GPIO の各端子の解説
