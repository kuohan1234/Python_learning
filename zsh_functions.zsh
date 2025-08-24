#!/usr/bin/env zsh

# 函數用法說明
function check_files() {
    # 檢查參數
    # can you explain what is -lt
    # -lt 是一個數字比較運算符，表示「小於」。在這裡，它用於檢查傳遞給函數的參數數量是否少於 1。
    if [[ $# -lt 1 ]]; then
        echo "用法: check_files <pattern> [directory]"
        echo "例如: check_files py ."
        echo "      check_files txt /home/documents"
        return 1
    

    local pattern=$1
    # can you explain what is :-. ?
    # :-. 是 Zsh 的一個參數擴展，用於提供預設值。在這裡，它的意思是「如果第二個參數未提供，則使用當前目錄」。
    local dir=${2:-.}  # 如果沒有提供目錄，使用當前目錄

    # 切換到指定目錄
    cd $dir

    echo "\n=== 符合模式 *.$pattern 的檔案 ==="
    # can you explain what is (N)  here ?
    # (N) 是 Zsh 的一個擴展，表示「名稱」的意思。在這裡，它用於匹配符合條件的檔案名稱。
    # 這意味著如果沒有符合條件的檔案，則不會產生任何錯誤，而是返回一個空的列表。
    for file in *.$pattern(N); do
        if [[ -f "$file" ]]; then
            echo "- $file"
        fi
    done

    echo "\n=== 不符合模式 *.$pattern 的檔案 ==="
    for file in *(N); do
        if [[ -f "$file" && "$file" != *.$pattern ]]; then
            echo "- $file"
        fi
    done
}

# 設定別名讓使用更方便
alias check='check_files'

# generate print said hellow word
function hello() {
    echo "Hello, World!"
}
