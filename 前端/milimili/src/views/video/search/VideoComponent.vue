<template>
    <div class="videoclass">
        <div class="videoclass-grid">
            <div v-for="video in videos" class="videocontainer">
                <div class="video-grid">
                    <video class="video" :id="video.id" @mouseenter="videoPlay(video.id)" @mouseleave="videoPause(video.id)"
                        @click="directToDetail(video.id)" muted="muted">
                        <source type="video/mp4" v-bind:src="video.src">
                    </video>
                    <div class="titlecontainer">
                        <div class="title-grid">
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
                <!-- <div>1</div>
                <div>1</div> -->
            </div>
        </div>
    </div>
</template>
<style>
.videoclass {
    display: flex;
    margin-left: 4%;
    margin-right: 4%;
}

.videoclass-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
    grid-auto-rows: 240px;

}

/* .videoclass-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
    grid-auto-rows: 240px;
} */
@media (max-width:1000px) {
    .videoclass-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        grid-auto-rows: 240px;
    }
}

@media (min-width:1000px) and (max-width:1600px) {
    .videoclass-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
        grid-auto-rows: 240px;
    }
}

@media (min-width:2000px) {
    .videoclass-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
        grid-auto-rows: 240px;
    }
}

/* .videocontainer {
    height: 75%;
} */

.videocontainer video {
    width: 95%;
    height: 95%;
    object-fit: cover;
    border-radius: 4%;
}

.title-grid {
    display: grid;
    grid-template-rows: 2fr 1fr;
    height: 100%;
}

.videocontainer a {
    text-decoration: none;
}

.video-grid {
    display: grid;
    grid-template-rows: 2fr 1fr;
    height: 100%;
    margin-right: 5%;
    text-align: left;
}

.videoTitlefond {
    color: black;
}

.videoTitlefond:hover {
    color: deepskyblue;
}

.videoAuthorfond {
    color: #909399;
}

.videoAuthorfond:hover {
    color: deepskyblue;
}
</style>
<script>
export default {
    data() {
        return {
            videos: [
                {
                    src: require('../../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转',
                    author: '123',
                    id: 'video1'
                },
                {
                    src: require('../../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转',
                    author: '123',
                    id: 'video2'
                },
                {
                    src: require('../../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转',
                    author: '123',
                    id: 'video3'
                },
                {
                    src: require('../../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转',
                    author: '123',
                    id: 'video4'
                },
                {
                    src: require('../../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转',
                    author: '123',
                    id: 'video5'
                },
                {
                    src: require('../../../assets/video/test.mp4'),
                    title: '旋转旋转旋转旋转旋转',
                    author: '123',
                    id: 'video6'
                },

            ]
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
        }
    },

}
</script >
