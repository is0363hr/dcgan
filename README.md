Overview

DCGANを動かしてみた。

## Description

以下、動作確認済みの環境構築を説明する。

pythonのバージョンは2.7だと動いた。
3.6だと動かない説。

Anacondaやpyenvの仮想環境を使用するのがオススメ。

Anacondaで仮想環境を作成したため、以下condaコマンドを使用する。
pipでも可。
conda と pip の混在はダメ絶対。

## Requirement

### 開発環境

| 使用ツール | バージョン | URL |
| ---- | ---- | ---- |
| python(仮想環境) | 2.7 | https://www.anaconda.com/ |
| tensorflow | 1.10.0 | http://tensorflow.classcat.com/2018/08/10/tensorflow-1-10-0-release-note/ |

### 使用ライブラリ (Python)

| 使用ライブラリ | 説明 |
| ---- | ---- |
| keras | ニューラルネットワークライブラリ |
| Numpy | python用の数値計算Wrapperライブラリ |
| scipy | 高度な科学計算を行うためのライブラリ |
| requests | httpライブラリ |
| beautifulsoup4 | Webページから情報を収集できるライブラリ |
| lxml | libxml2/libxsltとElementTree APIを組み合わせた強力でPythonicなXML処理ライブラリ |

## Install & Usage

### DCGAN

まず、クローンしてソースコードをダウンロードしよう。

```bash
git clone https://github.com/is0363hr/dcgan.git
cd gan
python main.py
```

たぶんそのままじゃ動かないので以下環境構築の説明。

上記で説明したライブラリをインストールする。
ただし、スクレイピングで画像を収集する必要がないなら、requests以下のライブラリは必要ない。

```bash
conda install tensorflow=1.10.0
conda install keras
conda install scipy
```

OpenCVは安定したバージョンじゃないと動かなかったので注意

```bash
conda install opencv
```


### スクレイピング

画像をネットから自動で収集したい人は必見！
スクレイピングで簡単に画像を収集しよう。
でも、yahooの画像サイトとかはimgタグで画像が張られてないから取れないいいいいい

```bash
conda install requests
conda install beautifulsoup4
conda install lxml
```


## Demo

## VS.

## Contribution

## Licence

## References



## Author

[tamakawa](https://github.com/is0363hr)



