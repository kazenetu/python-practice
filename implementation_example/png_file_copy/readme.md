# サンプルコード：filesのpngファイルを改名してresultにコピー
---

## 改名ルール
* *フォルダ名*_ファイル名.png
 
## 変換例
```
files
│  A.png
│
├─Dir1
│  A.png
│
└─Dir2
    └─01
       C.png
```

↓

```
result
 A.png
 Dir1_A.png
 Dir2_01_C.png
```
