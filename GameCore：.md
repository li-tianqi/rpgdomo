GameCore：

- 显示场景
- 放音乐
- UI控制

class Stage

- scenePaint(scene)
- playMusic(music)
- collisionDetection(A, B, condition)
- controlDetection()
- sceneSwitch(scene)



场景中要显示的:

static: map, 事件组件

dynamica: 动态NPC,



角色



地图数据格式

width

height

(图片信息, img, x, y, w, h)

第一层: [[img, x, y, w, h]] (最底层大地图)

第二层: [[img1,x1,y1,w1,h1],[img2,x2,y2,w2,h2,]] (地图上静态覆盖物)

第三层: [[img,x,y,w,h]] (遮挡层,可半透明)

第四层: [[img,x,y,w,h]] (地形层,用黑色区域标识不可达区域)



map01数据:

wight: 800

height: 600

[

[('map01.png', 0, 0, 800, 600)],

[('npc01.png', 51, 64, -1, -1), ('baoxiang01', 100, 200, -1, -1), ('npc02.png', 160, 500, -1, -1)],

[('map01_cover.png', 0, 0, 800, 600)],

[('map01_coll.png', 0, 0, 800, 600)],

]