## Overview

DCGAN を動かしてみた。

## Description

以下、動作確認済みの環境構築を説明する。

DCGANは python のバージョンは 2.7 だと動いた。  
3.6 だと動かない説。  
スクレイピングは python 3.6じゃないと動かない。  
統一できなくてすいません……  

Anaconda や pyenv の仮想環境を使用するのがオススメ。

Anaconda で仮想環境を作成したため、以下 conda コマンドを使用。  
pip でも可。  
conda と pip の混在するとバグる可能性がある。

## Requirement

DCGAN関係のソースコード
* main.py
* model.py
* ops.py
* utils.py

スクレイピング関係のソースコード
* yahoo_collect.py
* crop.py
* resize.py

既存のデータセットをインストール
* download.py


### 開発環境

| 使用ツール              | バージョン | URL                                                                       |
| --------------------- | ---------- | ------------------------------------------------------------------------- |
| python(dcgan実行時)   | 2.7        | https://www.anaconda.com/                                                 |
| python(スクレイピング) | 3.6        | https://www.anaconda.com/                                                 |
| tensorflow           | 1.10.0     | http://tensorflow.classcat.com/2018/08/10/tensorflow-1-10-0-release-note/ |

### 使用ライブラリ (Python)

#### DCGAN

| 使用ライブラリ | 説明                                                                                   |
| -------------- | -------------------------------------------------------------------------------------- |
| keras          | ニューラルネットワークライブラリ                                                       |
| Numpy          | python 用の数値計算 Wrapper ライブラリ                                                 |
| opencv         | python 画像処理のライブラリ                                                            |
| scipy          | 高度な科学計算を行うためのライブラリ                                                   |

#### スクレイピング

| 使用ライブラリ | 説明                                                                                   |
| -------------- | -------------------------------------------------------------------------------------- |
| requests       | http ライブラリ                                                                        |
| beautifulsoup4 | Web ページから情報を収集できるライブラリ                                               |
| lxml           | libxml2/libxslt と ElementTree API を組み合わせた強力で Pythonic な XML 処理ライブラリ |
| pillow         | Pythonの画像処理ライブラリ                                                          |
| matplotlib     | グラフ描画ライブラリ |

## Install & Usage

### DCGAN

まず、クローンしてソースコードをダウンロード。

```bash
git clone https://github.com/is0363hr/dcgan.git
```

たぶんそのままじゃ動かないので以下環境構築の説明。

上記で説明したライブラリをインストール。

```bash
conda install tensorflow=1.10.0
conda install keras
conda install scipy
```

OpenCV は安定したバージョンじゃないと動かなかったので注意。

```bash
conda install opencv=3.1.0
```

DCGANの実行方法は以下のコマンド
```bash
python main.py --input_height 96 --input_width 96 --crop --output_height 64
--output_width 64 --dataset <filename> --train --epoch 300 --input_fname_pattern "*.jpg"
```

### スクレイピング

画像をネットから自動で収集したい人は必見！  
スクレイピングで簡単に画像を収集できます。

```bash
conda install requests
conda install beautifulsoup4
conda install lxml
conda install pillow
conda install matplotlib
```

yahoo_collect.pyを実行すると画像を勝手に収集してくれる。  
短時間でたくさんダウンロードするので適宜 control c。  
ちなみにこれはpython3.6で動きます。  
python2.7だと動きません……

```bash
python yahoo_collect.py
検索ワードを入力してください :　<検索キーワード>
```

以下の実行で顔面抽出。  
実行する前にファイルパスを確認してください。
```bash
python crop.py
```

以下の実行で画像サイズを統一できる。  
実行する前にファイルパスを確認してください。
```bash
python resize.py
```

これでデータセットの準備は整う。  
train_dataにはデモのデータセットが入っている。

## Demo

## VS.

## Contribution

## Licence

## References
<https://qiita.com/NakaokaRei/items/0551dbfc0ac14176b876>  
<https://github.com/carpedm20/DCGAN-tensorflow>  
<https://qiita.com/ishiwara51/items/3979fbc1c69b4f8ee2d3>  

## Author

[tamakawa](https://github.com/is0363hr)
