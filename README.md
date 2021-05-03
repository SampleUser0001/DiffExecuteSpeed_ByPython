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

### 環境1

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

