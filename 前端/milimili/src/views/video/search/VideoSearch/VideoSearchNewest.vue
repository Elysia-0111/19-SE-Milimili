<template>
    <VideoSearch></VideoSearch>
    <VideoComponent></VideoComponent>
</template>
<style>
.newestclass {
    background-color: rgb(228, 245, 255);
    border-radius: 8%;
}

.newestfond {
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
    }
}
</script >