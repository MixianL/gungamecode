# 游戏的脚本可置于此文件中。

 


#定义结局
default ending0 = False
#定义一下序章结局的数值，这样更新的时候可以保证存档读取
default xuzhangjiejv = 0
default money = 0
# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define n = Character("贺美丽",color="#ff69b4")
define m = Character("武不疯",color="#2e8b57")
define e = Character("杨告贞",color="#87cefa")
define p = Character("邢青尧",color="#ff7f50")
define z = Character("张楠楠",color="#da70d6")
define t = Character(
    None,
    window_background=None,
    what_color="#fff",
    what_xalign=0.5
)
define x = Character("武扬柒",color="#006400")



# 游戏在此开始。
screen simple_screen():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "KIND+1"
            textbutton "确定":
                action Return(True)
screen simp_screen():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "KIND-1"
            textbutton "确定":
                action Return(True)

 
label start:


label xuanzezhangjie:


menu:
    
    "序幕":
        jump xumu
    "番外：邢青尧的告白":
        jump xingqingyao
    "会员必看":
        jump huiyuanbikan


    # （命名为 bg room.png 或 bg room.jpg）来显示。
label xumu:
    
    t "此游戏为公测版本，版本号为0.05alpha，在此版本内展示的任何剧情，人物不代表最终版本"
    t "本游戏剧情，人物纯属虚构"
    t "感谢 水清漓   小袁同学   若无 对本游戏的赞助！"
    stop music fadeout 1.0
    scene keting
    with fade
    
    n "哈哈哈哈哈！！这房子真豪华......以后就是我们的了！"with vpunch
    m "你小点声，张楠楠还在附近"
    n "她这么小，能懂什么？    就算是懂了也没关系，因为......"
    ".................."
    e "先生，小姐，该就餐了"
    "你端着餐盘，来到他们两人身边"
    n "好，就放这儿吧。"
    e "好的"
    "你缓缓退下，在墙角偷听他们的对话"
    m "哼哼.......张楠楠可别出什么意外......不然的话，财产可都归我们了......."
    n "哈哈哈哈哈，我会好好照顾她的......"
    
    "你听着他们的对话，脸不禁冷了下来"
default kindness = 0
default relationship_wubufeng = 0
menu:

    "这可不是什么好主意......":
        jump nuchi

    "这计划一般般吧......":
        jump jingguan

label nuchi:
    $ kindness = kindness+1
   
    call screen simple_screen
 

 

    "你正准备冲出去，突然，张楠楠跑了进来"

    jump marry

label jingguan:

    "你正在吐槽之时，刚刚一直在外面玩耍的张楠楠跑了进来，满身都是脏污的她不像是一个文静的女孩"

    jump marry

label marry:

    t "武不疯，贺美丽一齐看向张楠楠，俩人都露出渗人的目光，伴着假笑"
    "说实话，他们可真不会演戏"
if kindness >= 1:
    "这计划真不靠谱...."
    jump fazhan
else:
    "如果让我来做的话，会更有趣一点的吧......"
    jump fazhan
label fazhan:
    n "楠楠，怎么了"
    z "我要......"
    t "武不疯的脸上很快便露出了不耐烦的神情"
    "啊，他肯定不是很喜欢小孩......"
if kindness >= 1:
    "杀掉一个小孩吗......有点艰难"
    jump fazhan2
else:
    
    jump fazhan2
label fazhan2:
menu:

    "把她带走":
        jump baozou

    "这场面还挺有趣":
        jump budong

label baozou:
    
    $ kindness = kindness + 1
    call screen simple_screen
 


    "你从墙角中冒出来"
   
    e "先生，我带张楠楠出去吧"
    m "以后叫我老爷，别叫先生！"
    e "是"
    "你牵着张楠楠的手，准备带她出去"
    "这还真把自己当成大人物了......"
    m "等一下！"with vpunch
    "你回过头"
    e "怎么了？老爷"
    m "......哦，没事，你走吧"
    e "是"

    jump end

label budong:

    "武不疯眼中不耐烦随着他的隐忍而消失，他深吸一口气，对着张楠楠，蹲了下来"
    m "楠楠，你先出去玩好不好啊。"
    z "我就要在这里玩！！"
    "八岁张楠楠一屁股坐在地上"
    z "呜呜呜呜......"
    t "武不疯的眼里闪烁着寒芒"
    "哦，这可不太妙......"
    n "楠楠，让那个哥哥陪你玩好不好？"
    z "好！"
    "......"
    t "你从墙角中站了出来，对武不疯和旁边的贺美丽报以优美的假笑"
    e "先生，我带张楠楠出去吧"
    m "以后叫我老爷，别叫先生！"
    e "是"
    "你牵着张楠楠的手，准备带她出去"
    "这还真把自己当成大人物了......"
    m "等一下！"with vpunch
    "你回过头"
    e "怎么了？老爷"
    m "......哦，没事，你走吧"
    e "是"  

    jump end

label end:
    
    scene huayuan
    with fade
    
    t "你牵着张楠楠来到了花园"
    "说实话，我从来这儿的第一天就想知道为什么他们家的花园建的这么大......"
    "你看了一眼院子里的小型瀑布，甚至张楠楠出生后她的父母为她建造了一个巨型的沙池"
    play music bird fadein 1.0
    p "告贞！"
    t "正在修剪灌木的邢青尧放下花艺剪刀"
    p "楠楠，你去那边玩好不好，那边有你最爱玩的小沙滩"
    z "好！"
    t "张楠楠跑开了"
    p "唉，这孩子多可怜，老爷和夫人都去世了"
    stop music fadeout 1.0

menu:

    "告诉她武不疯和贺美丽的话":
        jump gaosu

    "还是岔开这个话题吧":
        jump yinman
label gaosu:
    e "刚才我听到武不疯和贺美丽......."
    t "你将事情一五一十的告诉了邢青尧"
    p "什么？怎么是这样？"
    t "邢青尧惊讶的大喊，看了看正在不远处玩的张楠楠，非常气愤"
    p "我早就知道，这两人绝对不是什么好货色......"
    jump endbad
label yinman:
    e "新来的老爷和夫人人都挺好的"
    p "是吗？我怎么听说......"
    e "都是些传言罢了"
    t "你打断她的话"
    p "......好吧"
    t "邢青尧跟你道了别，去照看张楠楠了"
    
    jump endgood
    
label endbad:
    p "我现在就去找他们！"
    e "别！"
    "你叫住邢青尧"
    e "还是先照顾好张楠楠，到时候再静观其变吧。"
    p "......好吧"
    t "邢青尧跟你道了别，去照看张楠楠了"
    jump wubufeng

label endgood:
    "现在......"
    "你思考了一下，决定先去探探这家的\"新主人\"的情况"
menu:
    "去找武不疯":
        jump wubufeng
    
    "去找贺美丽":
        jump hemeili
    
label wubufeng:
    scene shufang
    with fade
   
    "你来到了武不疯的书房"
    e"老爷"
    "你轻轻叩门"
    m"哦？进来，怎么了"
    e"我......"
    "你还没有说话，武不疯就开口了"
    m"哼，不用说了。多少钱？"
    e"......"
    "我想他一定是误会了什么......"
    t "武不疯掏出一张五百元的支票递给你"
    m "拿去吧"
menu:
    "那我可就收下了":
        jump jieshoule
       
    
    "就这么一点？":
        jump bishi
    
    "我不收你的钱":
        jump bushouqian
    "收下,然后烧了":
        jump shaole
label bushouqian:    
    "你并没有收"
    m "哦？难道这还不够多吗？"
    "武不疯直勾的看向你"
    "你并没有动"
    e "我不要钱"
    
    m"哦？那你想怎么样？"
menu:
    "我们两个人平分500万":
        jump xiee
    "我是不会放任你谋害张楠楠的":
        jump zhengyi
label jieshoule:
    $ kindness = kindness - 1
    e "那我就不客气了......"
    "你笑眯眯的接下500元的支票，察觉到了武不疯脸上的一丝抽搐"
    t "{color=#1e90ff}金钱+500{/color}"
    $ money = 500
    e "那，我就先走一步"
    "......"
    t "序章完"
    jump zhangjiexuanze2
    $ xuzhangjiejv = 1
label xiee:
    $ kindness = kindness - 1
    call screen simp_screen
label bishi:
    m "呵，你的胃口还挺大。"
label shaole:
    "武不疯突然掏出枪，瞄准了你"
if kindness >= 1:
    e "哦？你这是要......"
    m "现在解决掉你就好了"
    t "武不疯扣下扳机"with vpunch
    play sound shotting
    t "你灵敏的躲过了，迅速飞身上前抓住武不疯的手"
    t "你和武不疯扭打在一起，武不疯的枪滑落在远处"with vpunch
    t "此时，贺美丽闯入了房间"
    n "啊！！！！"with vpunch
    t "贺美丽晕倒在地"
    m "真没用！！"
    t "武不疯愤怒的大叫"
    t "武不疯挣脱开你，随手拿起桌上的小型雕像，对着你狠狠的砸了下去"
    scene heian
    m "好好睡一觉吧"
    "......"
    $ xuzhangjiejv = 2
    "序章完"
    jump zhangjiexuanze2
    
else:
    jump ending0
    
label ending0:
    e "哦？你这是要......"
    m "现在解决掉你就好了"
    t "武不疯扣下扳机"with vpunch
    play sound shotting
    $ renpy.block_rollback()  
    t "你死了"
    $ ending0 = True
    "{color=#f00}结局E01：简单的死亡,没有一人追忆{/color}"
    jump huamian
label zhengyi:
    $ kindness = kindness + 1
    call screen simple_screen
    "你直接退出了书房"
menu:
    "准备晚餐":
        jump wancan
    "去找贺美丽":
        jump hemeili

label wancan:
    scene heian
    t "你来到厨房"
    "序章完"
    $ xuzhangjiejv = 3
    jump zhangjiexuanze2
label hemeili:
    scene keting
    with fade
    t "你没有找到贺美丽"
    "算了，没事干，去准备晚餐吧......"
    jump wancan

    # 此处显示各行对话。

    e ""

    e ""
label xingqingyao:
    

       
    
    "此章节本月仅仅对会员开放，您可以在爱发电上赞助我成为会员！"
    jump xuanzezhangjie
    t ""
    
    t ""
    t ""
    t ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""

label huiyuanbikan:
    "如果您在爱发电上赞助了我，请密切关注我在爱发电平台上新发布的内容"
    "另外，由于本人原因，番外可能会晚一点更新，请见谅（最迟一个月内）"
    jump xuanzezhangjie
    # 此处为游戏结尾。

label zhangjiexuanze2:

menu:
    "进入第一章（注意及时存档）":
        jump diyizhang
    "重玩序章":
        jump xumu
    "游玩 番外：邢青尧的告白":
        jump xingqingyao


label diyizhang:
label huamian:
    return

