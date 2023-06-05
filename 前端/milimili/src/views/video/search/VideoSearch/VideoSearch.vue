<template>
    <Search></Search>
    <div class="Videoclass">
        <div class="Videoclass-grid">
            <div class="VideoClass zongheclass">
                <a class="Videoclassfond zonghefond" href="/search/video/all">综合排序</a>
            </div>
            <div class="VideoClass maxlikeclass">
                <a class="Videoclassfond maxlikefond" href="/search/video/maxlike">最多点赞</a>
            </div>
            <div class="VideoClass newestclass">
                <a class="Videoclassfond newestfond" href="/search/video/newest">最新发布</a>
            </div>
        </div>
    </div>
</template>
<style>
.videofont {
    color: deepskyblue;
    text-decoration: underline;
    text-decoration-color: deepskyblue;
    text-decoration-thickness: 5px;
    text-underline-offset: 20px;

}

.Videoclass {
    height: 80px;
    margin-left: 2%;
}

.Videoclass-grid {
    display: grid;
    grid-template-columns: auto auto auto;
    margin-left: 2%;
    margin-top: 1%;
    font-size: 20px;
    width: 700px;
}

.Videoclassfond {
    text-decoration: none;
    color: #606266;
}

.VideoClass {
    margin-left: 15%;
    margin-right: 15%;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
<script>
import Search from '../SearchComponent.vue'
export default {
    components: {
        Search
    }
}
</script>