<template>
    <Search></Search>
    <div class="Videoclass">
        <div class="Videoclass-grid">
            <div class="VideoClass zongheclass">
                <a class="Videoclassfond zonghefond" :href="getAllHref">综合排序</a>
            </div>
            <div class="VideoClass maxlikeclass">
                <a class="Videoclassfond maxlikefond" :href="getMaxHref">最多点赞</a>
            </div>
            <div class="VideoClass newestclass">
                <a class="Videoclassfond newestfond" :href="getNewHref">最新发布</a>
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
import { mapState, mapActions } from 'vuex';
export default {
    components: {
        Search
    },
    computed: {
        ...mapState(['searchinput']),
        getAllHref() {
            let query = {};
            if (this.searchinput !== this.input) {
                query = { input: this.searchinput };
            } else {
                query = { input: this.input };
            }

            const route = {
                path: '/search/video/all',
                query
            }
            console.log(this.$router.resolve(route).href)
            return this.$router.resolve(route).href;
        },
        getMaxHref() {
            //console.log(this.input)
            let query = {};
            if (this.searchinput !== this.input) {
                query = { input: this.searchinput };
            } else {
                query = { input: this.input };
            }
            const route = {
                path: '/search/video/maxlike',
                query
            }
            return this.$router.resolve(route).href;
        },
        getNewHref() {
            //console.log(this.input)
            const query = { input: this.searchinput };
            const route = {
                path: '/search/video/newest',
                query
            }
            return this.$router.resolve(route).href;
        }
    },
    created() {
        this.updateSearchInput(this.$route.query.input || '');
    },
    methods: {
        ...mapActions(['updateSearchInput'])
    }

}
</script>