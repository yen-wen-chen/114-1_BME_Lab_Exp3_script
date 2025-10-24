# ...existing code...
# 實驗 3 — 控制腳本

簡短說明
- 這個資料夾包含用於生理訊號測試的控制腳本。
- 主要檔案：
  - `experiment_protocol.py`：互動式實驗控制腳本（含語音提示、倒數計時與三種實驗模式）。
  - 數個語音檔（例：放鬆.mp3、閉眼.mp3、專注.mp3、休息.mp3），請放在同一目錄。

如何執行
1. 啟用虛擬環境（如有）。
2. 執行主程式：
   - mac / linux / windows:
     - python experiment_protocol.py
3. 選擇模式 1 / 2 / 3（輸入數字後按 Enter）。
   - Class 2（專注規則）建議手動執行 dot_animation.exe
     - 或 python dot_animation.py
     - 腳本也可直接以外部程式啟動（註解已在 code 中列出範例）。

平台注意事項（音檔播放）
- macOS 使用 afplay；Windows 使用 PowerShell 或 winsound；Linux 使用 aplay。若系統沒有對應工具，語音提示會被忽略並印出錯誤訊息。
- 確認語音檔（mp3）存在於同一資料夾，檔名需與程式內呼叫的字串一致（例：放鬆.mp3）。

常見問題
- 音檔不響：確認系統是否有對應播放程式（afplay / aplay / PowerShell），或改用 wav 並在 Windows 使用 winsound。