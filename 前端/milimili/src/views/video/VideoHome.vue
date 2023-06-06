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
                <el-input v-model="input" size="large" placeholder="Please input" @keyup.enter="submitData">
                    <template #append>
                        <el-button type="primary" icon="Search" circle @click="submitData"></el-button>
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
                    </router-link><router-link to="../../personal/upload">
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
                <el-carousel class="video-el-carousel" height="480px">
                    <el-carousel-item v-for="item in imgs">
                        <router-link :to="item.href"><img class="img3" :src="item.src"></router-link>
                    </el-carousel-item>
                </el-carousel>
            </div>
            <div class="rightvideo">
                <div class="rightvideo-grid">
                    <div v-for="video in  videos1 " class="rightvideo-container">
                        <video class="video" :id="video.id" @mouseenter="videoPlay(video.id)"
                            @mouseleave="videoPause(video.id)" @click="directToDetail(video.id)" muted="muted">
                            <source type="video/mp4" v-bind:src="video.src">
                        </video>
                        <div class="videoTitle">
                            <a class="videoTitlefond" :href="video.src">
                                {{ video.title }}
                            </a>
                        </div>
                        <div class="videoAuthor">
                            <a class="videoAuthorfond" :href="video.src">
                                {{ video.author }}
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="videoNVGT2">
        <div class="video-grid2">
            <div v-for="video in  videos2 " class="rightvideo-container">
                <video class="video" :id="video.id" @mouseenter="videoPlay(video.id)" @mouseleave="videoPause(video.id)"
                    @click="directToDetail(video.id)" muted="muted">
                    <source type="video/mp4" v-bind:src="video.src">
                </video>
                <div class="videoTitle">
                    <a class="videoTitlefond" :href="video.src">
                        {{ video.title }}
                    </a>
                </div>
                <div class="videoAuthor">
                    <a class="videoAuthorfond" :href="video.src">
                        {{ video.author }}
                    </a>
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
    margin-left: 2%;
    margin-right: 2%;
}

.leftheader-grid {
    display: grid;
    grid-template-columns: auto auto auto;
    font-size: large;
}

.leftheader {
    transform: translateY(8%);
}

.fonthead {
    text-decoration: none;
    color: white;
}

/* .fonthead:hover {
    text-decoration: underline;
} */

.rightheader-grid {
    display: grid;
    grid-template-columns: auto auto auto auto auto;
}

.img1 {
    transform: translateY(-20%);
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
    height: 80px;
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
    height: 650px;
    transform: translateY(50px);
}

.video-grid1 {
    display: grid;
    grid-template-columns: auto auto;
    margin-left: 6%;
    margin-right: 6%;
}

.leftvideo {
    height: 480px;
    width: 800px;
}

.video-el-carousel {
    border-radius: 4%;
}

.img3 {
    width: 800px;
    height: 480px;
    border-radius: 4%;
}

.rightvideo-grid {
    display: grid;
    grid-template-columns: auto auto auto auto;

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

.videoTitle {
    width: 320px;
    margin-left: 20px;
    text-align: left;
    height: 48px;

}

.videoAuthor {
    width: 320px;
    margin-left: 20px;
    text-align: left;

}

.videoTitlefond {
    font-size: 18px;
}

.videoTitlefond:hover {
    color: rgb(49, 117, 196);
}

.videoAuthorfond:hover {
    color: rgb(49, 117, 196);
}

.videoNVGT2 {
    height: 800px;

}

.video-grid2 {
    display: grid;
    grid-template-columns: auto auto auto auto auto auto;

    margin-left: 5%;
    margin-right: 5%;
}
</style>
<script>
import { mapActions, mapState } from "vuex";
export default {
    data() {
        return {
            videos1: [
                {
                    id: 'video1-1',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video1-2',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video1-3',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video1-4',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video1-5',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video1-6',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video1-7',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video1-8',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转',
                    author: '123'
                }
            ],
            imgs: [
                {
                    id: 'leftimg1',
                    src: require('../../assets/img/V.png'),
                    href: 'home'
                },
                {
                    id: 'leftimg2',
                    src: require('../../assets/login.jpg'),
                    href: '../../personal'
                },
                {
                    id: 'leftimg3',
                    src: require('../../assets/img/V.png'),
                    href: '../../about'
                }

            ],
            videos2: [
                {
                    id: 'video2-1',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video2-2',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video2-3',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video2-4',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video2-5',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转',
                    author: '123'
                },
                {
                    id: 'video2-6',
                    src: require('../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转旋转',
                    author: '123'
                },

            ],
            input: '',
        }
    },
    methods: {
        videoPlay(id) {
            console.log(id);
            // for (var i = 0; i < this.videos.length; i++) {
            //     if (id == this.videos[i].id) {
            //         console.log(this.videos[i].src);
            //     }
            // }

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
        },
        ...mapActions(['updateSearchInput']),
        submitData() {
            this.updateSearchInput(this.input);
            console.log(this.input);
            console.log(this.searchinput);
            if (this.input.trim() !== '') {
                this.$router.push({ path: '/search/video/all', query: { input: this.input } })

            }

        }
    },
    computed: {
        ...mapState(['searchinput'])
    }

}
</script>