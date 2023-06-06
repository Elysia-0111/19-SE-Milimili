<template>
    <VideoSearch></VideoSearch>
    <VideoComponent v-if="this.videos != 0"></VideoComponent>

    <el-empty v-else :image-size="250" description="这里空空如也哦"></el-empty>
</template>
<style>
.zongheclass {
    background-color: rgb(228, 245, 255);
    border-radius: 8%;
}

.zonghefond {
    color: deepskyblue;
    text-decoration: none;
}
</style>
<script>
import VideoSearch from './VideoSearch.vue';
import VideoComponent from '../VideoComponent.vue';
export default {
    components: {
        VideoSearch,
        VideoComponent
    },
    data() {
        return {
            videos: []
        }
    },
    mounted() {
        this.videos = VideoComponent.videos;
        if (!sessionStorage.getItem('pageRefreshed')) {
            sessionStorage.setItem('pageRefreshed', 'true');
            window.history.replaceState({}, '', window.location.href); // 替换当前页面 URL
            location.reload(); // 刷新页面
        } else {
            sessionStorage.removeItem('pageRefreshed');
        }
    }
}
</script >