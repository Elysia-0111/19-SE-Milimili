<template>
    <div class="headerNVGT">
        <div class="header-grid">
            <div class="leftheader">
                <div class="leftheader-grid">
                    <!-- <router-link to="home"><span class="fonthead">首页</span></router-link>
                    <router-link to="home"><a class="fonthead">热门</a></router-link>
                    <router-link to="home"><a class="fonthead">频道</a></router-link> -->
                    <a class="fonthead" href="home">首页</a>
                    <a class="fonthead" href="home">热门</a>
                    <a class="fonthead" href="home">频道</a>
                </div>
            </div>
            <div class="middleheader">
                <el-input v-model="searchinput" size="large" placeholder="Please input">
                    <template #append>
                        <el-button type="primary" icon="Search" circle></el-button>
                    </template>
                </el-input>
            </div>
            <div class="rightheader">
                <div class="rightheader-grid">
                    <router-link to="../../personal">
                        <img class="img1" src="../../assets/头像.jpg">
                    </router-link>
                    <router-link to="home">
                        <el-icon class="icon-header">
                            <ChatLineSquare />
                        </el-icon>
                    </router-link>
                    <router-link to="../../personal/mycollect">
                        <el-icon class="icon-header">
                            <Collection />
                        </el-icon>
                    </router-link><router-link to="home">
                        <el-icon class="icon-header">
                            <VideoPlay />
                        </el-icon>
                    </router-link><router-link to="home">
                        <el-icon class="icon-header">
                            <Upload />
                        </el-icon>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
    <div class="partNVGT">
        <div class="part-grid">
            <div class="leftpart">
                <div class="leftpart-grid">
                    <a class="icon-img" href="home">
                        <div><img class="img2" src="../../assets/img/V.png" alt="lazy"></div>
                        <span class="icon-title">动态</span>
                    </a>
                    <a class="icon-img" href="home">
                        <div><img class="img2" src="../../assets/img/V.png" alt="lazy"></div>
                        <span class="icon-title">热门</span>
                    </a>
                    <a class="icon-img" href="home">
                        <div><img class="img2" src="../../assets/img/V.png" alt="lazy"></div>
                        <span class="icon-title">频道</span>
                    </a>
                </div>
            </div>
            <div class="middlepart">
                <div class="middlepart-grid">
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>番剧</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>国创</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>综艺</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>动画</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>鬼畜</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>舞蹈</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>娱乐</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>科技</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>美食</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>电影</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>电视剧</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>纪录片</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>游戏</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>音乐</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>影视</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>知识</el-button></a>
                    <a href="home"><el-button size="middle" type="default" class="button" text bg>资讯</el-button></a>
                    <a href="../../personal"><el-button size="middle" type="default" class="button" text
                            bg>更多</el-button></a>
                </div>
            </div>
            <div class="rightpart">
                here is something else
            </div>
        </div>
    </div>
    <div class="videoNVGT1">
        <div class="video-grid1">
            <div class="leftvideo">
                <img class="img3" src="../../assets/img/V.png">
            </div>
            <div class="rightvideo">
                <div class="rightvideo-grid">
                    <div class="rightvideo-container">
                        <video class="video" id="video1" @mouseenter="videoPlay('video1')"
                            @mouseleave="videoPause('video1')" @click="directToDetail(1)" muted="muted">
                            <source type="video/mp4" src="../../assets/video/测试.mp4">
                        </video>
                        <div class="videoTitle">
                            旋转旋转旋转
                        </div>
                    </div>
                    <div class="rightvideo-container">
                        <video class="video" id="video2" @mouseenter="videoPlay('video2')"
                            @mouseleave="videoPause('video2')" @click="directToDetail(1)" muted="muted">
                            <source type="video/mp4" src="../../assets/video/测试.mp4">
                        </video>
                        <div class="videoTitle">
                            旋转旋转旋转
                        </div>
                    </div>
                    <div class="rightvideo-container">
                        <video class="video" id="video3" @mouseenter="videoPlay('video3')"
                            @mouseleave="videoPause('video3')" @click="directToDetail(1)" muted="muted">
                            <source type="video/mp4" src="../../assets/video/测试.mp4">
                        </video>
                        <div class="videoTitle">
                            旋转旋转旋转
                        </div>
                    </div>
                    <div class="rightvideo-container">
                        <video class="video" id="video4" @mouseenter="videoPlay('video4')"
                            @mouseleave="videoPause('video4')" @click="directToDetail(1)" muted="muted">
                            <source type="video/mp4" src="../../assets/video/测试.mp4">
                        </video>
                        <div class="videoTitle">
                            旋转旋转旋转
                        </div>
                    </div>
                    <div class="rightvideo-container">
                        <video class="video" id="video5" @mouseenter="videoPlay('video5')"
                            @mouseleave="videoPause('video5')" @click="directToDetail(1)" muted="muted">
                            <source type="video/mp4" src="../../assets/video/测试.mp4">
                        </video>
                        <div class="videoTitle">
                            旋转旋转旋转
                        </div>
                    </div>
                    <div class="rightvideo-container">
                        <video class="video" id="video6" @mouseenter="videoPlay('video6')"
                            @mouseleave="videoPause('video6')" @click="directToDetail(1)" muted="muted">
                            <source type="video/mp4" src="../../assets/video/测试.mp4">
                        </video>
                        <div class="videoTitle">
                            旋转旋转旋转
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
a {
    text-decoration: none;
    color: black;
}

.headerNVGT {
    height: 150px;
    background-image: url("../../assets/img/background.jpg");
}

.header-grid {
    display: grid;
    grid-template-columns: 2fr 3fr 3fr;
    grid-gap: 150px 150px;

    padding: 10px;
    transform: translateY(20%);
}

.leftheader-grid {
    display: grid;
    grid-template-columns: auto auto auto;
    font-size: large;
}

.leftheader {
    transform: translateY(8%);
    color: white;
}

.fonthead {
    text-decoration: none;
    color: white;
}

.fonthead:hover {
    text-decoration: underline;
}

.rightheader-grid {
    display: grid;
    grid-template-columns: auto auto auto auto auto;
}

.img1 {
    transform: translateY(-10%);
    width: 50px;
    height: 50px;

    border-radius: 50%;
}

.icon-header {
    color: white;
    font-size: 24px;
}

.icon-header:hover {
    color: wheat;
}

.partNVGT {
    height: 100px;
    transform: translateY(20%);
}

.part-grid {
    display: grid;
    grid-template-columns: auto auto auto;
    margin-left: 4%;
}


.leftpart-grid {
    display: grid;
    grid-template-columns: auto auto auto;

}

.img2 {
    /* transform: translateY(-15%); */
    width: 50px;
    height: 50px;

    border-radius: 50%;
}

.middlepart-grid {
    display: grid;
    grid-template-columns: auto auto auto auto auto auto auto auto auto;
    grid-row-gap: 10px;
}

.button {
    width: 68px;
    font-size: 18px;
}

.videoNVGT1 {
    height: 400px;
    transform: translateY(50px);
}

.video-grid1 {
    display: grid;
    grid-template-columns: auto auto;
    grid-gap: 40px;
}

.img3 {
    width: 640px;
    height: 480px;
}

.rightvideo-grid {
    display: grid;
    grid-template-columns: auto auto auto;

}

.rightvideo-container {
    border-radius: 20%;
    width: 360px;
    height: 280px;
}

.video {
    border-radius: 12%;
    width: 320px;
    height: 200px;

}
</style>
<script>
export default {
    methods: {
        videoPlay(id) {
            console.log(id);
            var video = document.getElementById(id);
            video.setAttribute("autoplay", "autoplay");
            video.setAttribute("loop", "loop");
            var play;
            play = video.play();
            if (play) {
                play.then(() => {
                    // 视频频加载成功
                    // 视频频的播放需要耗时
                    setTimeout(() => {
                        // 后续操作
                        console.log("done.");
                    }, video[0].duration * 1000); // video[0].duration 为视频频的时长，单位为秒


                }).catch((e) => {
                    // 视频频加载失败
                })
            }
        },
        videoPause(id) {
            var video = document.getElementById(id);
            video.currentTime = 0;
            video.pause();
        },
        directToDetail(id) {
            this.$router.push('../../personal');
            // TODO
        }
    }
}
</script>