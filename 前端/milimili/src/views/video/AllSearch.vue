<template>
    <Search></Search>
    <div class="allclass">
        <div class="allclass-grid">
            <div>
                <a>综合排序</a>
            </div>
            <div><a>最多点击</a></div>
            <div><a>最新发布</a></div>
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
    height: 400px;
}

.allclass-grid {
    display: grid;
    grid-template-columns: auto auto auto;
    margin-right: 60%;
    margin-top: 1%;
}
</style>
<script>
import Search from './Search.vue'
export default {
    components: {
        Search
    }
}
</script>