<template>
    <div class="login">
        <div v-if="this.$store.state.isLogin == false">
            <div class="container">
                <div class="main">
                    <!-- 整个注册盒子 -->
                    <div class="loginbox">
                        <!-- 左侧的注册盒子 -->
                        <div class="loginbox-in">
                            <div class="userbox">
                                <el-avatar :size="30"> user </el-avatar>
                                <input class="user" id="user" placeholder="用户名">
                            </div>
                            <br>
                            <div class="pwdbox">
                                <el-avatar :size="30"> pwd </el-avatar>
                                <input class="pwd" id="password" type="password" placeholder="密码">
                            </div>
                            <br>
                            <el-button type="primary" @click="this.$store.commit('login')">登录</el-button> |
                            <router-link to="/register"><el-button class="register_btn"
                                    type="success">注册</el-button></router-link>
                        </div>
                        <!-- 右侧的注册盒子 -->
                        <div class="background">
                            <div class="title">Welcome to MiLiMiLi</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-else>
            <el-button type="info" @click="this.$store.commit('logout')">退出登录</el-button>
        </div>
    </div>
</template>
