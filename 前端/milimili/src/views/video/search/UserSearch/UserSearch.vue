<template>
    <search></search>
    <div class="Userclass">
        <div class="Userclass-grid">
            <div class="UserClass defaultclass">
                <a class="Userclassfond defaultfond" href="/search/user/default">默认排序</a>
            </div>
            <div class="UserClass downclass">
                <a class="Userclassfond downfond" href="/search/user/down">粉丝数由高到低</a>
            </div>
            <div class="UserClass upclass">
                <a class="Userclassfond upfond" href="/search/user/up">粉丝数由低到高</a>
            </div>
        </div>
    </div>
</template>
<style>
.userfont {
    color: deepskyblue;
    text-decoration: underline;
    text-decoration-color: deepskyblue;
    text-decoration-thickness: 5px;
    text-underline-offset: 20px;
}

.Userclass {
    height: 80px;
}

.Userclass-grid {
    display: grid;
    grid-template-columns: auto auto auto;
    margin-left: 2%;
    margin-top: 1%;
    font-size: 20px;
    width: 700px;
}

.Userclassfond {
    text-decoration: none;
    color: #606266;
}

.UserClass {
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