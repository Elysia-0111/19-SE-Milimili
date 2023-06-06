<template>
    <div class="headerNVGT">
        <div class="header-grid">
            <div class="leftheader">
                <div class="leftheader-grid">
                    <!-- <router-link to="home"><span class="fonthead">首页</span></router-link>
                    <router-link to="home"><a class="fonthead">热门</a></router-link>
                    <router-link to="home"><a class="fonthead">频道</a></router-link> -->
                    <a class="fonthead" href="/home">首页</a>
                    <a class="fonthead" href="home">热门</a>
                    <a class="fonthead" href="home">频道</a>
                </div>
            </div>
            <div class="rightheader">
                <div class="rightheader-grid">
                    <router-link to="../../personal">
                        <img class="img1" src="../../../assets/头像.jpg">
                    </router-link>
                    <router-link to="home">
                        <el-icon class="icon-header">
                            <ChatLineSquare />
                        </el-icon>
                    </router-link>
                    <router-link to="../../personal/mycollect">
                        <el-icon class="icon-header">
                            <Collection />
                        </el-icon>
                    </router-link><router-link to="home">
                        <el-icon class="icon-header">
                            <VideoPlay />
                        </el-icon>
                    </router-link><router-link to="../../personal/upload">
                        <el-icon class="icon-header">
                            <Upload />
                        </el-icon>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
    <div class="search">
        <div class="search-grid">
            <el-input v-model="input" size="large" :placeholder="placeholder" clearable @keyup.enter="submitData"
                @input="handleInput(input)">
                <template #prefix>
                    <el-icon class="el-input__icon" style="color: rgb(35, 130, 204);">
                        <search />
                    </el-icon>
                </template>
            </el-input>
            <el-button type="primary" size="large" @click="submitData">搜索</el-button>
        </div>
        <!-- <div>{{ $route.query.input }}</div> -->
    </div>
    <div class="classification">
        <div class="class-grid">
            <!-- <div><a class="classfont allfont" href="/search/all/all">综合</a></div> -->
            <div><a class="classfont videofont" :href="getVideoHref">视频</a></div>
            <div><a class="classfont userfont" :href="getUserHref">用户</a></div>
        </div>
    </div>
</template>
<style>
.headerNVGT {
    height: 80px;
    box-shadow: 0px 5px 5px #E6E8EB;
}

.header-grid {
    display: grid;
    grid-template-columns: 2fr 3fr;
    grid-gap: 50%;

    padding: 10px;
    transform: translateY(20%);
    margin-left: 2%;
    margin-right: 2%;
}

.leftheader-grid {
    display: grid;
    grid-template-columns: auto auto auto;
    font-size: large;
}

.leftheader {
    transform: translateY(8%);
}

.fonthead {
    text-decoration: none;
    color: black;
}

.fonthead:hover {
    animation: up-down 0.4s ease-in-out;
}

.rightheader-grid {
    display: grid;
    grid-template-columns: auto auto auto auto auto;
}

.img1 {
    transform: translateY(-20%);
    width: 50px;
    height: 50px;
    border-radius: 50%;
}

.icon-header {
    color: black;
    font-size: 24px;
}

.icon-header:hover {
    /* transform: translateY(-20%); */
    animation: up-down 0.4s ease-in-out;

}

@keyframes up-down {
    0% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-10px);
    }

    100% {
        transform: translateY(0);
    }
}

.search {
    height: 50px;
    margin-left: 30%;
    margin-right: 30%;
    margin-top: 1%;
}

.search-grid {
    display: grid;
    grid-template-columns: 10fr 1fr;
}

.classification {
    margin-top: 1%;
    height: 50px;
    box-shadow: 0px 1px 1px #E6E8EB;
}

.class-grid {
    display: grid;
    grid-template-columns: auto auto;
    margin-right: 60%;
    font-size: 25px;
}

.classfont {
    text-decoration: none;
    color: #A8ABB2;
}

.classfont:hover {
    color: deepskyblue;
}
</style>

<script>
import { mapActions, mapState } from 'vuex';
export default {
    data() {
        return {
            input: null
        }
    },
    computed: {
        ...mapState(['searchinput']),

        getVideoHref() {
            const query = { input: this.input };
            const route = {
                path: '/search/video/all',
                query
            }
            return this.$router.resolve(route).href;
        },
        getUserHref() {
            const query = { input: this.input };
            const route = {
                path: '/search/user/default',
                query
            }
            return this.$router.resolve(route).href;
        },
    },
    methods: {
        ...mapActions(['updateSearchInput']),
        submitData() {
            this.updateSearchInput(this.input);
            // console.log(this.input);
            // console.log(this.searchinput)
            if (this.input.trim() !== '') {
                this.$router.push({ path: this.$route.path, query: { input: this.input } })
            }

        },
        handleInput(value) {
            this.updateSearchInput(value);
            //console.log(this.searchinput)
        }
    },
    created() {
        this.input = this.$route.query.input || '';
    }

}
</script>