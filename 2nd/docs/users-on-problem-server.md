# problem-serverにおけるユーザ情報

SSHして色々やる際に使ってもらうアカウント
適当に早い順に割り振っていく
CTFdのアカウントとは別なので、適当でいい
パスワードは後から変えてもらってもどっちでもいい

`newusers`コマンドと`pwgen`コマンドを組み合わせてよしなに作る

```bash
for i in {01..10}; do
	username="user$i"
	password=`pwgen 8 1`
	echo "${username}:${password}::::/home/${username}:/bin/bash" >> users
done;

newusers users
```

↑な感じで作る

 user  | password | ctfd            |
-------|----------|-----------------|
user01 | ooYoo4oh | reserved        |
user02 | Aikou4ph | reserved        |
user03 | ieK3neib | reserved        |
user04 | Queet7ie | reserved        |
user05 | Oin3ThoF | reserved        |
user06 | aa9dae3N | Nakaya          |
user07 | aePhi8ee | Cub3            |
user08 | Ood8Eeph | rainierrr       |
user09 | oToo7eth | emma            |
user10 | oor5UC9w | Osadakun        |
user11 | ahD1ipha | takumi          |
user12 | ieB4kool | ik14            |
user13 | Ahtuu4ri | mae-da          |
user14 | Shoong9O | umeshin         |
user15 | kieC1eim | ishihara-taichi |
user16 | auGoh6ne | saak            |
user17 | thiXief1 | maimai          |
user18 | Eis5Iech | rui             |
user19 | VeiFaic6 | torkn           |
user20 | zul1Aixa | t0kapo          |
user21 | wiegu2Ie | mtms            |
user22 | bat0vooV |                 |
user23 | aoRohWe6 |                 |
user24 | juiPh0Ph |                 |
user25 | peen2Shi |                 |
user26 | Ie8oopae |                 |
user27 | Eegie6od |                 |
user28 | OoB4wait |                 |
user29 | ieSho6th |                 |
user30 | Nohshoo9 |                 |
