# 各サーバのhost情報

## CTFd

[http://secprj-hack-the-pods.japaneast.cloudapp.azure.com/](http://secprj-hack-the-pods.japaneast.cloudapp.azure.com/)

- user: `admin`
- email: `admin@example.com`
- pw: `xxxx`

## 問題サーバ

hostnameは `problem-server` と `hidden-server` にする
管理者ログインuserは `root` , `pi` を持ち， `pi` はsudo可
SSHは基本 `pi` （ `root` も一応許可しとく）

### problem-server

- user: `root` , `pi`
- pw: `xxxx`

- [SSH CONNECTION]() `:22`
- [Welcome to Web !]() `:80`
- [Another Hidden Page?!]() `:8000`
- [File Not Found]() `$HOME/file-not-found`
- [Exit less command]() `$HOME/exit-less-command`

### problem-server2

- user: `root` , `pi`
- pw: `xxxx`

problem-serverはみんなSSHするのでdaemon系問題はできるだけこっちへ

- [What is HTTP method ?]() `:8001`
- [Million Click]() `:8002`
- [INJECTION]() `:8003`
- [Welcome to PWN !]() `:60000`

### hidden-server

- user: `root` , `pi`
- pw: `xxxx`

基本的には↓の問題の発信元に使いたい

[Who is sending MESSAGE]()

他にもあれば言って欲しい
