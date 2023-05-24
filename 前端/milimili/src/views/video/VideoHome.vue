<template>
    <div>
        <el-container class="videohome">
            <el-header class="header">
                <el-row>
                    <el-col :span="1" :offset="1"><router-link to="home">首页</router-link></el-col>
                    <el-col :span="1"><router-link to="home">热门</router-link></el-col>
                    <el-col :span="1"><router-link to="home">频道</router-link></el-col>
                    <el-col :span="6" :offset="3">
                        <el-input v-model="searchinput" size="small" placeholder="Please input">
                            <template #append>
                                <el-button type="primary" icon="Search" circle></el-button>
                            </template>
                        </el-input>
                    </el-col>
                    <el-col :span="3" :offset="3"><router-link to="../../personal">
                            <img class="img1" src="../../assets/头像.jpg">
                        </router-link>
                    </el-col>
                    <el-col :span="1"><router-link to="home">
                            <el-icon color=white size="24">
                                <ChatLineSquare />
                            </el-icon>
                        </router-link>
                    </el-col>
                    <el-col :span="1"><router-link to="../../personal/mycollect">
                            <el-icon color=white size="24">
                                <Collection />
                            </el-icon>
                        </router-link>
                    </el-col>
                    <el-col :span="1"><router-link to="home">
                            <el-icon color=white size="24">
                                <VideoPlay />
                            </el-icon>
                        </router-link>
                    </el-col>
                    <el-col :span="1"><router-link to="home">
                            <el-icon color=white size="24">
                                <Upload />
                            </el-icon>
                        </router-link>
                    </el-col>
                </el-row>

            </el-header>
            <el-main>
                <div class="channel-icons">
                    <a class="channel-icons1" href="home">
                        <div class="icon-img">
                            <picture class="icon-img-pic">
                                <img class="img2" src="../../assets/img/V.png" alt="lazy">
                            </picture>
                        </div>
                        <span class="icon-title">动态</span>
                    </a>
                    <a class="channel-icons2" href="home">
                        <div class="icon-img">
                            <picture class="icon-img-pic">
                                <img class="img2" src="../../assets/img/V.png" alt="lazy">
                            </picture>
                        </div>
                        <span class="icon-title">热门</span>
                    </a>
                    <a class="channel-icons3" href="home">
                        <div class="icon-img">
                            <picture class="icon-img-pic">
                                <img class="img2" src="../../assets/img/V.png" alt="lazy">
                            </picture>
                        </div>
                        <span class="icon-title">频道</span>
                    </a>
                </div>
                <div class="relative-container">
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button1" text bg>番剧</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button2" text bg>电影</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button3" text bg>国创</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button4" text bg>电视剧</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button5" text bg>综艺</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button6" text bg>纪录片</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button7" text bg>动画</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button8" text bg>游戏</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button9" text bg>鬼畜</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button10" text bg>音乐</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button11" text bg>舞蹈</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button12" text bg>影视</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button13" text bg>娱乐</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button14" text bg>知识</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button15" text bg>科技</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button16" text bg>资讯</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button17" text bg>美食</el-button>
                    </a>
                    <a class="channel-link" href="home" style="letter-spacing: 2px;" target="_blank">
                        <el-button size="small" type="default" class="button18" text bg>更多</el-button>
                    </a>
                </div>
            </el-main>
        </el-container>
    </div>
</template>
<style>
.header {
    width: auto;
    height: 150px;

    background-image: url("../../assets/img/background.jpg");
}

.router-link-active {
    text-decoration: none;
    color: wheat;
    font-size: large;
}

a {
    text-decoration: none;
    color: black;
}

.el-row {
    transform: translateY(50%);
}

.img1 {
    transform: translateY(-30%);
    width: 50px;
    height: 50px;

    border-radius: 50%;
}

.channel-icons1 {
    position: absolute;
    left: 3.5%;
    top: 250px;
    display: block;
}

.channel-icons2 {
    position: absolute;
    left: 8.5%;
    display: block;
    top: 250px;
}

.channel-icons3 {
    position: absolute;
    left: 13.5%;
    top: 250px;
}

.img2 {
    transform: translateY(-15%);
    width: 37px;
    height: 37px;

    border-radius: 50%;
}

.relative-container {

    position: absolute;
    left: 18.5%;
    top: 245px;
    height: 70px;
    width: max-content;
}

.button1 {
    width: 68px;
    position: relative;
    left: 0;
    top: 0;
}

.button2 {
    width: 68px;
    position: relative;
    left: -68px;
    top: 35px;
}

.button3 {
    width: 68px;
    position: relative;
    left: -50px;
    top: 0;
}

.button4 {
    width: 68px;
    position: relative;
    left: -118px;
    top: 35px;
}

.button5 {
    width: 68px;
    position: relative;
    left: -100px;
    top: 0;
}

.button6 {
    width: 68px;
    position: relative;
    left: -168px;
    top: 35px;
}

.button7 {
    width: 68px;
    position: relative;
    left: -150px;
    top: 0;
}

.button8 {
    width: 68px;
    position: relative;
    left: -218px;
    top: 35px;
}

.button9 {
    width: 68px;
    position: relative;
    left: -200px;
    top: 0;
}

.button10 {
    width: 68px;
    position: relative;
    left: -268px;
    top: 35px;
}

.button11 {
    width: 68px;
    position: relative;
    left: -250px;
    top: 0;
}

.button12 {
    width: 68px;
    position: relative;
    left: -318px;
    top: 35px;
}

.button13 {
    width: 68px;
    position: relative;
    left: -300px;
    top: 0;
}

.button14 {
    width: 68px;
    position: relative;
    left: -368px;
    top: 35px;
}

.button15 {
    width: 68px;
    position: relative;
    left: -350px;
    top: 0;
}

.button16 {
    width: 68px;
    position: relative;
    left: -418px;
    top: 35px;
}

.button17 {
    width: 68px;
    position: relative;
    left: -400px;
    top: 0;
}

.button18 {
    width: 68px;
    position: relative;
    left: -468px;
    top: 35px;
}
</style>

<script>
</script>
