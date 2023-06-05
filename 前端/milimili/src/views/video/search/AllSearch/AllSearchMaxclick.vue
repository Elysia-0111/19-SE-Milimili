<template>
    <AllSearch></AllSearch>

    <VideoComponent v-if="this.videos != 0"></VideoComponent>

    <el-empty v-else :image-size="250" description="这里空空如也哦"></el-empty>
</template>
<style>
.maxclickclass {
    background-color: rgb(228, 245, 255);
    border-radius: 8%;
}

.maxclickfond {
    color: deepskyblue;
    text-decoration: none;
}
</style>
<script>
import AllSearch from './AllSearch.vue'
import VideoComponent from '../VideoComponent.vue';
export default {
    components: {
        AllSearch,
        VideoComponent
    },
    data() {
        return {
            videos: []
        }
    },
    mounted() {
        this.videos = VideoComponent.videos
    }
}
</script >
