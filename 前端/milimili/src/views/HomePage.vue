<template>
    <div v-if="this.$store.state.isLogin == false">
        <div>尚未登录，请前往登录或注册</div>
        <router-link to="/login">登录</router-link> |
        <router-link to="/login">注册</router-link>
    </div>
    <div v-else>
        <div class="personal homepage">
            <router-link to="/personal">主页界面</router-link>
        </div>
    </div>
</template>
