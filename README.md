# 分散式系統模擬

## 概述

這是一個用於模擬分散式系統的 Python 應用程式。此應用程式旨在提供用戶一個簡單且直觀的介面來模擬不同的排程策略和節點數量，並分析模擬結果。

## 功能

- **模擬排程策略**: 支援多種排程策略如 SJF、LLF、FCFS 和 RR。
- **模擬節點數量**: 支援不同數量的節點進行模擬。
- **結果儲存**: 將模擬結果儲存為 CSV 檔案。
- **數據分析**: 分析模擬結果並生成圖表。
- **記憶體使用量**: 記錄並分析模擬過程中的記憶體使用量。

## 目錄

- [安裝方式](#安裝方式)
- [使用方式](#使用方式)
- [資料分析方式](#資料分析方式)
- [已知問題](#已知問題)
- [待辦事項](#待辦事項)
- [貢獻者](#貢獻者)
- [聯絡方式](#聯絡方式)

## 安裝方式

1. **複製存放庫**:
    
    ```bash
    git clone https://github.com/Unforgettableeternalproject/DistributedSystemSImulation
    cd DistributedSystemSImulation
    ```
    
2. **安裝附屬檔案**:
    ```bash
    pip install -r requirements.txt
    ```

## 使用方式

單純的執行`DistributedSystemSimulation.py`檔案即可開啟應用程式。

## 資料分析方式

1. **載入資料**:
    - 使用 `load_data_for_systems` 和 `load_data_for_strategies` 函數來載入模擬結果。

2. **分析資料**:
    - 使用 `analyze_data` 函數來分析數據並生成圖表。

## 已知問題

- 模擬結果可能會因為不同的系統配置而有所不同。
- 當前版本僅支援特定的排程策略和節點數量。

## 待辦事項

- 增加對更多排程策略的支援。
- 增加對不同系統配置的支援。
- 增加更多數據分析功能。

## 貢獻者

此專案由 [Bernie](https://github.com/Unforgettableeternalproject) 開發。

歡迎其他人提交 pull requests 或開啟 issues 來提供建議或報告錯誤！

## 聯絡方式

如果您有任何問題或建議，請聯繫我們的開發團隊：
[![Static Badge](https://img.shields.io/badge/mail-Bernie-blue)](mailto:ptyc4076@gmail.com)
