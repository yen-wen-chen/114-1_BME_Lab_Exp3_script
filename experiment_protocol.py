# source venv/bin/activate
import time
import subprocess

import platform
import threading

def play(prompt):
    """跨平台非阻塞播放音檔"""
    def _play():
        system = platform.system()
        filename = f"{prompt}.mp3"

        try:
            if system == "Darwin":  # macOS
                subprocess.Popen(
                    ["afplay", filename],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

            elif system == "Windows":  # Windows
                # PowerShell 播放 mp3 / wav
                subprocess.Popen(
                    ["powershell", "-c",
                     f"(New-Object Media.SoundPlayer '{filename}').PlaySync()"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

            elif system == "Linux":
                subprocess.Popen(
                    ["aplay", filename],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

            else:
                print(f"[未知平台無法播放]：{system}")

        except Exception as e:
            print(f"[語音提示缺失]：{prompt} ({e})")

    threading.Thread(target=_play, daemon=True).start()


def play(prompt):
    """跨平台非阻塞播放音檔"""
    def _play():
        system = platform.system()
        filename = f"{prompt}.mp3"

        try:
            if system == "Darwin":  # macOS
                subprocess.Popen(["afplay", filename],
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL)
            elif system == "Windows":
                # 方法 1: 用 PowerShell (支援 mp3 / wav)
                subprocess.Popen(
                    ["powershell", "-c",
                     f"(New-Object Media.SoundPlayer '{filename}').PlaySync()"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                # 方法 2（備用）: 若轉成 WAV，可用 winsound.PlaySound
                # winsound.PlaySound(filename, winsound.SND_FILENAME)
            else:  # Linux
                subprocess.Popen(["aplay", filename],
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"[語音提示缺失]：{prompt} ({e})")

    threading.Thread(target=_play, daemon=True).start()




# -------------------
# 工具函式
# -------------------


def wait(sec, message=""):
    """顯示倒數計時"""
    if message:
        print(message)
    for i in range(sec, 0, -1):
        print(f"  倒數 {i} 秒", end="\r")
        time.sleep(1)
    print(" " * 20, end="\r")

# -------------------
# Class 1：放鬆規則
# -------------------
def class1_relaxation():
    print("\n=== Class 1：放鬆規則 ===")
    print("初始階段：0–20 秒放鬆預備")
    print("每回合：0–20 秒閉眼呼吸；20–40 秒喚醒活動")
    print("總時長約 420 秒，採樣率建議：500 Hz\n")

    play("放鬆")
    wait(20, "放鬆預備 20 秒")

    for i in range(1, 11):
        print(f"\n--- 第 {i} 回合 ---")
        play("閉眼")
        wait(20, "閉眼，緩慢呼吸 20 秒")
        play("睜眼")
        wait(20, "喚醒、休息並活動 20 秒")

    print("\n[完成] Class 1 放鬆規則結束。")

# -------------------
# Class 2：專注規則
# -------------------
def class2_focus():
    print("\n=== Class 2：專注規則 ===")
    print("初始階段：0–20 秒預備開啟 dot_animation.exe")
    print("每回合：0–20 秒專注注視螢幕；20–40 秒縮小視窗休息")
    print("總時長約 420 秒，採樣率建議：500 Hz\n")

    play("放鬆")
    wait(20, "預備開啟動畫程式")

    for i in range(1, 11):
        print(f"\n--- 第 {i} 回合 ---")
        play("專注")
        print("開啟 dot_animation.exe")
        #proc = subprocess.Popen(["python3", "dot_animation.py"])
        wait(20, "請注視移動的點 20 秒")

        # 結束動畫或最小化
        #proc.terminate()
        play("休息")
        wait(20, "縮小視窗並休息 20 秒")

    print("\n[完成] Class 2 專注規則結束。")

# -------------------
# Class 3：睜閉眼規則
# -------------------
def class3_eye_control():
    print("\n=== Class 3：睜閉眼規則 ===")
    print("初始階段：0–20 秒穩定閉眼")
    print("每回合：0–20 秒睜眼不眨眼；20–40 秒閉眼")
    print("總時長約 420 秒，採樣率建議：500 Hz\n")

    play("閉眼")
    wait(20, "閉眼預備 20 秒")

    for i in range(1, 11):
        print(f"\n--- 第 {i} 回合 ---")
        play("睜眼")
        wait(20, "睜眼且不眨眼 20 秒")
        play("閉眼")
        wait(20, "閉眼休息 20 秒")

    print("\n[完成] Class 3 睜閉眼規則結束。")

# -------------------
# 主程序
# -------------------
def main():
    print("==========================================")
    print("     生理訊號測試控制腳本  (Ver. 1.2)")
    print("==========================================")
    print("1 = Class 1 放鬆規則")
    print("2 = Class 2 專注規則")
    print("3 = Class 3 睜閉眼規則")
    print("------------------------------------------")

    choice = input("請輸入數字選擇模式: ").strip()

    if choice == "1":
        class1_relaxation()
    elif choice == "2":
        class2_focus()
    elif choice == "3":
        class3_eye_control()
    else:
        print("輸入錯誤，請重新執行。")
        return

    print("\n==========================================")
    print("⚠️ 測試結束，請確認以下項目：")
    print("1. 實際紀錄時長是否約 420 秒。")
    print("2. 輸出資料 txt 的總行數是否正確。")
    print("3. 若需下一次測試，請重新啟動程式。")
    print("==========================================")

if __name__ == "__main__":
    main()
