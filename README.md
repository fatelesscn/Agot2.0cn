# Agot2.0cn

cn offical version update
2016.3.4
中文版本更新1133

修复问题
1.修正 国王之治 打出时候为垂直放置的问题
2.修正 雇佣骑士 被错误的标记为独有卡的问题
3.修正 部署阶段 多张卡牌排列位置的错误，应为从左至右

新功能
独有附属和地区牌在拥有复制品的时候，如果被弃掉会让玩家进行选择，弃掉主卡或弃掉复制品，玩家选择弃掉复制品则复制品进入弃牌堆，玩家选择弃掉主卡则复制品随主卡一起弃掉



2016-2-24


4.2 action finished

2016-2-12


4.2.5 finished

2016-2-10


4.2.2 finished





[system history]

1. System will judge whether an attachment is valid on targeted card or not. Attachments will automatically add STR bonus and icons on attached cards.

![q1] (http://upload.ouliu.net/i/20160205092757fqyx9.png)
![q1] (http://upload.ouliu.net/i/20160205092829e1p80.jpeg)
![q1] (http://upload.ouliu.net/i/20160205092926cna3j.jpeg)
![q1] (http://upload.ouliu.net/i/201602050930523wc5t.jpeg)
![q1] (http://upload.ouliu.net/i/201602050931154kds4.png)

2. Dupes and attachments will stick to orderly targeted cards when player move targeted cards.
![q1] (http://upload.ouliu.net/i/20160205092641yj92x.jpeg)

3. Former carddlg cannot deal with non-unique same copies, so I add a selectmode to players in which they can choose cards on board or in hand, with double click and click next to finish the window
![q1] (http://upload.ouliu.net/i/201602050932013la5g.jpeg)

4. I’m now working on automatic process, these are what I have accomplished:
- Target selecting after initiate stealth
- Unopposed reward in 4.2.3
- Applying all claim effect in 4.2.4 automatically, including int, pow and mil(choose which character to kill->save interrupts->cancel interrupts->judging whether a character is saved successfully->leave play interrupts->leave play reactions)
Now I’m  working on reactions for determining the winner in 4.2.2, which I found very complicated and leads to very slow progress.
![q1] (http://upload.ouliu.net/i/20160205092415zx5k0.jpeg)
