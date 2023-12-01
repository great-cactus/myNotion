# myNotion

作業を中断せずランチャから特定のNotionデータベースにデータを追加する．
UeliでPowershell commandをたたいて実装した．

## Requirements

- [Ueli](https://ueli.app/#/)
- Powershellでのpython実行環境 [参考](https://learn.microsoft.com/ja-jp/windows/python/beginners)
- Notion APIのクライアントキー（以下でNOTION_TOKEN内に格納）[参考](https://developers.notion.com/docs/getting-started)
- 当該データベースのID（以下でGTD_TASK_ID内に格納）[参考](https://booknotion.site/setting-databaseid)

## How to Use

### python

1. addTask.pyを以下のディレクトリへ保存する．
   なおUSERNAMEは個々のWin.マシンでのユーザ名である．
   C:\Users\USERNAME\Documents\WindowsPowerShell

### Powershell

1. powershellを立ち上げ，[notion_client](https://pypi.org/project/notion-client/)をインストールする．

   ```powershell
   pip install notion_client
   ```

2. 管理者権限でpowershellを立ち上げ，.ps1ファイルの実行権限を付与する（権限を与えすぎている気がする）

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine
   ```

3. $PROFILEを作成する．

   ```powershell
   if (!(Test-Path -Path $PROFILE)) {New-Item -ItemType File -Path $PROFILE -Force}
   ```

4. $PROFILEに次の内容を追記する．
   YOUR_DATABASE_IDはデータベースのID，YOUR_API_TOKENは自身のAPIトークンを格納する．
   USERNAMEは個々のWin.マシンでのユーザ名である．

   ```
   # Notion
   $env:GTD_TASK_ID = "YOUR_DATABASE_ID"
   $env:NOTION_TOKEN = "YOUR_API_TOKEN"
   function FNA{
   	python C:\Users\USERNAME\Documents\WindowsPowerShell\addtask.py $args[0]
   	exit
   }
   ```

   >[!Note]
   >powershellではファイルをメモ帳などから直接開けるので便利です.
   > ```
   > notepad $PROFILE
   > ```

### Ueli

1. UeliのCommandlieのShellはPowershellにしておく

2. Ueliランチャーを起動して(Alt + Space?)次のコマンドを打つとデータベースにtestというデータが追加される．

   ```
   >FNA test
   ```

## ToDo

- 実行終了までpowershellが開き鬱陶しい，バックグラウンド処理にする
- 実行終了まで2秒くらいかかる，長い．短くする．
