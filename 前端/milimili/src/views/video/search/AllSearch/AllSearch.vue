<template>
    <Search></Search>
    <div class="allclass">
        <div class="allclass-grid">
            <div class="allClass zongheclass">
                <a class="allclassfond zonghefond" href="/search/all/all">综合排序</a>
            </div>
            <div class="allClass maxclickclass">
                <a class="allclassfond maxclickfond" href="/search/all/maxclick">最多点击</a>
            </div>
            <div class="allClass newestclass">
                <a class="allclassfond newestfond" href="/search/all/newest">最新发布</a>
            </div>
        </div>
    </div>
</template>
<style>
.allfont {
    color: deepskyblue;
    text-decoration: underline;
    text-decoration-color: deepskyblue;
    text-decoration-thickness: 5px;
    text-underline-offset: 20px;
}

.allclass {
    height: 80px;
}

.allclass-grid {
    display: grid;
    grid-template-columns: auto auto auto;
    margin-left: 2%;
    margin-top: 1%;
    font-size: 20px;
    width: 700px;
}

.allclassfond {
    text-decoration: none;
    color: #606266;
}

.allClass {
    margin-left: 15%;
    margin-right: 15%;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
<script>
import Search from "../SearchComponent.vue"
export default {
    components: {
        Search
    }
}
</script>