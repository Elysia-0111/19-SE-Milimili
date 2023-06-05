<template>
    <UserSearch></UserSearch>
    <Usercomponent></Usercomponent>
</template>
<style>
.upclass {
    background-color: rgb(228, 245, 255);
    border-radius: 8%;
}

.upfond {
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
    }
}
</script>