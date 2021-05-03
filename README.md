# Template Python on Docker

Pythonのdiffの実行時間の目安を確認する。

- [Template Python on Docker](#template-python-on-docker)
  - [実行](#実行)
  - [実行結果](#実行結果)
    - [環境1](#環境1)

## 実行

``` sh
docker-compose up
```

## 実行結果

### 環境1 main Windows10 + WSL2

``` txt
get_diff_time | average_count: 10
get_diff_time | count: 1000
get_diff_time | time[0]: 4.616667747497559
get_diff_time | time[1]: 4.611105680465698
get_diff_time | time[2]: 4.604280948638916
get_diff_time | time[3]: 4.595933437347412
get_diff_time | time[4]: 4.610756158828735
get_diff_time | time[5]: 4.600559234619141
get_diff_time | time[6]: 4.613155364990234
get_diff_time | time[7]: 4.584386587142944
get_diff_time | time[8]: 4.5735392570495605
get_diff_time | time[9]: 4.57933497428894
get_diff_time | average: 4.598971939086914
```

### 環境2 オンプレcloud9

``` txt
get_diff_time | average_count: 10
get_diff_time | count: 1000
get_diff_time | time[0]: 5.206491231918335
get_diff_time | time[1]: 5.210886001586914
get_diff_time | time[2]: 5.2126336097717285
get_diff_time | time[3]: 5.21392035484314
get_diff_time | time[4]: 5.208491086959839
get_diff_time | time[5]: 5.208231449127197
get_diff_time | time[6]: 5.210576772689819
get_diff_time | time[7]: 5.209428310394287
get_diff_time | time[8]: 5.215868711471558
get_diff_time | time[9]: 5.2109057903289795
get_diff_time | average: 5.21074333190918
```