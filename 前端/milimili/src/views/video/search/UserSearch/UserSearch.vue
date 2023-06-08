<template>
    <Search></Search>
    <div class="Userclass">
        <div class="Userclass-grid">
            <div class="UserClass defaultclass">
                <a class="Userclassfond defaultfond" :href="getDefaultHref">默认排序</a>
            </div>
            <div class="UserClass downclass">
                <a class="Userclassfond downfond" :href="getDownHref">粉丝数由高到低</a>
            </div>
            <div class="UserClass upclass">
                <a class="Userclassfond upfond" :href="getUpHref">粉丝数由低到高</a>
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
import Search from '../SearchComponent.vue'
import { mapState, mapActions } from "vuex";
export default {
    components: {
        Search
    },
    computed: {
        ...mapState(['searchinput']),
        getDefaultHref() {
            let query = {};
            if (this.searchinput !== this.input) {
                query = { input: this.searchinput };
            } else {
                query = { input: this.input };
            }

            const route = {
                path: '/search/user/default',
                query
            }
            // console.log(this.$route.resolve(route).href)
            return this.$router.resolve(route).href;
        },
        getDownHref() {
            let query = {};
            if (this.searchinput !== this.input) {
                query = { input: this.searchinput };
            } else {
                query = { input: this.input };
            }
            const route = {
                path: '/search/user/down',
                query
            }
            // console.log(this.$route.resolve(route).href)
            return this.$router.resolve(route).href;
        },
        getUpHref() {
            let query = {};
            if (this.searchinput !== this.input) {
                query = { input: this.searchinput };
            } else {
                query = { input: this.input };
            }
            const route = {
                path: '/search/user/up',
                query
            }
            // console.log(this.$route.resolve(route).href)
            return this.$router.resolve(route).href;
        },

    }, created() {
        this.updateSearchInput(this.$route.query.input || '');

    },
    methods: {
        ...mapActions(['updateSearchInput'])
    }
}
</script>