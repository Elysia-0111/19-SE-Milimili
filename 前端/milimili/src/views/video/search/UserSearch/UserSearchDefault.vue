<template>
    <UserSearch></UserSearch>
    <Usercomponent></Usercomponent>
</template>
<style>
.defaultclass {
    background-color: rgb(228, 245, 255);
    border-radius: 8%;
}

.defaultfond {
    color: deepskyblue;
    text-decoration: none;
}
</style>
<script>
import UserSearch from './UserSearch.vue';
import Usercomponent from '../Usercomponent.vue';
export default {
    components: {
        UserSearch, Usercomponent
    },
    mounted() {
        if (!sessionStorage.getItem('pageRefreshed')) {
            sessionStorage.setItem('pageRefreshed', 'true');
            window.history.replaceState({}, '', window.location.href); // 替换当前页面 URL
            location.reload(); // 刷新页面
        } else {
            sessionStorage.removeItem('pageRefreshed');
        }
    }
}
</script>