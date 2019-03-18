# NAME

hardware - 開発に必要な機材一式について

# SYNOPSIS

主にラズベリーパイを活用する

# SETUP

下記の順番で開発に必要な準備をすすめる

## RASPBERRY_PI

__下記のモデルを採用する__

- 標準サイズ
    - `Raspberry Pi 3 Model B` 以降のバージョン
- ミニサイズ
    - `Raspberry Pi Zero W`
    - `Raspberry Pi Zero WH`

__購入方法__

- インターネットショッピングを活用する
    - [SEE ALSO](#see-also) の「ショッピングサイト」のリンクを参考にする
- 実店舗で購入する
    - [SEE ALSO](#see-also) の「電子部品関係の店舗」のリンクを参考にする

__ラズベリーパイの詳細__

- 書籍を参考にする
    - [SEE ALSO](#see-also) の「関連書籍」のリンクを参考にする
- インターネットの記事を参考にする
    - [SEE ALSO](#see-also) の「関連サイト」のリンクを参考にする

## PARTS

__開発に必要なもの__

- Raspberry Pi
    - マイクロ SD カード (8GB 以上推奨)
    - マイクロ USB アダプター電源 (出力に注意、電気が足りないと不安定になる)
        - 推奨出力 5V, 2.5A (2019年現在)
    - ケース (必須ではないが各端子を壊さないためにあると良い)
- Raspberry を操作する
    - USB キーボードとマウス (一般的なもの)
    - HDMI ケーブルと HDMI 接続ができるPC用モニター (一般的なもの)
    - HDMI と Mini HDMI 変換器 (モデル `Zero w` もしくは `WH` は必要)
    - USB と micro USB 変換器 (モデル `Zero w` もしくは `WH` は必要)
- インターネット環境
    - 無線LANが使用できる環境一式

__購入方法__

- Raspberry Pi と同様の購入先から揃えられる

## INSTALL

__オペレーションシステムをインストール__

- 公式サイトの資料を活用する (projects には様々な資料が存在する)
    - [SEE ALSO](#see-also) の「ラズベリーパイの設定」のリンクを参考にする
    - 最近のWEBブラウザは日本語翻訳の機能があるので活用する
- 初期パスワードについて
    - パスワードは変更する、理由は `system.md` で解説

## POINT

__一連の作業についての注意事項__

- SSH や VNC を使って Raspberry Pi を遠隔操作する方法があるが完璧に操作ができるわけでないことを覚えておく
- 購入はネットショップの方が安くつく場合が多いが、リアルショップに行くと思わぬ商材を見つけることもあるのでバランスよく使い分ける
- 作業につまづいた時は公式サイトの情報を見る方が間違いは少ない


# SEE ALSO

__ショッピングサイト__

- <https://www.amazon.co.jp/> - アマゾン
- <https://raspberry-pi.ksyic.com/main/index> - KSY
- <https://jp.rs-online.com/web/> - アールエスコンポーネンツ
- <https://www.switch-science.com/> - スイッチサイエンス
- <http://akizukidenshi.com/> - 秋月電子通商
- <https://www.sengoku.co.jp/> - 千石電商

__電子部品関係の店舗__

- 福岡地区
    - <http://www.kahoparts.co.jp/> - カホパーツセンター
    - <https://www.marutsu.co.jp/pc/static/shop/hakata-gofukumachi> - marutsu

__関連サイト__

- <https://www.raspberrypi.org/> - Raspberry Pi 公式サイト
- <https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up> - ラズベリーパイの設定
- <https://ja.wikipedia.org/wiki/Raspberry_Pi> - wiki ペディア

__関連書籍__

- <https://www.oreilly.co.jp/books/9784873118314/> - Raspberry Pi を始めよう 第3版
- <https://www.oreilly.co.jp/books/9784873118116/> - Raspberry Piクックブック 第2版
