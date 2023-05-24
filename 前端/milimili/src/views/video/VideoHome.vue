<template>
    <div>
        <el-container class="videohome">
            <el-header class="header">
                <el-row>
                    <el-col :span="1"><router-link to="home">首页</router-link></el-col>
                    <el-col :span="1"><router-link to="home">热门</router-link></el-col>
                    <el-col :span="1"><router-link to="home">频道</router-link></el-col>
                    <el-col :span="6" :offset="3">
                        <el-input v-model="searchinput" size="small" placeholder="Please input">
                            <template #append>
                                <el-button type="primary" icon="Search" circle></el-button>
                            </template>
                        </el-input>
                    </el-col>
                    <el-col :span="3" :offset="3"><router-link to="home">
                            <img src="../../assets/头像.jpg">
                        </router-link>
                    </el-col>
                    <el-col :span="1"><router-link to="home">
                            <el-icon color=white size="24">
                                <ChatLineSquare />
                            </el-icon>
                        </router-link>
                    </el-col>
                    <el-col :span="1"><router-link to="home">
                            <el-icon color=white size="24">
                                <Collection />
                            </el-icon>
                        </router-link>
                    </el-col>
                    <el-col :span="1"><router-link to="home">
                            <el-icon color=white size="24">
                                <VideoPlay />
                            </el-icon>
                        </router-link>
                    </el-col>
                    <el-col :span="1"><router-link to="home">
                            <el-icon color=white size="24">
                                <Upload />
                            </el-icon>
                        </router-link>
                    </el-col>
                </el-row>
            </el-header>
        </el-container>
    </div>
</template>
<style>
.header {
    width: auto;
    height: 150px;

    background-image: url("../../assets/img/background.jpg");
}

.router-link-active {
    text-decoration: none;
    color: white;
    font-size: large;
}

a {
    text-decoration: none;
    color: black;
}

.el-row {
    transform: translateY(50%);
}

img {
    transform: translateY(-30%);
    width: 50px;
    height: 50px;

    border-radius: 50%;

}
</style>

<script>
</script>
