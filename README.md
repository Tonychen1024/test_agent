# test_agent

最小可執行遊戲骨架，使用 Python + Pygame。

## 資料夾結構

```
test_agent/
├── main.py              # 程式入口
├── requirements.txt     # 依賴套件
└── game/
    ├── game.py          # Game 類別、主迴圈、狀態機
    └── states/
        ├── menu.py      # 選單畫面
        ├── playing.py   # 遊戲中畫面
        └── game_over.py # 遊戲結束畫面
```

## 操作說明

| 狀態      | 按鍵           | 動作             |
|-----------|----------------|------------------|
| Menu      | `Enter`        | 開始遊戲         |
| Playing   | `ESC`          | 結束（Game Over）|
| Game Over | `R`            | 回到選單         |
| Game Over | `Q`            | 離開程式         |

## 如何執行

### 1. 安裝依賴

```bash
pip install -r requirements.txt
```

### 2. 執行遊戲

```bash
python main.py
```