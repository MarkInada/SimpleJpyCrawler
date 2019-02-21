# SimpleJpyCrawler

root以下全てのファイルをzip化してAWS Lambdaに置くことで為替レートを監視し、
閾値以上または以下を検出したときに指定のメールアドレスに通知します。

ZIP化する前に以下の変更を行う必要があります。
lambda_function.pyに閾値（upper_rate(上限), lower_rate(下限)）を設定してください。
デフォルトは112円を超えるまたは110円より下がると通知するようになっています。
また、送信元のアドレスとパスワード、送信先のアドレスも入力する必要があります。
"Sender@gmail.com", "Password", "Receiver@gmail.com" を埋めてください。

JavascriptでCRUDアプリを作っている。そこから入力できるようにいつかする・・。